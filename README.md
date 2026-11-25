# PDF Bookmark Generator

A simple Python program that adds custom bookmarks to a PDF file.

The program uses PyMuPDF to create bookmarks from a predefined template. It supports chapters, subsections, and nested subsections.

## Requirements

- Python
- The provided `.venv` virtual environment, which contains PyMuPDF

## Project Structure

```text
PDF-Bookmark-Generator/
│
├── main.py
├── .venv/
├── input/
└── output/
```

## How to Use

### 1. Prepare the PDF

Place the PDF file you want to modify inside the `input` folder.

The program accepts only one PDF file at a time. Remove any previous PDF files from the input folder before running the program.

Non-PDF files are ignored.

### 2. Configure the Bookmarks

Open `main.py` and find the `BOOKMARK_TEMPLATE` dictionary.

Modify the dictionary according to the chapters and page numbers of your book.

Example:

```python
BOOKMARK_TEMPLATE = {
    "Introduction": 1,

    "Chapter 1": {
        "Section 1.1": 5,
        "Section 1.2": 10,
    },

    "Chapter 2": {
        "Section 2.1": 20,
        "Section 2.2": 25,
    },
}
```

The dictionary structure determines the bookmark hierarchy.

- A number represents the PDF page number.
- A dictionary represents a chapter containing subsections.
- Dictionaries can be nested to create additional levels of bookmarks.

Page numbers must correspond to the actual PDF page numbers, starting from 1.

### 3. Run the Program

The program must be executed using the provided virtual environment.

**Windows:**

```powershell
.\.venv\Scripts\python.exe main.py
```

**Linux:**

```bash
./.venv/bin/python main.py
```

No additional user input is required.

### 4. Get the Output

The program creates the bookmarked PDF inside the `output` folder.

The output filename is generated automatically using the original PDF filename.

For example:

```text
input/book.pdf
```

Produces:

```text
output/book_bookmarked.pdf
```

## How the Code Works

### `get_input_pdf()`

Finds the PDF file inside the input folder.

- Ignores non-PDF files.
- Raises an exception if no PDF is found.
- Raises an exception if more than one PDF is found.

### `build_toc()`

Converts the bookmark template into the table of contents format required by PyMuPDF.

It uses recursion to process nested dictionaries and generate the correct bookmark hierarchy.

### `add_bookmarks()`

Opens the input PDF, removes all existing bookmarks, and adds the new bookmarks generated from the template.

The modified PDF is saved in the output folder.

### `main()`

Runs the complete process:

1. Finds the input PDF.
2. Generates the bookmarks.
3. Saves the output PDF.

## Important Notes

- Existing bookmarks are removed before new bookmarks are added.
- The original PDF in the input folder is not modified.
- The output folder is created automatically if it does not exist.
- The input folder should contain only one PDF file.
- The bookmark template must be updated for each new book.
- The program does not automatically detect chapter titles or page numbers.
