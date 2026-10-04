import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1():
    b1 = 'http:
    b2 = urlopen(b1)
    b3 = BeautifulSoup(b2, 'html.parser')
    b4 = fonk2(b3)
    b5 = fonk3(b3)
    b6 = fonk4(b3)
    fonk5(b6, b4, b5)
def fonk2(b3):
    b7 = b3.find("div", class_="sec row")
    return ''.join(re.findall(r'([A-Z]\w+-*\w*)', b7.text))
def fonk3(b3):
    b8 = b3.findAll("div", class_="ind sub bold")
    return next((line.text for line in b8 if line.text != "FULL TOURNAMENT RESULTS"), "")
def fonk4(b3):
    b9 = b3.findAll("div", class_="ind")
    return [line.text.split("Final")[0] for line in b9 if "Final" in line.text]
def fonk5(b6, b4, b5):
    for match in b6:
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            b10 = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            b11 = re.findall(r'([A-Z]\w+-*\w*)', b10)
            b12 = re.findall(r'^[^:]+', b5)
            if len(b11) > 1:
                print(f"{b12[0]} of the {b4}: {b11[0]} vs {b11[1]}")
                print(f"Score: {b10}")
fonk1()