import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1():
    b1 = 'http:
    b2 = urlopen(b1)
    b3 = BeautifulSoup(b2, 'html.parser')
    b4 = b3.find("div", class_="sec row")
    b5 = ''.join(re.findall(r'([A-Z]\w+-*\w*)', b4.text))
    b6 = b3.findAll("div", class_="ind sub bold")
    b7 = next((line.text for line in b6 if line.text != "FULL TOURNAMENT RESULTS"), "")
    b8 = b3.findAll("div", class_="ind")
    b9 = [line.text.split("Final")[0] for line in b8 if "Final" in line.text]
    fonk2(b9, b5, b7)
def fonk2(b9, b5, b7):
    b10 = sum(1 for match in b9 if match)
    fonk3(b9, b10, b5, b7)
def fonk3(b9, b10, b5, b7):
    for match in b9:
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            b11 = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            b12 = re.findall(r'([A-Z]\w+-*\w*)', b11)
            b13 = re.findall(r'^[^:]+', b7)
            if len(b12) > 1:
                print(f"{b13[0]} of the {b5}: {b12[0]} vs {b12[1]}")
                print(f"Score: {b11}")
fonk1()