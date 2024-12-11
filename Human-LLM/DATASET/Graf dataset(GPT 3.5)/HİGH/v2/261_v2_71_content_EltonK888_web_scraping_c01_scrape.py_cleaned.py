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
def fonk1():
    '''
    Scrapes lecture notes and reading URLs, saves lecture notes to current directory,
    and writes reading URLs to a PDF file called c01_urls.pdf.
    '''
    b6 = b5.find_all('div', class_='notes')
    b7 = b5.find_all('div', class_='readings')
    for i in range(len(b6)):
        try:
            b8 = b6[i].find_all('a')
            b9 = b7[i].find_all('a')
        except:
            pass
        else:
            for link in b8:
                b10 = b1 + link['href']
                b11 = link['href'].split('/')[-1]
                urllib.request.urlretrieve(b10, b11)
                print(f"Downloaded: {b10} -> {b11}")
            for link in b9:
                b12 = link['href']
                b3.write(5, b12 + '\n')
                print(f"Wrote: {b12} to PDF file")
    b3.output('c01_urls.pdf')
if b13 = = "__main__":
    fonk1()