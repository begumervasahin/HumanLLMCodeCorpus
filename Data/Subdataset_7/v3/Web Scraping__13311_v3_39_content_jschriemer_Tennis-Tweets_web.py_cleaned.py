import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1(url):
    with urlopen(url) as response:
        b1 = BeautifulSoup(response, 'html.parser')
    b2 = b1.find_all("div", class_="ind")
    b3 = b1.find("div", class_="sec row")
    b4 = fonk2(b3)
    b5 = fonk3(b1)
    b6 = fonk4(b2)
    fonk5(b6, b4, b5)
def fonk2(b3):
    b7 = b3.text
    return ' '.join(re.findall(r'([A-Z]\w+-*\w*)', b7))
def fonk3(b1):
    b8 = b1.find_all("div", class_="ind sub bold")
    for section in b8:
        if section.text != "FULL TOURNAMENT RESULTS":
            return section.text
def fonk4(b2):
    b6 = []
    for section in b2:
        if "Final" in section.text:
            b9 = section.text.split("Final")
            b6.extend(b9)
    return b6
def fonk5(b6, b4, b5):
    print(f"Tournament Round: {b5} of the Tournament: {b4}")
    for b10 in b6:
        b10 = b10.strip()
        if b10 and b10 not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            fonk6(b10)
def fonk6(b10):
    b11 = re.sub(r'([a-z])(\d{1})', r'\1 \2', b10.strip())
    b12 = re.findall(r'([A-Z]\w+-*\w*)', b11)
    if len(b12) >= 2:
        player1, b13 = b12[:2]
        print(f"Match: {player1} vs {b13}")
        print(f"Score: {b11.strip()}\n")
if b14 = = "__main__":
    b15 = 'http:
    fonk1(b15)