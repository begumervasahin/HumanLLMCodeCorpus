
import fitz
from storage import enumerate_filenames
def read_all_pdfs():
    pdf_texts = []
    for pdf in enumerate_filenames():
        with fitz.open(pdf) as infile:
            for page in infile:
                pdf_texts.append((pdf, page.get_text()))
    return pdf_texts
def read_pdf(pdfname):
    pdf_texts = []
    with fitz.open(pdfname) as infile:
        for page in infile:
            pdf_texts.append((pdfname, page.get_text()))
    return pdf_texts