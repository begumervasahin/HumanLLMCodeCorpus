import fitz
from storage import enumrateFilenames
def read_all_pdfs():
    pdf_texts = []
    pdf_files = enumrateFilenames()
    for pdf_file in pdf_files:
        pdf_texts.extend(read_pdf(pdf_file))
    return pdf_texts
def read_pdf(pdf_filename):
    pdf_texts = []
    with fitz.open(pdf_filename) as pdf_document:
        for page in pdf_document:
            pdf_texts.append((pdf_filename, page.get_text()))
    return pdf_texts
def display_pdf_texts(pdf_texts):
    for pdf_file, text in pdf_texts:
        print(f"PDF Name: {pdf_file}")
        print(f"Text: {text}")
        print("\n" + "="*80 + "\n")
if __name__ == "__main__":
    all_pdfs = read_all_pdfs()
    display_pdf_texts(all_pdfs)
    specific_pdf = read_pdf("path/to/your/pdf.pdf")
    display_pdf_texts(specific_pdf)