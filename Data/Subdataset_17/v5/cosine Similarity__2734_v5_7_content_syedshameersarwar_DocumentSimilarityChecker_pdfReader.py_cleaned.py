import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def pdf_to_text(file_path):
    resource_manager = PDFResourceManager()
    output_string = io.StringIO()
    laparams = LAParams()
    with TextConverter(resource_manager, output_string, laparams=laparams) as device:
        interpreter = PDFPageInterpreter(resource_manager, device)
        with open(file_path, 'rb') as file:
            for page in PDFPage.get_pages(file, check_extractable=True):
                interpreter.process_page(page)
        text = output_string.getvalue()
    return text
if __name__ == '__main__':
    pdf_path = 'Computer Graphics.pdf'
    extracted_text = pdf_to_text(pdf_path)
    print(extracted_text)