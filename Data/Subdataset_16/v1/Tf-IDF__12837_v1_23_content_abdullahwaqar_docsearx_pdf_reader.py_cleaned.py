import fitz
from storage import enumrateFilenames
def fonk1():
    b1 = []
    for pdf in enumrateFilenames():
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
if b2 = = "__main__":
    b3 = fonk1()
    for pdf in b3:
        print(f"PDF Name: {pdf[0]}")
        print(f"Text: {pdf[1]}")
        print("\n" + "="*80 + "\n")
    b4 = fonk2("path/to/your/pdf.pdf")
    for pdf in b4:
        print(f"PDF Name: {pdf[0]}")
        print(f"Text: {pdf[1]}")
        print("\n" + "="*80 + "\n")