
import fitz
from storage import enumrateFilenames
def read_all_pdfs():
    pages = []
    for pdf in enumrateFilenames():
        with fitz.open(pdf) as infile:
            for page in infile:
                pages.append((pdf, page.get_text()))
    return pages
def read_pdf(pdf_name):
    pages = []
    with fitz.open(pdf_name) as infile:
        for page in infile:
            pages.append((pdf_name, page.get_text()))
    return pages