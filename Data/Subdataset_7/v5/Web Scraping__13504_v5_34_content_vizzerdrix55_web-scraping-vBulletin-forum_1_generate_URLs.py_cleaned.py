import requests
from bs4 import BeautifulSoup
import re
import random
import logging
import time
logging.basicConfig(b1 = 'log.log',
                    b2 = 'w',
                    b3 = '%(asctime)s %(message)s',
                    b4 = logging.DEBUG)
logging.info('Script started')
b5 = 'http:
b6 = (0.8, 1.2)
b7 = re.compile(r'Seite\s\d+\svon\s(\d+)', re.I)
def fonk1(soup, tag, class_name):
    b8 = []
    b9 = soup.find_all(tag, class_=class_name)
    for element in b9:
        b10 = element.find('a')
        if b10:
            b8.append(b10.get('href'))
    return b8
def fonk2(url):
    try:
        b11 = requests.get(url)
        b11.raise_for_status()
        return BeautifulSoup(b11.text, 'html.parser')
    except Exception as e:
        logging.error(f'ERROR: Failed to fetch {url} because of {e}')
        return None
def fonk3():
    b12 = random.uniform(*b6)
    time.sleep(b12)
def fonk4(urls):
    b13 = []
    for url in urls:
        fonk3()
        b14 = fonk2(url)
        if b14:
            b15 = b14.find('form', class_='pagination')
            if b15:
                b16 = int(b7.match(b15.text).group(1))
                b13.extend([f'{url}/index{page}.html' for page in range(1, b16 + 1)])
            else:
                b13.append(url)
    return b13
b17 = fonk2(b5)
if b17:
    b18 = fonk1(b17, 'h2', 'forumtitle')
    b19 = fonk1(b17, 'li', 'subforum')
    with open('forumtitles.txt', 'w') as file:
        file.write('\n'.join(b18))
    with open('subforumtitles.txt', 'w') as file:
        file.write('\n'.join(b19))
    b20 = fonk4(b18)
    b21 = fonk4(b19)
    with open('forumtitles_new.txt', 'w') as file:
        file.write('\n'.join(b20))
    with open('subforumtitles_new.txt', 'w') as file:
        file.write('\n'.join(b21))
    b22 = b20 + b21
    with open('all_forumtitles_new.txt', 'w') as file:
        file.write('\n'.join(b22))
    b23 = fonk4(b22)
    with open('threadurls.txt', 'w') as file:
        file.write('\n'.join(b23))
    b24 = fonk4(b23)
    with open('threadurls_new.txt', 'w') as file:
        file.write('\n'.join(b24))
logging.info('Script ended')