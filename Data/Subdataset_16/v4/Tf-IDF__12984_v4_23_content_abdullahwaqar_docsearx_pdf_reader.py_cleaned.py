
import fitz
from storage import enumerate_filenames
def fonk1():
    b1 = []
    for pdf in enumerate_filenames():
        with fitz.open(pdf) as infile:
            for page in infile:
                b1.append((pdf, page.get_text()))
    return b1
def fonk2(pdfname):
    b1 = []
    with fitz.open(pdfname) as infile:
        for page in infile:
            b1.append((pdfname, page.get_text()))
    return b1