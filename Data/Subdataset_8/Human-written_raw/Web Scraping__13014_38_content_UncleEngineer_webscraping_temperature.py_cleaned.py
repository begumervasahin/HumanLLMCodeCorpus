from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
def Temperature(pvid):
    try:
        url = 'https:
        webopen = req(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html,'html.parser')
        temp = data.findAll('td',{'class':'strokeme'})
        province = data.findAll('span',{'class':'title'})
        pv = province[0].text.replace('Â ','')
        result = temp[0].text
        print('à¸à¸±à¸à¸«à¸§à¸±à¸: {} à¸­à¸¸à¸à¸«à¸ à¸¹à¸¡à¸´: {}'.format(pv,result))
        text = 'à¸à¸±à¸à¸«à¸§à¸±à¸: {} à¸­à¸¸à¸à¸«à¸ à¸¹à¸¡à¸´: {}'.format(pv,result)
        return text
    except:
        print('No Result')
        return 'No Result'
import songline
token = 'fjcOrtgQPPbsmYmIz4OX94nNHt8u8yi1kd1A6JjGOXC'
messenger = songline.Sendline(token)
myprovince = Temperature(2)
messenger.sendtext(myprovince)
'''
for i in range(1,100):
    print(i)
    Temperature(i)
    print('----')
'''