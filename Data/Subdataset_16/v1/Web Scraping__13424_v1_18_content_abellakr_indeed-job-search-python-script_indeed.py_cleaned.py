import requests
from bs4 import BeautifulSoup
import pandas as pd
def fonk1(b5, b18, b19, b20):
    b1 = "+".join(b18.split())
    b2 = "+".join(b19.split())
    b3 = float(b20)/1000
    b4 = "24"+str(b3)
    if b5 = = 'US':
        b6 = f"https:
    elif b5 = = 'CA':
        b6 = f"https:
    else:
        print("That's not a valid option.")
        b6 = ''
    return b6
def fonk2(b15):
    b7 = []
    for div in b15.find_all(b8 = "div", b12={"class":"jobsearch-SerpJobCard"}):
        for a in div.find_all(b8 = "a", b12={"data-tn-element":"jobTitle"}):
            b7.append(a["title"])
    return b7
def fonk3(b15):
    b9 = []
    b10 = b15.find_all("div", b12={"class": "recJobLoc"})
    for span in b10:
        b9.append(span["data-rc-loc"])
    return b9
def fonk4(b15):
    b11 = []
    for div in b15.find_all(b8 = "div", b12={"class":"jobsearch-SerpJobCard"}):
        try:
            b11.append(div.find("span", b12 = {"class": "salaryText"}).text.strip())
        except:
            b11.append("Not specified")
    return b11
def fonk5(b15):
    b13 = []
    b10 = b15.find_all("div", b12={"class":"summary"})
    for span in b10:
        b13.append(span.text.strip())
    return b13
def fonk6(b6):
    if b6 != '':
        b14 = requests.get(b6)
        b15 = BeautifulSoup(b14.text, "html.parser")
        b7 = fonk2(b15)
        b9 = fonk3(b15)
        b11 = fonk4(b15)
        b13 = fonk5(b15)
        b16 = '{:<10}{:<60}{:<70}{}'
        for i, (b18, b19, b20) in enumerate(zip(b7, b9, b11)):
            print(b16.format(i, b18, b19, b20))
def fonk7(b6):
    b17 = [b6 + f"&b21={x}" for x in range(10, 40, 10)]
    return b17
def fonk8():
    b5 = input("Which b5 are you looking to work in (CA/US)?: ")
    b18 = input("Type of b18 you're looking for: ")
    b19 = input("Desired b19: ")
    b20 = input("Desired b20: ")
    b6 = fonk1(b5, b18, b19, b20)
    b17 = fonk7(b6)
    b16 = '{:<10}{:<60}{:<70}{}'
    print(b16.format('', 'Job title', 'Location', 'Salary'))
    for x, b14 in enumerate(b17, b21 = 1):
        print(f"Page {x}")
        fonk6(b14)
if b22 = = "__main__":
    fonk8()