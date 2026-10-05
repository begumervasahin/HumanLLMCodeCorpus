from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import songline
def fonk1(pvid):
    try:
        b1 = 'https:
        b2 = req(b1)
        b3 = b2.read()
        b2.close()
        b4 = soup(b3, 'html.parser')
        b5 = b4.findAll('td', {'class': 'strokeme'})
        b6 = b4.findAll('span', {'class': 'title'})
        b7 = b6[0].b9.replace('Â ', '')
        b8 = b5[0].b9
        print('Province: {} Temperature: {}'.format(b7, b8))
        b9 = 'Province: {} Temperature: {}'.format(b7, b8)
        return b9
    except Exception as e:
        print('Error:', e)
        return 'No Result'
def fonk2():
    b10 = 'Your_Songline_Token_Here'
    b11 = songline.Sendline(b10)
    a1 = 2
    b12 = fonk1(a1)
    if b12 != 'No Result':
        b11.sendtext(b12)
if b13 = = "__main__":
    fonk2()