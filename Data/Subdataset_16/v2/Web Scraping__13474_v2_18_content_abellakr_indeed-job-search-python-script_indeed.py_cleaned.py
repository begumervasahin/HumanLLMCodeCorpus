import requests
from bs4 import BeautifulSoup
import pandas as pd
def fonk1(b4, b17, b18, b19):
    b1 = "+".join(b17.split())
    b2 = "+".join(b18.split())
    b3 = "24" + str(int(b19)
    if b4 = = 'US':
        b5 = f"https:
    elif b4 = = 'CA':
        b5 = f"https:
    else:
        print("That's not a valid option.")
        b5 = ''
    return b5
def fonk2(b13):
    b6 = []
    for div in b13.find_all(b7 = "div", b10={"class":"jobsearch-SerpJobCard"}):
        for a in div.find_all(b7 = "a", b10={"data-tn-element":"jobTitle"}):
            b6.append(a["title"])
    return b6
def fonk3(b13):
    b8 = []
    for div in b13.find_all(b7 = "div", b10={"class":"recJobLoc"}):
        b8.append(div["data-rc-loc"])
    return b8
def fonk4(b13):
    b9 = []
    for div in b13.find_all(b7 = "div", b10={"class":"jobsearch-SerpJobCard"}):
        try:
            b9.append(div.find("span", b10 = {"class": "salaryText"}).text.strip())
        except AttributeError:
            b9.append("Not specified")
    return b9
def fonk5(b13):
    b11 = []
    for div in b13.find_all(b7 = "div", b10={"class":"summary"}):
        b11.append(div.text.strip())
    return b11
def fonk6(b5):
    if b5:
        b12 = requests.get(b5)
        b13 = BeautifulSoup(b12.text, "html.parser")
        b14 = fonk2(b13)
        b8 = fonk3(b13)
        b9 = fonk4(b13)
        b15 = '{:<10}{:<60}{:<70}{}'
        for i, (b17, b18, b19) in enumerate(zip(b14, b8, b9)):
            print(b15.format(i, b17, b18, b19))
def fonk7(b5):
    return [b5 + f"&b16 = {x}" for x in range(10, 40, 10)]
def fonk8():
    b4 = input("Which b4 are you looking to work in (CA/US)?: ")
    b17 = input("Type of b17 you're looking for: ")
    b18 = input("Desired b18: ")
    b19 = input("Desired b19: ")
    b5 = fonk1(b4, b17, b18, b19)
    b20 = fonk7(b5)
    b15 = '{:<10}{:<60}{:<70}{}'
    print(b15.format('', 'Job Title', 'Location', 'Salary'))
    for page_number, page_url in enumerate(b20, b16 = 1):
        print(f"Page {page_number}")
        fonk6(page_url)
if b21 = = "__main__":
    fonk8()