from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
def convert_pdf_to_text(pdf_file_path):
    resource_manager = PDFResourceManager()
    output_string = io.StringIO()
    layout_params = LAParams()
    text_converter = TextConverter(resource_manager, output_string, codec='utf-8', laparams=layout_params)
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    with open(pdf_file_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file, check_extractable=True):
            interpreter.process_page(page)
    converted_text = output_string.getvalue()
    pdf_file.close()
    text_converter.close()
    output_string.close()
    return converted_text
if __name__ == '__main__':
    pdf_file_path = 'Computer Graphics.pdf'
    extracted_text = convert_pdf_to_text(pdf_file_path)
    print(extracted_text)