import re
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup
from crossref.restful import Works
from MainApp.models import EmailInfo
import scholar
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
        return b8.group(0)[16:-2]
    return None
def fonk2(title):
    b9 = "python scholar.py -c 1 -A " +  "\"" + str(title[0]) + "\""
    b10 = subprocess.check_output(b9, shell=True)
    if str(b10) == "'b'":
        print("Error fetching results! IP might be blocked!")
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
        b15 = b14.split('?')
        b15.insert(1, "?b16 = " + str(a1) + "&")
        b4 = ''.join(b15)
        b17 = requests.get(b4)
        b6 = BeautifulSoup(b17.content, 'html.parser')
        b18 = b6.find_all('h3', class_='gs_rt')
        if not b18:
            break
        for paper in b18:
            b19 = paper.get_text()
            if b19[0] == '[':
                b19 = b19.split(' ', 1)[1]
            b20 = fonk1(b19)
            b21 = metainfoscrapper.getEmail(b20)
        a1 += 10
def fonk3(b20):
    return fonk2(b2.b20(b20)['title'])