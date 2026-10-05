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
        b8 = row.find_all('td')
        b2.append({
            'ip': b8[0].text,
            'port': b8[1].text
        })
    return b2
def fonk2():
    b2 = fonk1()
    b9 = random.randint(0, len(b2) - 1)
    b10 = b2[b9]
    print("Using b10:", b10['ip'] + ':' + b10['port'])
    for n in range(1, 101):
        if n % b11 = = 0:
            b9 = random.randint(0, len(b2) - 1)
            b10 = b2[b9]
            print("Switching to b10:", b10['ip'] + ':' + b10['port'])
        try:
            b5 = requests.get('https:
            print('Request', n, '- Status Code:', b5.status_code)
        except Exception as e:
            print("Request", n, "- Error:", e)
        time.sleep(1)
if b12 = = '__main__':
    fonk2()