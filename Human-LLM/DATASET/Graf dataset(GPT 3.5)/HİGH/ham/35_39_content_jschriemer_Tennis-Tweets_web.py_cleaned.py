
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1(auth, api):
    b1 = 'http:
    b2 = urlopen(b1)
    b3 = BeautifulSoup(b2, 'html.parser')
    b4 = b3.findAll("div", class_="ind")
    b5 = b3.find("div", class_="sec row")
    b6 = b5.text
    b7 = len(re.findall(r'([A-Z]\w+-*\w*)', b6))
    b8 = re.findall(r'([A-Z]\w+-*\w*)', b6)
    b9 = ''
    a1 = 0
    while(a1 < b7):
        b9 = b9 + b8[a1]
        a1 = a1 + 1
    b10 = b3.findAll("div", class_="ind sub bold")
    b11 = ""
    for line in b10:
        if line.text != "FULL TOURNAMENT RESULTS":
            b11 = line.text
    b12 = []
    for line in b4:
        print(line)
        print(line.text.find("Final"))
        if (line.text.find("Final") >= 0):
            print("check!")
            print(line)
            b13 = line.text.split("Final")
            b12 = b12 + b13
    print(b12)
    fonk2(b12, auth, api, b9, b11)
def fonk2(b12, auth, api, b9, b11):
    a2 = 0
    for a1 in range(len(b12)):
        if b12[a1] != "":
            a2 = a2 + 1
    fonk3(b12, a2, auth, api, b9, b11)
def fonk3(b12, a2, auth, api, b9, b11):
    for a1 in range(len(b12)):
        if b12[a1] != "" and b12[a1] != "FULL TOURNAMENT RESULTS" and b12[a1] != "TENNIS HOME PAGE":
            b14 = re.sub(r'([a-z])(\d{1})', r'\1 \2', b12[a1])
            b15 = re.findall(r'([A-Z]\w+-*\w*)', b14)
            b16 = re.findall(r'^[^:]+', b11)
            if(len(b15)>1):
                print(b16[0] + " of the