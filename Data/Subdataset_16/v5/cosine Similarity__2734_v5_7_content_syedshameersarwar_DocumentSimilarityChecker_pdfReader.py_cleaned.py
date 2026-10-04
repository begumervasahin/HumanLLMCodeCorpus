import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def fonk1(file_path):
    b1 = PDFResourceManager()
    b2 = io.StringIO()
    b3 = LAParams()
    with TextConverter(b1, b2, b3 = b3) as device:
        b4 = PDFPageInterpreter(b1, device)
        with open(file_path, 'rb') as file:
            for page in PDFPage.get_pages(file, b5 = True):
                b4.process_page(page)
        b6 = b2.getvalue()
    return b6
if b7 = = '__main__':
    b8 = 'Computer Graphics.pdf'
    b9 = fonk1(b8)
    print(b9)