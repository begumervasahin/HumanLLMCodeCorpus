from bs4 import BeautifulSoup
import requests
import csv
import os
def fonk1():
    b1 = input("Enter the b1 you want to search: ")
    b2 = int(input("Enter the number of b2 to scrape: "))
    return b1, b2
def fonk2(b1):
    b3 = f"/search?q={b1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
    return b3
def fonk3(b13):
    b4 = b13.find_all(class_="_1UoZlX")
    for b1 in b4:
        b5 = b1.find(class_='_3wU53n').text.strip()
        b6 = b1.find(class_="_1vC4OE._2rQ-NK").text.strip()[1:]
        b7 = b1.find(class_="hGSR34")
        b8 = b7.text.strip() if b7 else "No Rating"
        yield b5, b6, b8
def fonk4(b1, b2, b16):
    b3 = fonk2(b1)
    if os.path.exists(b16):
        print("Previous search results found. Deleting previous results...")
        os.remove(b16)
    with open(b16, "a", b9 = "", encoding="utf-8") as file:
        b10 = csv.writer(file)
        b10.writerow(["Title", "Price", "Rating"])
        for page_num in range(b2):
            print(f"Scraping data from page {page_num + 1}...")
            b11 = "https:
            b12 = requests.get(b11)
            b13 = BeautifulSoup(b12.text, 'lxml')
            for b5, b6, b8 in fonk3(b13):
                b10.writerow([b5, b6, b8])
            b14 = b13.find_all(class_="_3fVaIS")[-1]['href']
            b3 = b14
if b15 = = "__main__":
    b1, b2 = fonk1()
    b16 = f"Flipkart Scraping on {b1}.csv"
    fonk4(b1, b2, b16)