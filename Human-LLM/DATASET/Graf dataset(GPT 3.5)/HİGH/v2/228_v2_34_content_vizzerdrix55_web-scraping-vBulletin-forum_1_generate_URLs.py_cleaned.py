import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
logging.basicConfig(b1 = 'log.log',
                    b2 = 'w',
                    b3 = '%(asctime)s %(message)s',
                    b4 = logging.DEBUG)
logging.info('Starting the scraping process')
b5 = [0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92,
          0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05,
          1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18,
          1.19, 1.2]
def fonk1(b9, tag, class_name):
    b6 = b9.find_all(tag, class_=class_name)
    b7 = [item.find('a').get('href') for item in b6 if item.find('a')]
    return b7
def fonk2(b18):
    b8 = requests.get(b18)
    b9 = BeautifulSoup(b8.text, 'html.parser')
    b10 = b9.find('form', class_='pagination')
    if b10:
        b11 = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
        b12 = b9.find('a', text=b11).text.strip()
        b13 = int(b11.match(b12).group(1))
        b14 = ['{}-{}.html'.b3(b18[:-5], p) for p in range(1, b13 + 1)]
        return b14
    return [b18]
def fonk3(b7):
    b15 = []
    for b18 in b7:
        b16 = random.choice(b5)
        time.sleep(b16)
        try:
            b8 = requests.get(b18)
            b9 = BeautifulSoup(b8.text, 'html.parser')
            b17 = b9.find_all('h3', class_='threadtitle')
            b15.extend([thread.find('a').get('href') for thread in b17 if thread.find('a')])
        except Exception as e:
            logging.error(f'Error occurred while scraping {b18}: {e}')
    return b15
b18 = 'http:
b8 = requests.get(b18)
b9 = BeautifulSoup(b8.text, 'html.parser')
b19 = fonk1(b9, 'h2', 'forumtitle')
b20 = fonk1(b9, 'li', 'subforum')
with open('forumtitles.txt', 'w') as file:
    file.write('\n'.join(b19))
with open('subforumtitles.txt', 'w') as file:
    file.write('\n'.join(b20))
logging.info(f'Extracted {len(b19)} forum titles and {len(b20)} subforum titles')
b21 = b19 + b20
b22 = [fonk2(title) for title in b21]
b15 = [fonk3(b7) for b7 in b22]
b23 = [b18 for sublist in b15 for b18 in sublist]
with open('threadurls.txt', 'w') as file:
    file.write('\n'.join(b23))
logging.info(f'Extracted {len(b23)} thread URLs')
logging.info('Scraping process completed')