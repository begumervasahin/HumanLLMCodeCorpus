
import fitz
from storage import enumrateFilenames
def read_all_pdfs():
    pages = []
    for pdf in enumrateFilenames():
        with fitz.open(pdf) as infile:
            for page in infile:
                pages.append((pdf, page.get_text()))
    return pages
def read_pdf(pdfname):
    pages = []
    with fitz.open(pdfname) as infile:
        for page in infile:
            pages.append((pdfname, page.get_text()))
    return pages