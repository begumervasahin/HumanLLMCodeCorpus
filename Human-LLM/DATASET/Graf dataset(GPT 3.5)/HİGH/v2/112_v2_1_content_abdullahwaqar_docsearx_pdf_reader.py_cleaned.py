import fitz
from storage import enumerate_filenames
def fonk1():
    b1 = []
    for pdf_file in enumerate_filenames():
        with fitz.open(pdf_file) as pdf_document:
            for page in pdf_document:
                b1.append((pdf_file, page.get_text()))
    return b1
def fonk2(pdf_path):
    b2 = []
    with fitz.open(pdf_path) as pdf_file:
        for page in pdf_file:
            b2.append((pdf_path, page.get_text()))
    return b2