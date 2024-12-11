
import requests
import webbrowser
import random
from bs4 import BeautifulSoup
b1 = requests.get("https:
b2 = BeautifulSoup(b1.text, "lxml")
print("***********Welcome to {}*************".format(b2.title.text))
b3 = b2.find("div", b16="_1_Nn")
b4 = b3.find_all("a")
for idx, category in enumerate(b4, b5 = 1):
    print(idx, category.text)
b6 = input("Which category do you want to explore (enter the corresponding number): ")
b7 = "https:
b8 = requests.get(b7)
b9 = BeautifulSoup(b8.text, "lxml")
b10 = b9.find("div", b16="_3RA-")
b11 = b10.find_all("div", b16="_1fje")
a1 = 1
b12 = []
b13 = str(random.randint(31, 37))
for product_div in b11:
    b14 = product_div.find_all("div", b16="_2i1r")
    for info in b14:
        print("\033[1;{};40m".format(b13) + str(a1) + " " + info.find("a").get("title"))
        a1 += 1
        b15 = info.find("a").find("span")
        print("  Price: " + b15.text)
        print(" " + info.find("div", b16 = "_27VV").text)
        b12.append("https:
b17 = int(input("Which product do you want to view (enter the corresponding number): "))
webbrowser.open_new_tab(b12[b17 - 1])