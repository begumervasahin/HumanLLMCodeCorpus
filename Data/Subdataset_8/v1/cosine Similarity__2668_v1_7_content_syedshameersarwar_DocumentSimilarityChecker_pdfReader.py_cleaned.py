from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
def pdf_to_text(pdf_file):
    resource_manager = PDFResourceManager()
    output_string = io.StringIO()
    layout_params = LAParams()
    text_converter = TextConverter(resource_manager, output_string, laparams=layout_params)
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    with open(pdf_file, 'rb') as file_object:
        for page in PDFPage.get_pages(file_object, check_extractable=True):
            interpreter.process_page(page)
    text = output_string.getvalue()
    file_object.close()
    text_converter.close()
    output_string.close()
    return text
if __name__ == '__main__':
    pdf_file_path = 'Computer Graphics.pdf'
    extracted_text = pdf_to_text(pdf_file_path)
    print(extracted_text)