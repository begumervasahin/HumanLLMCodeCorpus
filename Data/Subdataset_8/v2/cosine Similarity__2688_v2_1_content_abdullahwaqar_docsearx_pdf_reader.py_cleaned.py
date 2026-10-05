import fitz
from storage import enumerate_filenames
def read_all_pdfs():
    all_pages = []
    for pdf_file in enumerate_filenames():
        with fitz.open(pdf_file) as pdf_document:
            for page in pdf_document:
                all_pages.append((pdf_file, page.get_text()))
    return all_pages
def read_pdf(pdf_path):
    pages = []
    with fitz.open(pdf_path) as pdf_file:
        for page in pdf_file:
            pages.append((pdf_path, page.get_text()))
    return pages