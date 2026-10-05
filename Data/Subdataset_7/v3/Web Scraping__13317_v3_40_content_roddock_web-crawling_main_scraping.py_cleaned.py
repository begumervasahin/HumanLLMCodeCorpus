import requests
from bs4 import BeautifulSoup
def fonk1(b9):
    try:
        b1 = requests.get(b9)
        return b1.text
    except Exception as e:
        print("Error fetching HTML:", e)
        return None
def fonk2(b10):
    try:
        b2 = BeautifulSoup(b10, 'html.parser')
        b3 = b2.b3.string
        return b3
    except Exception as e:
        print("Error extracting b3:", e)
        return None
def fonk3(b10):
    try:
        b2 = BeautifulSoup(b10, 'html.parser')
        b4 = b2.b4
        return b4
    except Exception as e:
        print("Error extracting b4:", e)
        return None
def fonk4(b10):
    try:
        b2 = BeautifulSoup(b10, 'html.parser')
        b5 = b2.find_all('p')
        return b5
    except Exception as e:
        print("Error extracting text paragraphs:", e)
        return None
def fonk5(b10):
    try:
        b2 = BeautifulSoup(b10, 'html.parser')
        b6 = b2.head
        return b6
    except Exception as e:
        print("Error extracting head section:", e)
        return None
def fonk6(b10):
    try:
        b2 = BeautifulSoup(b10, 'html.parser')
        b7 = b2.find_all('a')
        return b7
    except Exception as e:
        print("Error extracting b7:", e)
        return None
def fonk7(b10):
    try:
        b2 = BeautifulSoup(b10, 'html.parser')
        b8 = b2.find_all('img')
        return b8
    except Exception as e:
        print("Error extracting b8:", e)
        return None
b9 = "https:
b10 = fonk1(b9)
if b10 is None:
    print("Failed to fetch HTML content.")
else:
    b3 = fonk2(b10)
    print("*** Title: ***")
    print(b3 if b3 else "Title not found")
    b4 = fonk3(b10)
    print("\n*** Body: ***")
    print(b4 if b4 else "Body not found")
    b5 = fonk4(b10)
    print("\n*** Text Paragraphs: ***")
    if b5:
        for paragraph in b5:
            print(paragraph.get_text())
    b6 = fonk5(b10)
    print("\n*** Head Section: ***")
    print(b6 if b6 else "Head section not found")
    b7 = fonk6(b10)
    print("\n*** Links: ***")
    if b7:
        for link in b7:
            if "href" in link.attrs:
                print(link.attrs["href"])
    b8 = fonk7(b10)
    print("\n*** Images: ***")
    if b8:
        for image in b8:
            if "src" in image.attrs:
                print(image.attrs["src"])