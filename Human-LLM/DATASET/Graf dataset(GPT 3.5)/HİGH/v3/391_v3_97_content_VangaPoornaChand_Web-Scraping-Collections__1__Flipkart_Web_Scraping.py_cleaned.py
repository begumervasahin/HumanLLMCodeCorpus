import os
import csv
import requests
from bs4 import BeautifulSoup
def fonk1():
    b1 = input("Enter the b1 you want to search: ")
    b2 = int(input("Enter the number of b2 to scrape: "))
    return b1, b2
def fonk2(b1):
    return f"/search?b3 = {b1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
def fonk3(b14):
    b4 = b14.find_all(class_="_1UoZlX")
    for b1 in b4:
        b5 = b1.find(class_='_3wU53n').text.strip()
        b6 = b1.find(class_="_1vC4OE._2rQ-NK").text.strip()[1:]
        b7 = b1.find(class_="hGSR34")
        b8 = b7.text.strip() if b7 else "No Rating"
        yield b5, b6, b8
def fonk4(b1, b2, b17):
    b9 = fonk2(b1)
    if os.path.exists(b17):
        print("Previous search results found. Deleting previous results...")
        os.remove(b17)
    with open(b17, "a", b10 = "", encoding="utf-8") as file:
        b11 = csv.writer(file)
        b11.writerow(["Title", "Price", "Rating"])
        for page_num in range(b2):
            print(f"Scraping data from page {page_num + 1}...")
            b12 = "https:
            b13 = requests.get(b12)
            b14 = BeautifulSoup(b13.text, 'lxml')
            for b5, b6, b8 in fonk3(b14):
                b11.writerow([b5, b6, b8])
            b15 = b14.find_all(class_="_3fVaIS")[-1]['href']
            b9 = b15
if b16 = = "__main__":
    b1, b2 = fonk1()
    b17 = f"Flipkart Scraping on {b1}.csv"
    fonk4(b1, b2, b17)