import requests
from bs4 import BeautifulSoup
import pandas as pd
def fonk1(b4, b16, b17, b18):
    b1 = "+".join(b16.split())
    b2 = "+".join(b17.split())
    b3 = "24" + str(float(b18) / 1000)
    if b4 = = 'US':
        b5 = f"https:
    elif b4 = = 'CA':
        b5 = f"https:
    else:
        print("Invalid b4 option.")
        b5 = ''
    return b5
def fonk2(b12):
    return [a["title"] for a in b12.find_all(b6 = "a", b7={"data-tn-element": "jobTitle"})]
def fonk3(b12):
    return [span.text for span in b12.find_all("span", b7 = {"class": "b17"})]
def fonk4(b12):
    b8 = []
    for div in b12.find_all(b6 = "div", b7={"class": "row"}):
        try:
            b8.append(div.find("nobr").text)
        except AttributeError:
            try:
                b9 = div.find(b6="div", b7={"class": "sjcl"})
                b10 = b9.find("div")
                b8.append(b10.text.strip())
            except AttributeError:
                b8.append("Nothing found")
    return b8
def fonk5(b12):
    return [span.text.strip() for span in b12.find_all("span", b7 = {"class": "summary"})]
def fonk6(b5):
    if b5:
        b11 = requests.get(b5)
        b12 = BeautifulSoup(b11.text, "html.parser")
        b13 = fonk2(b12)
        b14 = fonk3(b12)
        b8 = fonk4(b12)
        for i, (b16, b17, b18) in enumerate(zip(b13, b14, b8)):
            print(f"{i:<10}{b16:<60}{b17:<70}{b18}")
def fonk7(base_url):
    return [base_url + "&b15 = " + str(x) for x in range(10, 40, 10)]
b4 = input("Which b4 are you looking to work in (CA/US)?: ")
b16 = input("Type of b16 you're looking for: ")
b17 = input("Desired b17: ")
b18 = input("Desired b18: ")
b5 = fonk1(b4, b16, b17, b18)
b19 = fonk7(b5)
print(f"{'':<10}{'Job Title':<60}{'Location':<70}{'Salary'}")
for page_number, page_url in enumerate(b19, b15 = 1):
    print(f"Page {page_number}")
    fonk6(page_url)