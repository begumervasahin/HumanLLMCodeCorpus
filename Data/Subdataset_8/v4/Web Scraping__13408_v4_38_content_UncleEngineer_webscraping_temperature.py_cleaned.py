
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import songline
def get_temperature(province_id):
    try:
        url = 'https:
        web_open = req(url)
        page_html = web_open.read()
        web_open.close()
        data = soup(page_html, 'html.parser')
        temperature = data.findAll('td', {'class': 'strokeme'})[0].text
        province_name = data.findAll('span', {'class': 'title'})[0].text.replace('Â ', '')
        print('Province:', province_name, 'Temperature:', temperature)
        message = 'Province: {} Temperature: {}'.format(province_name, temperature)
        return message
    except Exception as e:
        print('Error occurred:', e)
        return 'No Result'
token = 'fjcOrtgQPPbsmYmIz4OX94nNHt8u8yi1kd1A6JjGOXC'
messenger = songline.Sendline(token)
my_province_data = get_temperature(2)
messenger.sendtext(my_province_data)
'''
for province_id in range(1, 100):
    print(province_id)
    get_temperature(province_id)
    print('----')
'''