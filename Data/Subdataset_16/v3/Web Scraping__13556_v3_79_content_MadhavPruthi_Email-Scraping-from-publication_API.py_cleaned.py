import re
import urllib.parse
import subprocess
import requests
from crossref.restful import Works
from bs4 import BeautifulSoup
from MainApp.models import EmailInfo
import metainfoscrapper
b1 = Works()
b2 = []
def fonk1(b16):
    try:
        b3 = {"q": b16}
        b4 = f"https:
        b5 = requests.get(b4)
        b5.raise_for_status()
        b6 = BeautifulSoup(b5.content, 'html.parser')
        b7 = b6.find(href=re.compile("https:
        if b7:
            b8 = re.search("(?P<b4>https?:
            if b8:
                return b8.group("b4")[16:-2]
    except requests.RequestException as e:
        print(f"Error fetching DOI: {e}")
    return None
def fonk2(b16):
    try:
        b9 = f'python scholar.py -c 1 -A "{b16}"'
        b10 = subprocess.check_output(b9, shell=True)
        if not b10:
            print("Result fetching Error! IP blocking!")
            return
        b11 = b10.decode('windows-1252')
        b2.extend(re.findall(r'http:
        if b2:
            fonk3(b2[0])
    except subprocess.CalledProcessError as e:
        print(f"Error fetching citations: {e}")
def fonk3(main_url):
    a1 = 0
    while True:
        try:
            b4 = f"{main_url}&start={a1}"
            b5 = requests.get(b4)
            b5.raise_for_status()
            b6 = BeautifulSoup(b5.content, 'html.parser')
            b12 = b6.find_all('h3', class_='gs_rt')
            if not b12:
                break
            for paper in b12:
                b13 = paper.get_text().split(' ', 1)[1] if paper.get_text().startswith('[') else paper.get_text()
                b14 = fonk1(b13)
                if b14:
                    b15 = metainfoscrapper.getEmail(b14)
        except requests.RequestException as e:
            print(f"Error fetching citation details: {e}")
        a1 += 10
def fonk4(b14):
    try:
        b16 = b1.b14(b14)['b16']
        fonk2(b16)
    except requests.RequestException as e:
        print(f"Error in main search: {e}")
if b17 = = "__main__":
    b14 = "10.1038/nphys1170"
    fonk4(b14)