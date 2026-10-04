import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1(auth, api):
    b1 = 'http:
    b2 = BeautifulSoup(urlopen(b1), 'html.parser')
    b3 = fonk2(b2)
    b4 = fonk3(b2)
    b5 = fonk4(b2)
    fonk5(b5, auth, api, b3, b4)
def fonk2(soup):
    b6 = soup.find("div", class_="sec row")
    return ''.join(re.findall(r'([A-Z]\w+-*\w*)', b6.text))
def fonk3(soup):
    b7 = soup.findAll("div", class_="ind sub bold")
    return next((line.text for line in b7 if line.text != "FULL TOURNAMENT RESULTS"), "")
def fonk4(soup):
    b8 = soup.findAll("div", class_="ind")
    return [line.text.split("Final")[0] for line in b8 if "Final" in line.text]
def fonk5(b5, auth, api, b3, b4):
    b9 = sum(1 for match in b5 if match)
    fonk6(b5, b9, auth, api, b3, b4)
def fonk6(b5, count, auth, api, b3, b4):
    for match in b5:
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            b10 = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            b11 = re.findall(r'([A-Z]\w+-*\w*)', b10)
            b12 = re.findall(r'^[^:]+', b4)
            if len(b11) > 1:
                print(f"{b12[0]} of the {b3}")
                print(f"Match: {b11[0]} vs {b11[1]}")
                print(f"Score: {b10}")
