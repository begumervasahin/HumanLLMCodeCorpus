import urllib.request
from bs4 import BeautifulSoup
import requests
import fpdf
b1 = 'https:
b2 = requests.get(b1).text
b3 = fpdf.FPDF(format='letter')
b3.add_page()
b3.set_font("Arial", b4 = 12)
b5 = BeautifulSoup(b2, 'lxml')
def fonk1():
    '''
    Finds the name of every lecture b3 and saves it to current directory
    writes all reading links to a b3 called c09_readings.b3
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
            for j in range(len(b8)):
                b10 = b8[j]['href']
                b11 = b10.split('/')[-1]
                urllib.request.urlretrieve(b1+b10, b11)
                print("Successfully downloaded: " + b10 + " and saved as: " + b11)
            for k in range(len(b9)):
                b12 = b9[k]['href']
                b3.write(5, b12+'\n', b12)
                print('Wrote ' + b12 + " to PDF file")
    b3.output('c09_urls.b3')
if b13 = = "__main__":
    fonk1()