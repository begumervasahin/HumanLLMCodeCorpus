
from urllib.request import urlopen as open_url
from bs4 import BeautifulSoup as parse_html
import songline
def fonk1(a1):
    try:
        b1 = 'https:
        with open_url(b1) as web_data:
            b2 = web_data.read()
        web_data.close()
        b3 = parse_html(b2, 'html.parser')
        b4 = b3.findAll('td', {'class': 'strokeme'})[0].text
        b5 = b3.findAll('span', {'class': 'title'})[0].text.replace('Â ', '')
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