import requests
from bs4 import BeautifulSoup
import pprint
def fonk1(b11):
    b1 = requests.get(b11)
    b2 = BeautifulSoup(b1.text, "html.parser")
    b3 = b2.find_all("div", b6="_1UoZlX")
    b4 = []
    for container in b3:
        b5 = {}
        b5["Name"] = container.find("div", b6 = "_3wU53n").text
        b5["Price"] = container.find("div", b6 = "_1vC4OE _2rQ-NK").text
        b7 = container.find("div", b6="hGSR34")
        if b7:
            b5["Rating"] = b7.text
        b8 = container.find_all("li", b6="tVe95H")
        for detail in b8:
            key, b9 = detail.text.split(": ")
            b5[key] = b9
        b4.append(b5)
    return b4
def fonk2():
    b10 = input("Enter page number: ")
    b11 = f"https:
    b4 = fonk1(b11)
    pprint.pprint(b4)
if b12 = = "__main__":
    fonk2()