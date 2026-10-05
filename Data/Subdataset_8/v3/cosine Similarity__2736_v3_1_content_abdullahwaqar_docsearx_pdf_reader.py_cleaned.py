import fitz
from storage import enumerate_filenames
def read_all_pdfs():
    all_pages = []
    for pdf_file in enumerate_filenames():
        with fitz.open(pdf_file) as pdf_document:
            for page in pdf_document:
                text = page.get_text()
                all_pages.append((pdf_file, text))
    return all_pages
def read_pdf(pdf_path):
    pages = []
    with fitz.open(pdf_path) as pdf_document:
        for page in pdf_document:
            text = page.get_text()
            pages.append((pdf_path, text))
    return pages