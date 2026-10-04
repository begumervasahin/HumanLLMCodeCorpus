import fitz
from storage import enumrateFilenames
def fonk1():
    b1 = []
    for pdf_file in enumrateFilenames():
        with fitz.open(pdf_file) as pdf_document:
            for page in pdf_document:
                b1.append((pdf_file, page.get_text()))
    return b1
def fonk2(pdf_filename):
    b1 = []
    with fitz.open(pdf_filename) as pdf_document:
        for page in pdf_document:
            b1.append((pdf_filename, page.get_text()))
    return b1
if b2 = = "__main__":
    b3 = fonk1()
    for pdf_file, text in b3:
        print(f"PDF Name: {pdf_file}")
        print(f"Text: {text}")
        print("\n" + "="*80 + "\n")
    b4 = fonk2("path/to/your/pdf.pdf")
    for pdf_file, text in b4:
        print(f"PDF Name: {pdf_file}")
        print(f"Text: {text}")
        print("\n" + "="*80 + "\n")