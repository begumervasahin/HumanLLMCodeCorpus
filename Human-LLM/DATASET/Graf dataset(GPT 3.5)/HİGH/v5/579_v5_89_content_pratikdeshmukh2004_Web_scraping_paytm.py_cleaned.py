import requests
import webbrowser
import random
from bs4 import BeautifulSoup
def fonk1(url):
    b1 = requests.get(url)
    return BeautifulSoup(b1.text, "lxml")
def fonk2(categories):
    for idx, category in enumerate(categories, b2 = 1):
        print(f"{idx}. {category.text}")
def fonk3(message, options):
    while True:
        try:
            b3 = int(input(message))
            if 1 <= b3 <= len(options):
                return b3
            else:
                print("Invalid b3. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def fonk4(products):
    a1 = 1
    b4 = str(random.randint(31, 37))
    b5 = []
    for product in products:
        b6 = product.find("a").get("b6")
        b7 = product.find("a").find("span").text
        b8 = product.find("div", class_="_27VV").text
        print(f"\033[1;{b4};40m{a1}. {b6}")
        print(f"  Price: {b7}")
        print(f" {b8}")
        b5.append("https:
        a1 += 1
    return b5
def fonk5():
    b9 = "https:
    b10 = fonk1(b9)
    print("***********Welcome to {}*************".format(b10.b6.text))
    b11 = b10.find("div", class_="_1_Nn")
    b12 = b11.find_all("a")
    fonk2(b12)
    b13 = fonk3("Which category do you want to explore? Enter the corresponding number: ", b12)
    b14 = "https:
    b15 = fonk1(b14)
    b16 = b15.find("div", class_="_3RA-")
    b17 = b16.find_all("div", class_="_1fje")
    b5 = fonk4(b17)
    b18 = fonk3("Which product do you want to view? Enter the corresponding number: ", b17)
    webbrowser.open_new_tab(b5[b18 - 1])
if b19 = = "__main__":
    fonk5()