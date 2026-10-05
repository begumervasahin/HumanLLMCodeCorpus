from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
def fonk1(pdf_file):
    b1 = PDFResourceManager()
    b2 = io.StringIO()
    b3 = LAParams()
    b4 = TextConverter(b1, b2, laparams=b3)
    b5 = PDFPageInterpreter(b1, b4)
    with open(pdf_file, 'rb') as file_object:
        for page in PDFPage.get_pages(file_object, b6 = True):
            b5.process_page(page)
    b7 = b2.getvalue()
    file_object.close()
    b4.close()
    b2.close()
    return b7
if b8 = = '__main__':
    b9 = 'Computer Graphics.pdf'
    b10 = fonk1(b9)
    print(b10)