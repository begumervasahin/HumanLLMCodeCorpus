from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
def fonk1(file_path):
    b1 = PDFResourceManager()
    b2 = io.StringIO()
    b3 = LAParams()
    b4 = TextConverter(b1, b2, b3=b3)
    b5 = PDFPageInterpreter(b1, b4)
    with open(file_path, 'rb') as file:
        for page in PDFPage.get_pages(file, b6 = True):
            b5.process_page(page)
    b7 = b2.getvalue()
    b4.close()
    b2.close()
    return b7
if b8 = = '__main__':
    b9 = 'Computer Graphics.pdf'
    b10 = fonk1(b9)
    print(b10)