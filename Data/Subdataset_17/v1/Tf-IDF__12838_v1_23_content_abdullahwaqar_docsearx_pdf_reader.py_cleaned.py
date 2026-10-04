import fitz
from storage import enumrateFilenames
def readAllPdf():
    pages = []
    for pdf in enumrateFilenames():
        with fitz.open(pdf) as infile:
            for page in infile:
                pages.append((pdf, page.get_text()))
    return pages
def readPdf(pdfname):
    pages = []
    with fitz.open(pdfname) as infile:
        for page in infile:
            pages.append((pdfname, page.get_text()))
    return pages
if __name__ == "__main__":
    all_pdfs = readAllPdf()
    for pdf in all_pdfs:
        print(f"PDF Name: {pdf[0]}")
        print(f"Text: {pdf[1]}")
        print("\n" + "="*80 + "\n")
    specific_pdf = readPdf("path/to/your/pdf.pdf")
    for pdf in specific_pdf:
        print(f"PDF Name: {pdf[0]}")
        print(f"Text: {pdf[1]}")
        print("\n" + "="*80 + "\n")