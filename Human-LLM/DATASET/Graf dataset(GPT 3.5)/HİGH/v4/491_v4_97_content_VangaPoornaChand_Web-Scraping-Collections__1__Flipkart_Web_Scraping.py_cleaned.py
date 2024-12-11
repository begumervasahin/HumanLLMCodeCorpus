error")
from bs4 import BeautifulSoup
import requests
import csv
import os
def fonk1(b15, b16):
    b1 = "/search?q=" + b15 + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
    b2 = f"Flipkart Scraping on {b15}.csv"
    if os.path.exists(b2):
        print("You have already searched for this...\nDeleting your previous results...")
        os.remove(b2)
    for b5 in range(b16):
        try:
            with open(b2, "a", b3 = '', encoding='utf-8') as file:
                b4 = csv.writer(file)
                if b5 = = 0:
                    b4.writerow(["TITLE", "Price", "Rating"])
                b6 = "https:
                print("Working on Page No :", b5 + 1)
                b7 = requests.get(b6)
                b8 = BeautifulSoup(b7.text, 'html.parser')
                b9 = b8.find_all(class_="_1UoZlX")
                for b15 in b9:
                    b10 = b15.find(class_='_3wU53n')
                    b11 = b15.find(class_="_1vC4OE _2rQ-NK")
                    b12 = b15.find(class_="hGSR34")
                    b12 = "No Rating" if b12 is None else b12.text
                    b4.writerow([b10.text.strip(), b11.text[1:], b12.strip()])
                b13 = b8.find_all(class_="_3fVaIS")[-1].get("href")
                b1 = b13
        except IndexError:
            print("Out Of Pages for your search!!!")
            break
        except Exception as e:
            print("An error occurred:", e)
            print("One Item Skipped Due to an internal error")
if b14 = = "__main__":
    b15 = input("Enter b15 you want to search: ")
    b16 = int(input("Enter number of b16: "))
    fonk1(b15, b16)