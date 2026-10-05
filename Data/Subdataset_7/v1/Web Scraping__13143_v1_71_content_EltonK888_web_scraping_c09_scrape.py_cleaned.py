import os
import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
b1 = r'https:
b2 = requests.get(b1).text
b3 = FPDF(format='letter')
b3.add_page()
b3.set_font("Arial", b4 = 12)
b5 = BeautifulSoup(b2, 'html.parser')
def fonk1():
    '''
    Finds the name of every lecture pdf and saves it to the current directory
    Writes all reading links to a pdf called c09_readings.pdf
    '''
    b6 = b5.find_all('div', class_='notes')
    b7 = b5.find_all('div', class_='readings')
    for i in range(len(b6)):
        try:
            b8 = b6[i].find_all('a')
            b9 = b7[i].find_all('a')
        except Exception as e:
            print("Error:", e)
            pass
        else:
            for j in range(len(b8)):
                b10 = b8[j]['href']
                b11 = b10.split('/')[-1]
                urllib.request.urlretrieve(b1 + b10, b11)
                print("Successfully downloaded: " + b10 + " and saved as: " + b11)
            for k in range(len(b9)):
                b12 = b9[k]['href']
                b3.cell(200, 10, b13 = b12, ln=True)
                print('Wrote ' + b12 + " to b3 file")
    b3.output('c09_urls.pdf')
if b14 = = "__main__":
    fonk1()