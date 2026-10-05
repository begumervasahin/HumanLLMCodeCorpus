import fitz
from storage import enumerate_filenames
def fonk1():
    b1 = []
    for pdf_file in enumerate_filenames():
        with fitz.open(pdf_file) as pdf_document:
            for page in pdf_document:
                b2 = page.get_text()
                b1.append((pdf_file, b2))
    return b1
def fonk2(pdf_path):
    b3 = []
    with fitz.open(pdf_path) as pdf_document:
        for page in pdf_document:
            b2 = page.get_text()
            b3.append((pdf_path, b2))
    return b3