
import fitz
from storage import enumrateFilenames
def readAllPdf():
    pages = []
    for pdf in enumrateFilenames():
        with fitz.open(pdf) as infile:
            for page in infile:
                pages.append((pdf, page.getText()))
    return pages
def readPdf(pdfname):
    pages = []
    with fitz.open(pdfname) as infile:
        for page in infile:
            pages.append((pdfname, page.getText()))
    return pages