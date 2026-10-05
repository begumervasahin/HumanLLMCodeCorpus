import re
import urllib.parse
from crossref.restful import Works
import subprocess
from bs4 import BeautifulSoup
import requests
from MainApp.models import EmailInfo
import scholar
import metainfoscrapper
b1 = []
b2 = Works()
"""
def fonk1():
    b3 = scholar.ScholarQuerier()
    b4 = scholar.ScholarSettings()
    b3.apply_settings(b4)
    b5 = scholar.SearchScholarQuery()
    b5.set_author("albert einstein")
    b5.set_num_page_results(1)
    b3.send_query(b5)
    print(b3.articles)
"""
def fonk2(title):
    b6 = {"q": title}
    b7 = "https:
    b8 = requests.get(b7)
    b9 = BeautifulSoup(b8.content, 'html.parser')
    b10 = b9.find_all(href=re.compile("https:
    b11 = re.search("(?P<b7>https?:
    if b11 is not None:
        return b11.groups(0)[0][16:-2]
    return None
def fonk3(title):
    b12 = "python scholar.py -c 1 -A " +  "\"" + str(title[0]) + "\""
    b13 = subprocess.check_output(b12, shell=True)
    if str(b13) == "'b'":
        print("Result fetching Error! IP blocking!")
        return None
    b14 = b13.decode('windows-1252')
    b15 = b14.split(" ")
    for b16 in b15:
        if b16.startswith('http:
            b16 = b16.strip()
            b1.append(b16)
    b17 = b1[0]
    a1 = 0
    while True:
        b7 = b17.split('?')
        b7.insert(1, "?b18 = " + str(a1) + "&")
        b7 = ''.join(b7)
        b19 = requests.get(b7)
        b9 = BeautifulSoup(b19.content, 'html.parser')
        b20 = b9.find_all('h3', class_='gs_rt')
        if not b20:
            break
        for paper in b20:
            b21 = paper.get_text()
            if b21[0] == '[':
                b21 = b21.split(' ', 1)[1]
            b22 = fonk2(b21)
            b23 = metainfoscrapper.getEmail(b22)
        a1 += 10
def fonk4(b22):
    return fonk3(b2.doi(b22)['title'])