
from urllib.request import urlopen
from bs4 import BeautifulSoup
import songline
def fonk1(province_id):
    try:
        b1 = f'https:
        with urlopen(b1) as web_open:
            b2 = web_open.read()
        b3 = BeautifulSoup(b2, 'html.parser')
        b4 = b3.find('td', class_='strokeme').text
        b5 = b3.find('span', class_='title').text.strip()
        print('Province:', b5, 'Temperature:', b4)
        b6 = f'Province: {b5} Temperature: {b4}'
        return b6
    except Exception as e:
        print('Error occurred:', e)
        return 'No Result'
b7 = 'fjcOrtgQPPbsmYmIz4OX94nNHt8u8yi1kd1A6JjGOXC'
b8 = songline.Sendline(b7)
b9 = fonk1(2)
b8.sendtext(b9)
'''
for province_id in range(1, 100):
    print(province_id)
    fonk1(province_id)
    print('----')
'''