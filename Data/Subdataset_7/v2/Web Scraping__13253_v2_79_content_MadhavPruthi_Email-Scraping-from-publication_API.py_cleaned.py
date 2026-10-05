import re
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup
from crossref.restful import Works
import metainfoscrapper
b1 = []
b2 = Works()
def fonk1(b21):
    b3 = {"q": b21}
    b4 = "https:
    b5 = requests.get(b4)
    b6 = BeautifulSoup(b5.content, 'html.parser')
    b7 = b6.find_all(href=re.compile("https:
    if b7:
        b8 = re.search("(?P<b15>https?:
        if b8:
            return b8.group(0)[16:-1]
    return None
def fonk2(b21):
    b9 = f"python scholar.py -c 1 -A \"{b21}\""
    try:
        b10 = subprocess.check_output(b9, shell=True)
    except subprocess.CalledProcessError:
        print("Error occurred while fetching results! IP might be blocked.")
        return None
    b1.clear()
    b11 = b10.decode('windows-1252')
    b12 = b11.split(" ")
    for string in b12:
        if string.startswith('http:
            b1.append(string.strip())
    b13 = b1[0] if b1 else None
    a1 = 0
    while b13:
        b14 = b13.split('?')
        b15 = f"{b14[0]}?start={a1}&{b14[1]}"
        b16 = requests.get(b15)
        b6 = BeautifulSoup(b16.content, 'html.parser')
        b17 = b6.find_all('h3', class_='gs_rt')
        if not b17:
            break
        for paper in b17:
            b18 = paper.get_text().split(' ', 1)[1] if paper.get_text()[0] == '[' else paper.get_text()
            b19 = fonk1(b18)
            if b19:
                b20 = metainfoscrapper.getEmail(b19)
        a1 += 10
def fonk3(doi):
    b21 = b2.doi(doi)['b21']
    fonk2(b21)
