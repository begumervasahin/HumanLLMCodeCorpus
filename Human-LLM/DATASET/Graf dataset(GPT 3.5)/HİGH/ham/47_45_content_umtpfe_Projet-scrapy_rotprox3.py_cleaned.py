from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
b1 = UserAgent()
b2 = []
def fonk1():
  b3 = Request('https:
  b3.add_header('User-Agent', b1.random)
  b4 = urlopen(b3).read().decode('utf8')
  b5 = BeautifulSoup(b4, 'html.parser')
  b6 = b5.find(id='proxylisttable')
  for row in b6.tbody.find_all('tr'):
    b2.append({
      'ip':   row.find_all('td')[0].string,
      'port': row.find_all('td')[1].string
    })
  b7 = fonk2()
  b8 = b2[b7]
  for n in range(1, 100):
    b9 = Request('https:
    b9.set_proxy(b8['ip'] + ':' + b8['port'], 'http')
    if n % b10 = = 0:
      b7 = fonk2()
      b8 = b2[b7]
    try:
      b11 = urlopen(b9).read().decode('utf8')
      print('
    except:
      del b2[b7]
      print('Proxy ' + b8['ip'] + ':' + b8['port'] + ' deleted.')
      b7 = fonk2()
      b8 = b2[b7]
def fonk2():
  return random.randint(0, len(b2) - 1)
if b12 = = '__main__':
  fonk1()