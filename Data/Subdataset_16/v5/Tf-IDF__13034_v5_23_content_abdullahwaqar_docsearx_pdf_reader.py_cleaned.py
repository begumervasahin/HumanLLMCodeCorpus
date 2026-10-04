
import fitz
from storage import enumerate_filenames
def fonk1(pdf_path):
    b1 = []
    with fitz.open(pdf_path) as infile:
        for page in infile:
            b1.append((pdf_path, page.get_text()))
    return b1
def fonk2():
    b2 = []
    for pdf in enumerate_filenames():
        b2.extend(fonk1(pdf))
    return b2
def fonk3(pdf_path):
    return fonk1(pdf_path)