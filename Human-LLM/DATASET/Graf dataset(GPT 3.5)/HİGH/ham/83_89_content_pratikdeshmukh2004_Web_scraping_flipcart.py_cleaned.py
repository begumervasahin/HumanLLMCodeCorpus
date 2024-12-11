import requests,webbrowser,pprint
from bs4 import BeautifulSoup
def fonk1(b1):
    b1 = requests.get(b1)
    b2 = BeautifulSoup(b1.text,"lxml")
    b3 = b2.find_all("div",class_="_1UoZlX")
    b4 = b2.find_all("a",class_="_31qSD5")
    b5 = []
    for div in b3:
        b6 = {}
        b7 = (div.find("div",class_="_3wU53n").text)
        b8 = (div.find("div",class_="_1vC4OE _2rQ-NK").text)
        b9 = (div.find("div",class_="hGSR34"))
        b10 = div.find_all("li",class_="tVe95H")
        b6["Memory"]=b10[0].text
        b6["Display"]=b10[1].text
        b6["Camera"]=b10[2].text
        b6["Battry"]=b10[3].text
        b6["Prosser"]=b10[4].text
        if len(b10)>5:
            b6["Warranty"]=b10[5].text
        b6["Name"]=b7
        b6["Price"]=b8
        if not(b9 = = None):
            b6["Ratting"]=b9.text
        b5.append(b6)
    pprint.pprint(b5)
b11 = input("aapako kaunsa page chaiye : ")
fonk1("https: