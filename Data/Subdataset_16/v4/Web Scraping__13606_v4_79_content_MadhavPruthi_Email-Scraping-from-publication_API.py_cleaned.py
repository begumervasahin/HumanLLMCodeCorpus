import re
import urllib.parse
import subprocess
from crossref.restful import Works
from bs4 import BeautifulSoup
import requests
from MainApp.models import EmailInfo
import scholar
import metainfoscrapper
b1 = []
b2 = Works()
def fonk1(b19):
    b3 = {"q": b19}
    b4 = f"https:
    b5 = requests.get(b4)
    b6 = BeautifulSoup(b5.content, 'html.parser')
    b7 = b6.find_all(href=re.compile("https:
    if b7:
        b8 = re.search(r"https?:
        if b8:
            return b8.group(1)
    return None
def fonk2(b19):
    b9 = f"python scholar.py -c 1 -A \"{b19}\""
    try:
        b10 = subprocess.check_output(b9, shell=True).decode('windows-1252')
    except subprocess.CalledProcessError:
        print("Result fetching Error! IP blocking!")
        return None
    b1 = [b4 for b4 in b10.split() if b4.startswith('http:
    if not b1:
        return None
    b11 = b1[0]
    a1 = 0
    while True:
        b12 = b11.split('?')
        b12.insert(1, f"?b13 = {a1}&")
        b14 = ''.join(b12)
        b5 = requests.get(b14)
        b6 = BeautifulSoup(b5.content, 'html.parser')
        b15 = b6.find_all('h3', class_='gs_rt')
        if not b15:
            break
        for paper in b15:
            b16 = paper.get_text()
            if b16.startswith('['):
                b16 = b16.split(' ', 1)[1]
            b17 = fonk1(b16)
            if b17:
                b18 = metainfoscrapper.getEmail(b17)
        a1 += 10
def fonk3(b17):
    b19 = b2.b17(b17)['b19']
    return fonk2(b19)
