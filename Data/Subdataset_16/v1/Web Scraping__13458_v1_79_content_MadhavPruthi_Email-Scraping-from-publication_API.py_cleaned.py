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
def fonk1(b17):
    try:
        b3 = {"q": b17}
        b4 = "https:
        b5 = requests.get(b4)
        b6 = BeautifulSoup(b5.content, 'html.parser')
        b7 = b6.find_all(href=re.compile("https:
        if b7:
            b8 = re.search("(?P<b4>https?:
            if b8:
                return b8.group(0)[16:-2]
    except Exception as e:
        print(f"Error fetching DOI: {e}")
    return None
def fonk2(b17):
    try:
        b9 = f"python scholar.py -c 1 -A \"{b17}\""
        b10 = subprocess.check_output(b9, shell=True)
        if not b10:
            print("Result fetching Error! IP blocking!")
            return None
        b11 = b10.decode('windows-1252')
        b2.extend(re.findall(r'http:
        if b2:
            fonk3(b2[0])
    except Exception as e:
        print(f"Error fetching citations: {e}")
def fonk3(main_url):
    a1 = 0
    while True:
        try:
            b4 = f"{main_url}&start={a1}"
            b12 = requests.get(b4)
            b6 = BeautifulSoup(b12.content, 'html.parser')
            b13 = b6.find_all('h3', class_='gs_rt')
            if not b13:
                break
            for paper in b13:
                b14 = paper.get_text().split(' ', 1)[1] if paper.get_text().startswith('[') else paper.get_text()
                b15 = fonk1(b14)
                b16 = metainfoscrapper.getEmail(b15)
        except Exception as e:
            print(f"Error fetching citation details: {e}")
        a1 += 10
def fonk4(b15):
    try:
        b17 = b1.b19(b15)['b17']
        fonk2(b17)
    except Exception as e:
        print(f"Error in main search: {e}")
if b18 = = "__main__":
    b19 = "10.1038/nphys1170"
    fonk4(b19)