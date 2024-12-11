
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import songline
def fonk1(province_id):
    try:
        b1 = 'https:
        b2 = req(b1)
        b3 = b2.read()
        b2.close()
        b4 = soup(b3, 'html.parser')
        b5 = b4.findAll('td', {'class': 'strokeme'})[0].text
        b6 = b4.findAll('span', {'class': 'title'})[0].text.replace('Â ', '')
        print('Province:', b6, 'Temperature:', b5)
        b7 = 'Province: {} Temperature: {}'.format(b6, b5)
        return b7
    except Exception as e:
        print('Error occurred:', e)
        return 'No Result'
b8 = 'fjcOrtgQPPbsmYmIz4OX94nNHt8u8yi1kd1A6JjGOXC'
b9 = songline.Sendline(b8)
b10 = fonk1(2)
b9.sendtext(b10)
'''
for province_id in range(1, 100):
    print(province_id)
    fonk1(province_id)
    print('----')
'''