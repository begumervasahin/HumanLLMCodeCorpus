import fitz
from storage import enumrateFilenames
def fonk1():
    b1 = []
    b2 = enumrateFilenames()
    for pdf_file in b2:
        b1.extend(fonk2(pdf_file))
    return b1
def fonk2(pdf_filename):
    b1 = []
    with fitz.open(pdf_filename) as pdf_document:
        for page in pdf_document:
            b1.append((pdf_filename, page.get_text()))
    return b1
def fonk3(b1):
    for pdf_file, text in b1:
        print(f"PDF Name: {pdf_file}")
        print(f"Text: {text}")
        print("\n" + "="*80 + "\n")
if b3 = = "__main__":
    b4 = fonk1()
    fonk3(b4)
    b5 = fonk2("path/to/your/pdf.pdf")
    fonk3(b5)