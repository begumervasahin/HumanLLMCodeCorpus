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
logging.info('Script started')
b5 = [i/100 for i in range(80, 121)]
b6 = 'http:
b7 = requests.get(b6)
b8 = BeautifulSoup(b7.text, 'html.parser')
b9 = b8.find_all('h2', class_='forumtitle')
b10 = []
if b9:
    for item in b9:
        b11 = item.find('a')
        if b11:
            b10.append(b11.get('href'))
else:
    logging.error('Unexpected HTML structure for forum titles')
with open('b10.txt', 'w') as file:
    for title in b10:
        file.write(title + '\n')
logging.info(f'Printed {len(b10)} forum titles to b10.txt')
b12 = b8.find_all('li', class_='subforum')
b13 = []
if b12:
    for item in b12:
        b14 = item.find('a')
        if b14:
            b13.append(b14.get('href'))
else:
    logging.error('Unexpected HTML structure for subforum titles')
with open('b13.txt', 'w') as file:
    for title in b13:
        file.write(title + '\n')
logging.info(f'Printed {len(b13)} subforum titles to b13.txt')
b15 = []
for item in b10:
    b16 = random.choice(b5)
    time.sleep(b16)
    try:
        b7 = requests.get(item)
        b8 = BeautifulSoup(b7.text, 'html.parser')
        b17 = b8.find('form', class_='pagination')
        if b17 is not None:
            b18 = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
            b19 = b8.find('a', text=b18).text.strip()
            b19 = int(b18.match(b19).group(1))
            b20 = [f'{item}/index{p}.html' for p in range(1, b19 + 1)]
            b15.extend(b20)
        else:
            b15.append(item)
    except Exception as e:
        logging.error(f'ERROR: Skipped {item} because of {e}')
with open('b15.txt', 'w') as file:
    for title in b15:
        file.write(title + '\n')
logging.info(f'Printed {len(b15)} updated forum titles to b15.txt')
b21 = []
for item in b13:
    b16 = random.choice(b5)
    time.sleep(b16)
    try:
        b7 = requests.get(item)
        b8 = BeautifulSoup(b7.text, 'html.parser')
        b17 = b8.find('form', class_='pagination')
        if b17 is not None:
            b18 = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
            b19 = b8.find('a', text=b18).text.strip()
            b19 = int(b18.match(b19).group(1))
            b20 = [f'{item}/index{p}.html' for p in range(1, b19 + 1)]
            b21.extend(b20)
        else:
            b21.append(item)
    except Exception as e:
        logging.error(f'ERROR: Skipped {item} because of {e}')
with open('b21.txt', 'w') as file:
    for title in b21:
        file.write(title + '\n')
logging.info(f'Printed {len(b21)} updated subforum titles to b21.txt')
b22 = b21 + b15
with open('b22.txt', 'w') as file:
    for title in b22:
        file.write(title + '\n')
logging.info(f'Printed {len(b22)} combined updated titles to b22.txt')
b23 = []
for item in b22:
    b16 = random.choice(b5)
    time.sleep(b16)
    try:
        b7 = requests.get(item)
        b8 = BeautifulSoup(b7.text, 'html.parser')
        b24 = b8.find_all('h3', class_='threadtitle')
        for thread in b24:
            b25 = thread.find('a')
            if b25:
                b23.append(b25.get('href'))
    except Exception as e:
        logging.error(f'ERROR: Skipped {item} because of {e}')
with open('b23.txt', 'w') as file:
    for b6 in b23:
        file.write(b6 + '\n')
logging.info(f'Printed {len(b23)} thread URLs to b23.txt')
b26 = []
for item in b23:
    b16 = random.choice(b5)
    time.sleep(b16)
    try:
        b7 = requests.get(item)
        b8 = BeautifulSoup(b7.text, 'html.parser')
        b17 = b8.find('form', class_='pagination')
        if b17 is not None:
            b18 = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
            b19 = b8.find('a', text=b18).text.strip()
            b19 = int(b18.match(b19).group(1))
            b20 = [f'{item[:-5]}-{p}.html' for p in range(1, b19 + 1)]
            b26.extend(b20)
        else:
            b26.append(item)
    except Exception as e:
        logging.error(f'ERROR: Skipped {item} because of {e}')
with open('b26.txt', 'w') as file:
    for b6 in b26:
        file.write(b6 + '\n')
logging.info(f'Printed {len(b26)} updated thread URLs to b26.txt')
logging.info('Script ended')