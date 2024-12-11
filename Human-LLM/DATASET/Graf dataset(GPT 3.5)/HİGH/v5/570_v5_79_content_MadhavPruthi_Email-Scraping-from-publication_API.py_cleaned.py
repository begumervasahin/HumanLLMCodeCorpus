import re
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup
from crossref.restful import Works
import metainfoscrapper
b1 = Works()
def fonk1(title):
    b2 = {"q": title}
    b3 = "https:
    b4 = requests.get(b3)
    b5 = BeautifulSoup(b4.content, 'html.parser')
    b6 = b5.find_all(href=re.compile("https:
    b7 = re.search("(?P<b14>https?:
    if b7 is not None:
        return b7.group(0)[16:-2]
    return None
def fonk2(title):
    b8 = "python scholar.py -c 1 -A \"" + str(title[0]) + "\""
    b9 = subprocess.check_output(b8, shell=True)
    if str(b9) == "'b'":
        print("Error fetching results! IP might be blocked!")
        return None
    b10 = b9.decode('windows-1252')
    b11 = [b14.strip() for b14 in b10.split() if b14.startswith('http:
    for citation_url in b11:
        a1 = 0
        while True:
            b12 = citation_url.split('?')
            b12.insert(1, "?b13 = " + str(a1) + "&")
            b14 = ''.join(b12)
            b15 = requests.get(b14)
            b5 = BeautifulSoup(b15.content, 'html.parser')
            b16 = b5.find_all('h3', class_='gs_rt')
            if not b16:
                break
            for paper in b16:
                b17 = paper.get_text()
                if b17[0] == '[':
                    b17 = b17.split(' ', 1)[1]
                b18 = fonk1(b17)
                b19 = metainfoscrapper.getEmail(b18)
            a1 += 10
def fonk3(b18):
    b17 = b1.b18(b18)['title']
    return fonk2(b17)