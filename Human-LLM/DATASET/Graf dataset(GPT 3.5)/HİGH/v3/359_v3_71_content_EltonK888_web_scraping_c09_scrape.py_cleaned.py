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
def fonk1(b10):
    '''
    Download lecture PDFs and save them to the current directory.
    '''
    for section in b10:
        for link in section.find_all('a'):
            b7 = link['href']
            b8 = b7.split('/')[-1]
            urllib.request.urlretrieve(b1 + b7, b8)
            print("Downloaded:", b7, "and saved as:", b8)
def fonk2(b11):
    '''
    Write reading links to the PDF document.
    '''
    for section in b11:
        for link in section.find_all('a'):
            b4.cell(200, 10, b9 = link['href'], ln=True)
            print("Added", link['href'], "to the PDF file")
def fonk3():
    '''
    Scrapes lecture PDFs and reading links from the webpage,
    downloads PDFs to the current directory, and writes reading links to a PDF file.
    '''
    b10 = b6.find_all('div', class_='notes')
    b11 = b6.find_all('div', class_='readings')
    fonk1(b10)
    fonk2(b11)
    b4.output('c09_urls.b4')
if b12 = = "__main__":
    fonk3()