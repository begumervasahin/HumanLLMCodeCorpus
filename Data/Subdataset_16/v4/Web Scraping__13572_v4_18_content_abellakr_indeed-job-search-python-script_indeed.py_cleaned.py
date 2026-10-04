import requests
from bs4 import BeautifulSoup
import pandas as pd
def fonk1(b5, b18, b19, b20):
    b1 = "+".join(b18.split())
    b2 = "+".join(b19.split())
    b3 = float(b20) / 1000
    b4 = "24" + str(b3)
    if b5 = = 'US':
        b6 = f"https:
    elif b5 = = 'CA':
        b6 = f"https:
    else:
        print("Invalid b5 option.")
        b6 = ''
    return b6
def fonk2(b15):
    b7 = []
    for div in b15.find_all(b8 = "div", attrs={"class": "row"}):
        for a in div.find_all(b8 = "a", attrs={"data-tn-element": "jobTitle"}):
            b7.append(a["title"])
    return b7
def fonk3(b15):
    b9 = [span.text for span in b15.find_all("span", attrs={"class": "b19"})]
    return b9
def fonk4(b15):
    b10 = []
    for div in b15.find_all(b8 = "div", attrs={"class": "row"}):
        try:
            b10.append(div.find("nobr").text)
        except:
            try:
                b11 = div.find(b8="div", attrs={"class": "sjcl"})
                b12 = b11.find("div")
                b10.append(b12.strip())
            except:
                b10.append("Nothing found")
    return b10
def fonk5(b15):
    b13 = [span.text.strip() for span in b15.find_all("span", attrs={"class": "summary"})]
    return b13
def fonk6(b6):
    if b6:
        b14 = requests.get(b6)
        b15 = BeautifulSoup(b14.text, "html.parser")
        b7 = fonk2(b15)
        b9 = fonk3(b15)
        b10 = fonk4(b15)
        b16 = '%-10s%-60s%-70s%s'
        for i, (b18, b19, b20) in enumerate(zip(b7, b9, b10)):
            print(b16 % (i, b18, b19, b20))
def fonk7(b6):
    return [b6 + "&b17 = " + str(a1) for a1 in range(10, 40, 10)]
b5 = input("Which b5 are you looking to work in (CA/US)?: ")
b18 = input("Type of b18 you're looking for: ")
b19 = input("Desired b19: ")
b20 = input("Desired b20: ")
b6 = fonk1(b5, b18, b19, b20)
b21 = fonk7(b6)
a1 = 1
b16 = '%-10s%-60s%-70s%s'
print(b16 % ('', 'Job Title', 'Location', 'Salary'))
for b14 in b21:
    print("Page " + str(a1))
    fonk6(b14)
    a1 += 1