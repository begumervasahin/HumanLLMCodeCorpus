
import fitz
from storage import enumrateFilenames
def fonk1():
    b1 = []
    for pdf_filename in enumrateFilenames():
        with fitz.open(pdf_filename) as pdf_file:
            for page in pdf_file:
                b1.append((pdf_filename, page.get_text()))
    return b1
def fonk2(pdf_filename):
    b1 = []
    with fitz.open(pdf_filename) as pdf_file:
        for page in pdf_file:
            b1.append((pdf_filename, page.get_text()))
    return b1
if b2 = = "__main__":
    b3 = fonk1()
    for pdf, text in b3:
        print(f"PDF: {pdf}\nText: {text[:100]}...\n")
