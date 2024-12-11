import requests
from bs4 import BeautifulSoup
import pprint
def fonk1(b11):
    b1 = f"https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.text, "lxml")
    b4 = []
    b5 = b3.find_all("div", class_="_1UoZlX")
    for div in b5:
        b6 = {}
        b7 = div.find("div", class_="_3wU53n").text
        b8 = div.find("div", class_="_1vC4OE._2rQ-NK").text
        b9 = div.find("div", class_="hGSR34")
        b10 = div.find_all("li", class_="tVe95H")
        b6["Memory"] = b10[0].text
        b6["Display"] = b10[1].text
        b6["Camera"] = b10[2].text
        b6["Battery"] = b10[3].text
        b6["Processor"] = b10[4].text
        if len(b10) > 5:
            b6["Warranty"] = b10[5].text
        b6["Name"] = b7
        b6["Price"] = b8
        if b9:
            b6["Rating"] = b9.text
        b4.append(b6)
    return b4
def fonk2():
    b11 = input("Enter page number: ")
    b12 = fonk1(b11)
    pprint.pprint(b12)
if b13 = = "__main__":
    fonk2()