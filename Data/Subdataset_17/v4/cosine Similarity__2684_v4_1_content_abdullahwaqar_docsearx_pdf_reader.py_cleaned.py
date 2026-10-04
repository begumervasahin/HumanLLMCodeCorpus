
import fitz
from storage import enumrateFilenames
def read_all_pdfs():
    pdf_pages = []
    for pdf_filename in enumrateFilenames():
        with fitz.open(pdf_filename) as pdf_file:
            for page in pdf_file:
                pdf_pages.append((pdf_filename, page.get_text()))
    return pdf_pages
def read_pdf(pdf_filename):
    pdf_pages = []
    with fitz.open(pdf_filename) as pdf_file:
        for page in pdf_file:
            pdf_pages.append((pdf_filename, page.get_text()))
    return pdf_pages
if __name__ == "__main__":
    all_pdfs = read_all_pdfs()
    for pdf, text in all_pdfs:
        print(f"PDF: {pdf}\nText: {text[:100]}...\n")
