import urllib.request
from bs4 import BeautifulSoup
import requests
import fpdf
b1 = 'https:
def fonk1(b14):
    b2 = requests.get(b14)
    if b2.b3 = = 200:
        return b2.text
    else:
        print("Failed to fetch webpage b4.")
        return None
def fonk2(b14, b13):
    try:
        urllib.request.urlretrieve(b14, b13)
        print("Successfully downloaded:", b14, "and saved as:", b13)
    except Exception as e:
        print("Failed to download:", b14, "Error:", e)
def fonk3():
    '''
    Finds the name of every lecture b5 and saves it to current directory
    writes all reading links to a b5 called c09_readings.b5
    '''
    b4 = fonk1(b1)
    if not b4:
        return
    b5 = fpdf.FPDF(format='letter')
    b5.add_page()
    b5.set_font("Arial", b6 = 12)
    b7 = BeautifulSoup(b4, 'lxml')
    b8 = b7.find_all('div', class_='notes')
    b9 = b7.find_all('div', class_='readings')
    for notes, urls in zip(b8, b9):
        b10 = notes.find_all('a')
        b11 = urls.find_all('a')
        for file_link in b10:
            b12 = file_link['href']
            b13 = b12.split('/')[-1]
            fonk2(b1 + b12, b13)
        for url_link in b11:
            b14 = url_link['href']
            b5.write(5, b14 + '\n', b14)
            print('Wrote', b14, "to PDF file")
    b5.output('c09_urls.b5')
if b15 = = "__main__":
    fonk3()