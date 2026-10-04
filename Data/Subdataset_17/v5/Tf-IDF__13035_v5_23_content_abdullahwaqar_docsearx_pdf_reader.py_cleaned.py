
import fitz
from storage import enumerate_filenames
def extract_text_from_pdf(pdf_path):
    pdf_texts = []
    with fitz.open(pdf_path) as infile:
        for page in infile:
            pdf_texts.append((pdf_path, page.get_text()))
    return pdf_texts
def read_all_pdfs():
    all_pdfs_texts = []
    for pdf in enumerate_filenames():
        all_pdfs_texts.extend(extract_text_from_pdf(pdf))
    return all_pdfs_texts
def read_pdf(pdf_path):
    return extract_text_from_pdf(pdf_path)