import requests
from bs4 import BeautifulSoup
def fonk1(b9):
    try:
        b1 = requests.get(b9)
        b2 = BeautifulSoup(b1.text, 'html.parser')
        b3 = b2.b3.string
        return b3
    except Exception as e:
        print("Error:", e)
        return None
def fonk2(b9):
    try:
        b1 = requests.get(b9)
        b2 = BeautifulSoup(b1.text, 'html.parser')
        b4 = b2.b4
        return b4
    except Exception as e:
        print("Error:", e)
        return None
def fonk3(b9):
    try:
        b1 = requests.get(b9)
        b2 = BeautifulSoup(b1.text, 'html.parser')
        b5 = b2.find_all('p')
        return b5
    except Exception as e:
        print("Error:", e)
        return None
def fonk4(b9):
    try:
        b1 = requests.get(b9)
        b2 = BeautifulSoup(b1.text, 'html.parser')
        b6 = b2.b6
        return b6
    except Exception as e:
        print("Error:", e)
        return None
def fonk5(b9):
    try:
        b1 = requests.get(b9)
        b2 = BeautifulSoup(b1.text, 'html.parser')
        b7 = b2.find_all('a')
        return b7
    except Exception as e:
        print("Error:", e)
        return None
def fonk6(b9):
    try:
        b1 = requests.get(b9)
        b2 = BeautifulSoup(b1.text, 'html.parser')
        b8 = b2.find_all('img')
        return b8
    except Exception as e:
        print("Error:", e)
        return None
b9 = "https:
b3 = fonk1(b9)
if b3 = = None:
    print("b3 not found")
else:
    print("***b3 below here***")
    print(b3)
b4 = fonk2(b9)
if b4 = = None:
    print("b4 not found")
else:
    print("***b4 below here***")
    print(b4)
b5 = fonk3(b9)
if b5 = = None:
    print("text not found")
else:
    print("***text below here***")
    for text in b5:
        print(text.get_text())
b6 = fonk4(b9)
if b6 = = None:
    print("b6 not found")
else:
    print("***b6 below here***")
    print(b6)
b7 = fonk5(b9)
if b7 = = None:
    print("b9 not found")
else:
    print("***link below here***")
    for link in b7:
        if "href" in link.attrs:
            print(link.attrs["href"])
b8 = fonk6(b9)
if b8 = = None:
    print("b9 not found")
else:
    print("***link image below here***")
    for img in b8:
        if "src" in img.attrs:
            print(img.attrs["src"])