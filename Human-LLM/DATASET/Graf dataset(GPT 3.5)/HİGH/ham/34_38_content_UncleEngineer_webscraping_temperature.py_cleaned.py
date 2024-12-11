from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
def fonk1(pvid):
    try:
        b1 = 'https:
        b2 = req(b1)
        b3 = b2.read()
        b2.close()
        b4 = soup(b3,'html.parser')
        b5 = b4.findAll('td',{'class':'strokeme'})
        b6 = b4.findAll('span',{'class':'title'})
        b7 = b6[0].b9.replace('Â ','')
        b8 = b5[0].b9
        print('à¸à¸±à¸à¸«à¸§à¸±à¸: {} à¸­à¸¸à¸à¸«à¸ à¸¹à¸¡à¸´: {}'.format(b7,b8))
        b9 = 'à¸à¸±à¸à¸«à¸§à¸±à¸: {} à¸­à¸¸à¸à¸«à¸ à¸¹à¸¡à¸´: {}'.format(b7,b8)
        return b9
    except:
        print('No Result')
        return 'No Result'
import songline
b10 = 'fjcOrtgQPPbsmYmIz4OX94nNHt8u8yi1kd1A6JjGOXC'
b11 = songline.Sendline(b10)
b12 = fonk1(2)
b11.sendtext(b12)
'''
for i in range(1,100):
    print(i)
    fonk1(i)
    print('----')
'''