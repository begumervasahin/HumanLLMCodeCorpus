import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
b1 = 'https:
b2 = requests.get(b1).text
b3 = FPDF(format='letter')
b3.add_page()
b3.set_font("Arial", b4 = 12)
b5 = BeautifulSoup(b2, 'lxml')
def fonk1():
    '''
    Scrapes lecture materials from the webpage and saves them locally.
    Writes all reading links to a PDF file named 'c01_readings.b3'.
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
            for note in b8:
                b10 = note['href']
                b11 = b10.split('/')[-1]
                urllib.request.urlretrieve(b1 + b10, b11)
                print("Successfully downloaded: " + b10 + " and saved as: " + b11)
            for url in b9:
                b3.write(5, url['href'] + '\n')
                print('Wrote ' + url['href'] + " to the PDF file")
    b3.output('c01_urls.b3')
if b12 = = "__main__":
    fonk1()