'''
- Make sure you have max 1 pdf file in input folder.
- Write your bookmarks in BOOKMARK_TEMPLATE
- Running script for;
* Windows users:
    .venv\Scripts\python.exe main.py
* Linux users:
    .venv/bin/python main.py
'''

from pathlib import Path
import pymupdf

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

BOOKMARK_TEMPLATE = {
    "Contents": 7,

    "1. Introduction": 20,

    "2. Air Conditioning Systems": {
        "2.1 Basic Principles": 41,
        "2.2 System Components": 45,
        "2.3 Types of Systems": {
            "2.3.1 Central Systems": 48,
            "2.3.2 Individual Systems": 52,
        },
    },

    "3. Moist Air and Conditioning Processes": {
        "3.1 Properties of Moist Air": 68,
        "3.2 Psychrometric Chart": 75,
        "3.3 Conditioning Processes": 82,
    },

    "4. Comfort and Health – Indoor Environmental Quality": 104,
}


def get_input_pdf() -> Path:

    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = [
        file for file in INPUT_DIR.iterdir()
        if file.is_file() and file.suffix.lower() == ".pdf"
    ]

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF file found in the input folder."
        )

    if len(pdf_files) > 1:
        raise ValueError(
            "More than one PDF file found in the input folder. "
            "Please keep only one PDF file."
        )

    return pdf_files[0]

# 2. Convert template to TOC

def build_toc(bookmark_template, level=1):

    toc = []

    for title, value in bookmark_template.items():

        if isinstance(value, dict):

            # Add the parent bookmark.
            # Its page is the first page of its first subsection.
            first_page = next(iter(value.values()))

            if isinstance(first_page, dict):
                first_page = next(iter(first_page.values()))

            toc.append([level, title, first_page])

            # Recursively add subsections.
            toc.extend(build_toc(value, level + 1))

        else:

            toc.append([level, title, value])

    return toc


def add_bookmarks(input_pdf: Path, bookmark_template: dict) -> Path:

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_pdf = OUTPUT_DIR / f"{input_pdf.stem}_bookmarked.pdf"

    with pymupdf.open(input_pdf) as doc:

        # Remove all existing bookmarks.
        doc.set_toc([])

        # Generate new bookmarks.
        toc = build_toc(bookmark_template)

        # Add the new bookmarks.
        doc.set_toc(toc)

        doc.save(output_pdf)

    return output_pdf

def main():

    input_pdf = get_input_pdf()
    output_pdf = add_bookmarks(input_pdf, BOOKMARK_TEMPLATE)

    print("Bookmarks added successfully.")


if __name__ == "__main__":
    main()
