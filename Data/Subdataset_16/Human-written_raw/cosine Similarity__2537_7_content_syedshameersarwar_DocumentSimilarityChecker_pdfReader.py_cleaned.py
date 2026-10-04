from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
def fonk1(fileObject):
    b1 = PDFResourceManager()
    b2 = io.StringIO()
    b3 = 'utf-8'
    b4 = LAParams()
    b5 = TextConverter(b1, b2, b3=b3, b4=b4)
    b6 = PDFPageInterpreter(b1, b5)
    b7 = ""
    a1 = 0
    b8 = True
    b9 = set()
    for page in PDFPage.get_pages(fileObject, b9, a1 = a1, b7=b7,b8=b8, check_extractable=True):
        b6.process_page(page)
    b10 = b2.getvalue()
    fileObject.close()
    b5.close()
    b2.close()
    return b10
if b11 = = '__main__':
    fonk1(open('Computer Graphics.pdf','rb'))