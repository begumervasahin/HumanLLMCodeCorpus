from bs4 import BeautifulSoup
import requests
import csv
import os
def fonk1(b16):
    return f"/search?b1 = {b16}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
def fonk2(b13):
    return b13.find_all(b2 = "_3fVaIS")[-1].get("href")
def fonk3(b16):
    b3 = b16.find(b2='_3wU53n').text.strip()
    b4 = b16.find(b2="_1vC4OE _2rQ-NK").text.strip()[1:]
    b5 = b16.find(b2="hGSR34")
    b5 = "No Rating" if b5 is None else b5.text.strip()
    return b3, b4, b5
def fonk4(b16, b17):
    b6 = fonk1(b16)
    b7 = f"Flipkart Scraping on {b16}.csv"
    if os.path.exists(b7):
        print("You have already searched for this...\nDeleting your previous results...")
        os.remove(b7)
    for b10 in range(b17):
        try:
            with open(b7, "a", b8 = '', encoding='utf-8') as file:
                b9 = csv.writer(file)
                if b10 = = 0:
                    b9.writerow(["TITLE", "Price", "Rating"])
                b11 = "https:
                print("Working on Page No :", b10 + 1)
                b12 = requests.get(b11)
                b13 = BeautifulSoup(b12.text, 'html.parser')
                b14 = b13.find_all(b2="_1UoZlX")
                for b16 in b14:
                    b3, b4, b5 = fonk3(b16)
                    b9.writerow([b3, b4, b5])
                b6 = fonk2(b13)
        except IndexError:
            print("Out Of Pages for your search!!!")
            break
        except Exception as e:
            print("An error occurred:", e)
            print("One Item Skipped Due to an internal error")
if b15 = = "__main__":
    b16 = input("Enter b16 you want to search: ")
    b17 = int(input("Enter number of b17: "))
    fonk4(b16, b17)