from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
def pdf_to_text(file_path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(file_path, 'rb') as file:
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)
    text = retstr.getvalue()
    device.close()
    retstr.close()
    return text
if __name__ == '__main__':
    pdf_path = 'Computer Graphics.pdf'
    extracted_text = pdf_to_text(pdf_path)
    print(extracted_text)