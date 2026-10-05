
from urllib.request import urlopen
from bs4 import BeautifulSoup
import songline
def get_temperature(province_id):
    try:
        url = f'https:
        with urlopen(url) as web_open:
            page_html = web_open.read()
        soup_data = BeautifulSoup(page_html, 'html.parser')
        temperature = soup_data.find('td', class_='strokeme').text
        province_name = soup_data.find('span', class_='title').text.strip()
        print('Province:', province_name, 'Temperature:', temperature)
        message = f'Province: {province_name} Temperature: {temperature}'
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