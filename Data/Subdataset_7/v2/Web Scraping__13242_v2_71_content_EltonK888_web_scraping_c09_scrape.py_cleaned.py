import os
import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
b1 = r'https:
b2 = requests.get(b1)
b3 = b2.text
b4 = FPDF(format='letter')
b4.add_page()
b4.set_font("Arial", b5 = 12)
b6 = BeautifulSoup(b3, 'html.parser')
def fonk1():
    '''
    Scrapes lecture PDFs and reading links from the webpage,
    downloads PDFs to the current directory, and writes reading links to a PDF file.
    '''
    b7 = b6.find_all('div', class_='notes')
    b8 = b6.find_all('div', class_='readings')
    for i in range(len(b7)):
        try:
            b9 = b7[i].find_all('a')
            b10 = b8[i].find_all('a')
        except Exception as e:
            print("Error:", e)
            continue
        else:
            for lecture_file in b9:
                b11 = lecture_file['href']
                b12 = b11.split('/')[-1]
                urllib.request.urlretrieve(b1 + b11, b12)
                print("Downloaded: " + b11 + " and saved as: " + b12)
            for reading_url in b10:
                b4.cell(200, 10, b13 = reading_url['href'], ln=True)
                print('Added ' + reading_url['href'] + " to the PDF file")
    b4.output('c09_urls.b4')
if b14 = = "__main__":
    fonk1()