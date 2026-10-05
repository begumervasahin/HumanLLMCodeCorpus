import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1():
    b1 = 'http:
    with urlopen(b1) as response:
        b2 = BeautifulSoup(response, 'html.parser')
    b3 = b2.find_all("div", class_="ind")
    b4 = b2.find("div", class_="sec row")
    b5 = b4.text
    b6 = ' '.join(re.findall(r'([A-Z]\w+-*\w*)', b5))
    b7 = b2.find_all("div", class_="ind sub bold")
    for section in b7:
        if section.text != "FULL TOURNAMENT RESULTS":
            b8 = section.text
            break
    b9 = []
    for section in b3:
        if "Final" in section.text:
            b10 = section.text.split("Final")
            b9.extend(b10)
    fonk2(b9, b6, b8)
def fonk2(b9, b6, b8):
    b11 = sum(1 for match in b9 if match.strip())
    print(f"Tournament Round: {b8} of the Tournament: {b6}")
    for match in b9:
        if match.strip() and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            fonk3(match, b8)
def fonk3(match, b8):
    b12 = re.sub(r'([a-z])(\d{1})', r'\1 \2', match.strip())
    b13 = re.findall(r'([A-Z]\w+-*\w*)', b12)
    if len(b13) >= 2:
        player1, b14 = b13[:2]
        print(f"Match: {player1} vs {b14}")
        print(f"Score: {b12.strip()}\n")
if b15 = = "__main__":
    fonk1()