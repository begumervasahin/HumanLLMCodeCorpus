import re
import urllib.parse
import subprocess
from crossref.restful import Works
from bs4 import BeautifulSoup
import requests
from MainApp.models import EmailInfo
import scholar
import metainfoscrapper
b1 = Works()
def fonk1(b16):
    b2 = f"https:
    b3 = requests.get(b2)
    b4 = BeautifulSoup(b3.content, 'html.parser')
    b5 = b4.find_all(href=re.compile("https:
    if b5:
        b6 = re.search(r"https?:
        if b6:
            return b6.group(1)
    return None
def fonk2(b16):
    b7 = f'python scholar.py -c 1 -A "{b16}"'
    try:
        b8 = subprocess.check_output(b7, shell=True).decode('windows-1252')
    except subprocess.CalledProcessError:
        print("Result fetching Error! IP blocking!")
        return None
    b9 = [url for url in b8.split() if url.startswith('http:
    if not b9:
        return None
    b10 = b9[0]
    a1 = 0
    while True:
        b11 = re.sub(r'(\?.*)', f'?start={a1}&\\1', b10)
        b3 = requests.get(b11)
        b4 = BeautifulSoup(b3.content, 'html.parser')
        b12 = b4.find_all('h3', class_='gs_rt')
        if not b12:
            break
        for paper in b12:
            b13 = paper.get_text()
            if b13.startswith('['):
                b13 = b13.split(' ', 1)[1]
            b14 = fonk1(b13)
            if b14:
                b15 = metainfoscrapper.getEmail(b14)
        a1 += 10
def fonk3(b14):
    b16 = b1.b14(b14)['b16']
    return fonk2(b16)
