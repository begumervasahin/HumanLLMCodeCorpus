import urllib.request
import fpdf
import requests
from bs4 import BeautifulSoup
b1 = r'https:
b2 = requests.get(b1).text
b3 = fpdf.FPDF(format='letter')
b3.add_page()
b3.set_font("Arial", b4 = 12)
b5 = BeautifulSoup(b2, 'lxml')
def fonk1(b11):
    for link in b11:
        b6 = b1 + link['href']
        b7 = link['href'].split('/')[-1]
        urllib.request.urlretrieve(b6, b7)
        print(f"Downloaded: {b6} -> {b7}")
def fonk2(b12):
    for link in b12:
        b8 = link['href']
        b3.write(5, b8 + '\n')
        print(f"Wrote: {b8} to PDF file")
def fonk3():
    '''
    Scrapes lecture notes and reading URLs, saves lecture notes to current directory,
    and writes reading URLs to a PDF file called c01_urls.pdf.
    '''
    b9 = b5.find_all('div', class_='notes')
    b10 = b5.find_all('div', class_='readings')
    for i in range(len(b9)):
        try:
            b11 = b9[i].find_all('a')
            b12 = b10[i].find_all('a')
        except:
            pass
        else:
            fonk1(b11)
            fonk2(b12)
    b3.output('c01_urls.pdf')
if b13 = = "__main__":
    fonk3()