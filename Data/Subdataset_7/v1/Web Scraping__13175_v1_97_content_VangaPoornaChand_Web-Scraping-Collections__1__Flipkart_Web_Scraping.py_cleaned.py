from bs4 import BeautifulSoup
import requests
import csv
import os
b1 = input("Enter b1 you want to b3: ")
b2 = int(input("Enter number of b2: "))
b3 = "/b3?q=" + b1 + "&otracker=b3&otracker1=b3&marketplace=FLIPKART&as-show=off&as=off"
b4 = f"Flipkart Scraping on {b1}.csv"
if os.path.exists(b4):
    print("You have already searched for this...\nDeleting your previous results...")
    os.remove(b4)
for b7 in range(b2):
    try:
        with open(b4, "a", b5 = "", encoding="utf-8") as file:
            b6 = csv.writer(file)
            if b7 = = 0:
                b6.writerow(["TITLE", "Price", "Rating"])
            b8 = "https:
            print("Working on Page No:", b7+1)
            b9 = requests.get(b8)
            b10 = BeautifulSoup(b9.text, 'lxml')
            for mobile_area in b10.find_all(b11 = "_1UoZlX"):
                b12 = mobile_area.find(b11='_3wU53n').text.strip()
                b13 = mobile_area.find(b11="_1vC4OE._2rQ-NK").text.strip()[1:]
                b14 = mobile_area.find(b11="hGSR34")
                b15 = b14.text.strip() if b14 else "No Rating"
                b6.writerow([b12, b13, b15])
            b16 = b10.find_all(b11="_3fVaIS")[-1]['href']
            b3 = b16
    except IndexError:
        print("Out Of Pages for your b3!!!")
        break
    except Exception as e:
        print("An error occurred:", e)