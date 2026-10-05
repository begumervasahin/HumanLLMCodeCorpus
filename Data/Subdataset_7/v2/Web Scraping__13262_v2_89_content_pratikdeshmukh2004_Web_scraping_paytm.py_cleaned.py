import requests
import webbrowser
import random
from bs4 import BeautifulSoup
def fonk1(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        return BeautifulSoup(b1.text, 'html.parser')
    else:
        print("Failed to fetch page:", url)
        return None
def fonk2(b8):
    print("Categories:")
    for idx, category in enumerate(b8, b3 = 1):
        print(f"{idx}. {category.text.strip()}")
def fonk3(b6):
    b4 = b6.find_all("div", class_="_2i1r")
    return ["https:
def fonk4():
    b5 = "https:
    b6 = fonk1(b5)
    if not b6:
        return
    print("***********Welcome to", b6.title.text.strip(), "*************")
    b7 = b6.find("div", class_="_1_Nn")
    b8 = b7.find_all("a")
    fonk2(b8)
    b9 = int(input("Which category do you want? (Enter the number): "))
    b10 = "https:
    b11 = fonk1(b10)
    if not b11:
        return
    b12 = fonk3(b11)
    b13 = random.b9(b12)
    print("Opening a random product from the selected category...")
    webbrowser.open_new_tab(b13)
if b14 = = "__main__":
    fonk4()