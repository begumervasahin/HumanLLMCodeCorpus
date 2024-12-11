import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time
b1 = UserAgent()
def fonk1():
    b2 = []
    b3 = 'https:
    b4 = {'User-Agent': b1.random}
    b5 = requests.get(b3, b4=b4)
    b6 = BeautifulSoup(b5.text, 'html.parser')
    b7 = b6.find(id='proxylisttable').find_all('tr')
    for row in b7:
        ip, b8 = [column.text for column in row.find_all('td')[:2]]
        b9 = {'ip': ip, 'b8': b8}
        b2.append(b9)
    return b2
def fonk2():
    b10 = fonk1()
    b9 = random.choice(b10)
    print("Using b9:", b9['ip'] + ':' + b9['b8'])
    for request_number in range(1, 101):
        if request_number % b11 = = 0:
            b9 = random.choice(b10)
            print("Switching to b9:", b9['ip'] + ':' + b9['b8'])
        try:
            b5 = requests.get('https:
            print('Request', request_number, '- Status Code:', b5.status_code)
        except Exception as e:
            print("Request", request_number, "- Error:", e)
        time.sleep(1)
if b12 = = '__main__':
    fonk2()