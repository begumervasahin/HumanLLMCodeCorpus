import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
def fonk1(b5, b20, b21, b22):
    b1 = "+".join(b20.split())
    b2 = "+".join(b21.split())
    b3 = float(b22)/1000
    b4 = "24"+str(b3)
    if b5 = = 'US':
        b6 = "https:
    elif b5 = = 'CA':
        b6 = "https:
    else:
        print("thats not a valid option.")
        b6 = ''
    return(b6)
def fonk2(b16):
    b7 = []
    for div in b16.find_all(b8 = "div",attrs={"class":"row"}):
        for a in div.find_all(b8 = "a",attrs={"data-tn-element":"jobTitle"}):
            b7.append(a["title"])
    return(b7)
def fonk3(b16):
    b9 = []
    b10 = b16.find_all("span", attrs={"class": "b21"})
    for span in b10:
        b9.append(span.text)
    return(b9)
def fonk4(b16):
    b11 = []
    for div in b16.find_all(b8 = "div", attrs={"class":"row"}):
        try:
            b11.append(div.find("nobr").text)
        except:
            try:
                b12 = div.find(b8="div", attrs={"class":"sjcl"})
                b13 = b12.find("div")
                b11.append(b13.strip())
            except:
                b11.append("Nothing found")
    return(b11)
def fonk5(b16):
    b14 = []
    b10 = b16.find_all("span", attrs={"class":"summary"})
    for span in b10:
        b14.append(span.text.strip())
    return(b14)
def fonk6(b6):
    if b6 != '':
        b15 = requests.get(b6)
        b16 = BeautifulSoup(b15.text, "html.parser")
        b7 = fonk2(b16)
        b9 = fonk3(b16)
        b11 = fonk4(b16)
        b17 = '%-10s%-60s%-70s%s'
        for i, (b20, b21, b22) in enumerate(zip(b7, b9, b11)):
            print(b17 % (i, b20, b21, b22))
def fonk7(b6):
    b18 = []
    for a1 in range(10, 40, 10):
        b18.append(b6+"&b19 = "+str(a1))
    return b18
b5 = input("which b5 are looking to work in (CA/US)?: ")
b20 = input("type of b20 you're looking for: ")
b21 = input("desired b21: ")
b22 = input("desired b22: ")
b6 = fonk1(b5, b20, b21, b22)
b18 = fonk7(b6)
a1 = 1
b17 = '%-10s%-60s%-70s%s'
print(b17 % ('', 'Job title', 'Location', 'b22'))
for b15 in b18:
    print("Page "+str(a1))
    fonk6(b15)
    a1 = a1 + 1