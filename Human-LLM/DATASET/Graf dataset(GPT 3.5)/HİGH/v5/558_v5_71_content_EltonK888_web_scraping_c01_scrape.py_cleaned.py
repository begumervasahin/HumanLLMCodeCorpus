import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
b1 = 'https:
def fonk1(url):
    b2 = requests.get(url)
    return b2.text
def fonk2(url, b12):
    urllib.request.urlretrieve(url, b12)
    print("Successfully downloaded:", url, "and saved as:", b12)
def fonk3():
    '''
    Scrapes lecture materials from the webpage and saves them locally.
    Writes all reading links to a PDF file named 'c01_urls.b4'.
    '''
    b3 = fonk1(b1)
    b4 = FPDF(format='letter')
    b4.add_page()
    b4.set_font("Arial", b5 = 12)
    b6 = BeautifulSoup(b3, 'lxml')
    b7 = b6.find_all('div', class_='notes')
    b8 = b6.find_all('div', class_='readings')
    for notes_section, links_section in zip(b7, b8):
        b9 = notes_section.find_all('a')
        b10 = links_section.find_all('a')
        for note_link in b9:
            b11 = note_link['href']
            b12 = b11.split('/')[-1]
            fonk2(b1 + b11, b12)
        for url_link in b10:
            b4.write(5, url_link['href'] + '\n')
            print('Wrote', url_link['href'], 'to the PDF file')
    b4.output('c01_urls.b4')
if b13 = = "__main__":
    fonk3()