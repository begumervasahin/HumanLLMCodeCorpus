import fitz
from storage import enumrateFilenames
def read_all_pdfs():
    pdf_texts = []
    for pdf_file in enumrateFilenames():
        with fitz.open(pdf_file) as pdf_document:
            for page in pdf_document:
                pdf_texts.append((pdf_file, page.get_text()))
    return pdf_texts
def read_pdf(pdf_filename):
    pdf_texts = []
    with fitz.open(pdf_filename) as pdf_document:
        for page in pdf_document:
            pdf_texts.append((pdf_filename, page.get_text()))
    return pdf_texts
if __name__ == "__main__":
    all_pdfs = read_all_pdfs()
    for pdf_file, text in all_pdfs:
        print(f"PDF Name: {pdf_file}")
        print(f"Text: {text}")
        print("\n" + "="*80 + "\n")
    specific_pdf = read_pdf("path/to/your/pdf.pdf")
    for pdf_file, text in specific_pdf:
        print(f"PDF Name: {pdf_file}")
        print(f"Text: {text}")
        print("\n" + "="*80 + "\n")