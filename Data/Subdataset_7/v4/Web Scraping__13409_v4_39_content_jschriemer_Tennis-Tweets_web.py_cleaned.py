import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1(auth, api):
    b1 = 'http:
    b2 = urlopen(b1)
    b3 = BeautifulSoup(b2, 'html.parser')
    b4 = b3.find("div", class_="sec row").text
    b5 = re.findall(r'([A-Z]\w+-*\w*)', b4)
    b6 = b3.findAll("div", class_="ind sub bold")
    b7 = ""
    for line in b6:
        if line.text != "FULL TOURNAMENT RESULTS":
            b7 = line.text
    b8 = b3.findAll("div", class_="ind")
    b9 = []
    for line in b8:
        if line.text.find("Final") >= 0:
            b10 = line.text.split("Final")
            b9.extend(b10)
    fonk2(b9, auth, api, b5, b7)
def fonk2(b9, auth, api, b5, b7):
    b11 = sum(1 for match in b9 if match)
    fonk3(b9, b11, auth, api, b5, b7)
def fonk3(b9, b11, auth, api, b5, b7):
    for match in b9:
        if match and match != "FULL TOURNAMENT RESULTS" and match != "TENNIS HOME PAGE":
            b12 = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            b13 = re.findall(r'([A-Z]\w+-*\w*)', b12)
            b14 = re.findall(r'^[^:]+', b7)
            if len(b13) > 1:
                print(b14[0] + " of the...")