import urllib.request
from bs4 import BeautifulSoup
import songline
def fonk1(a1):
    try:
        b1 = f'https:
        with urllib.request.urlopen(b1) as response:
            b2 = response.read()
        b3 = BeautifulSoup(b2, 'html.parser')
        b4 = b3.find('td', class_='strokeme').text
        b5 = b3.find('span', class_='title').text.replace('Â ', '')
        print(f'Province: {b5}, Temperature: {b4}')
        b6 = f'Province: {b5}, Temperature: {b4}'
        return b6
    except Exception as e:
        print('Error:', e)
        return 'No Result'
def fonk2():
    b7 = 'Your_Songline_Token_Here'
    b8 = songline.Sendline(b7)
    a1 = 2
    b9 = fonk1(a1)
    if b9 != 'No Result':
        b8.sendtext(b9)
if b10 = = "__main__":
    fonk2()