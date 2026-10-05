import requests
from bs4 import BeautifulSoup
import re
import random
import datetime
import logging
import sys
import time
logging.basicConfig(b1 = 'log.log',
                    b2 = 'w',
                    b3 = '%(asctime)s %(message)s',
                    b4 = logging.DEBUG)
logging.info('start')
b5 = [0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92,
          0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05,
          1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18,
          1.19, 1.2]
def fonk1(tag, class_name):
    b6 = b10.find_all(tag, class_=class_name)
    b7 = []
    for item in b6:
        b8 = item.find('a')
        if b8:
            b7.append(b8.get('href'))
    return b7
def fonk2(b19):
    b9 = requests.get(b19)
    b10 = BeautifulSoup(b9.text, 'html.parser')
    b11 = b10.find('form', class_='pagination')
    if b11:
        b12 = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
        b13 = b10.find('a', text=b12).text.strip()
        b14 = int(b12.match(b13).group(1))
        b15 = ['{}-{}.html'.b3(b19[:-5], p) for p in range(1, b14 + 1)]
        return b15
    return [b19]
def fonk3(b7):
    b16 = []
    for b19 in b7:
        b17 = random.choice(b5)
        time.sleep(b17)
        try:
            b9 = requests.get(b19)
            b10 = BeautifulSoup(b9.text, 'html.parser')
            b18 = b10.find_all('h3', class_='threadtitle')
            for thread in b18:
                b8 = thread.find('a')
                if b8:
                    b16.append(b8.get('href'))
        except Exception as e:
            logging.error('ERROR: skipped {} because of {}'.b3(b19, e))
    return b16
b19 = 'http:
b9 = requests.get(b19)
b10 = BeautifulSoup(b9.text, 'html.parser')
b20 = fonk1('h2', 'forumtitle')
b21 = fonk1('li', 'subforum')
with open('forumtitles.txt', 'w') as file:
    for title in b20:
        file.write(title + '\n')
with open('subforumtitles.txt', 'w') as file:
    for title in b21:
        file.write(title + '\n')
logging.info('printed {} b6 to list forumtitles'.b3(len(b20)))
logging.info('printed {} b6 to list subforumtitles'.b3(len(b21)))
b22 = b20 + b21
b23 = [fonk2(title) for title in b22]
b16 = [fonk3(b7) for b7 in b23]
b24 = [b19 for sublist in b16 for b19 in sublist]
with open('threadurls.txt', 'w') as file:
    for b19 in b24:
        file.write(b19 + '\n')
logging.info('printed {} b6 to list threadurls'.b3(len(b24)))
logging.info('end')