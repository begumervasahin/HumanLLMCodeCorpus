import re
import urllib.parse
import subprocess
from bs4 import BeautifulSoup
import requests
from crossref.restful import Works
import metainfoscrapper
b1 = []
b2 = Works()
def fonk1(title):
    b3 = {"q": title}
    b4 = "https:
    b5 = requests.get(b4)
    b6 = BeautifulSoup(b5.content, 'html.parser')
    b7 = b6.find_all(href=re.compile("https:
    b8 = re.search("(?P<b4>https?:
    if b8 is not None:
        return b8.group(0)[16:-1]
    return None
def fonk2(title):
    b9 = f"python scholar.py -c 1 -A \"{title}\""
    b10 = subprocess.check_output(b9, shell=True)
    if str(b10) == "'b'":
        print("Result fetching Error! IP blocking!")
        return None
    b11 = b10.decode('windows-1252')
    b12 = b11.split(" ")
    for b13 in b12:
        if b13.startswith('http:
            b13 = b13.strip()
            b1.append(b13)
    b14 = b1[0]
    a1 = 0
    while True:
        b4 = b14.split('?')
        b4.insert(1, "?b15 = " + str(a1) + "&")
        b4 = ''.join(b4)
        b16 = requests.get(b4)
        b6 = BeautifulSoup(b16.content, 'html.parser')
        b17 = b6.find_all('h3', class_='gs_rt')
        if not b17:
            break
        for paper in b17:
            b18 = paper.get_text()
            if b18[0] == '[':
                b18 = b18.split(' ', 1)[1]
            b19 = fonk1(b18)
            b20 = metainfoscrapper.getEmail(b19)
        a1 += 10
def fonk3(b19):
    return fonk2(b2.doi(b19)['title'])
