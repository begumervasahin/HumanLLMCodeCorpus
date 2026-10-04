import csv
import requests
from bs4 import BeautifulSoup
b1 = []
def fonk1():
    b2 = input("Enter the file name to save the proxies: ")
    with open(b2 + '.csv', 'w', b3 = '') as file:
        b4 = csv.b4(file)
        b4.writerow(['IP', 'Port'])
        for row in b1:
            b4.writerow(row)
    print(f"File saved successfully as {b2}.csv")
def fonk2(b12):
    try:
        b5 = requests.get(b12)
        b5.raise_for_status()
        print(f"{b12} scraped successfully")
        return BeautifulSoup(b5.text, "lxml")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {b12}: {e}")
        return None
def fonk3(b10):
    if b10:
        for row in b10.findAll('tr'):
            b6 = row.findAll('td')
            if len(b6) > 1:
                b7 = b6[0].text.strip()
                b8 = b6[1].text.strip()
                b1.append([b7, b8])
def fonk4(b12):
    b9 = fonk2(b12)
    if b9:
        b10 = b9.find('b10', attrs={'id': 'proxylisttable'})
        fonk3(b10)
def fonk5():
    print("   _______      ___      .______      .______       _______ .___________.___________. ")
    print("  /  _____|    /   \     |   _  \     |   _  \     |   ____||           |           | ")
    print(" |  |  __     /  ^  \    |  |_)  |    |  |_)  |    |  |__   `---|  |----`---|  |----` ")
    print(" |  | |_ |   /  /_\\  \\   |      /     |      /     |   __|      |  |        |  |      ")
    print(" |  |__| |  /  _____  \\  |  |\\  \\----.|  |\\  \\----.|  |____     |  |        |  |      ")
    print("  \\______| /__/     \\__\\ | _| `._____|| _| `._____||_______|    |__|        |__|      ")
    print("")
    print("Please select a source to scrape proxies from:")
    print(" 1. https:
    print(" 2. https:
    print(" 3. https:
    print(" 4. https:
    print(" 5. Exit")
    b11 = input("Option: ")
    return int(b11)
def fonk6():
    while True:
        b11 = fonk5()
        if b11 = = 1:
            fonk4(b12 = "https:
        elif b11 = = 2:
            fonk4(b12 = "https:
        elif b11 = = 3:
            fonk4(b12 = "https:
        elif b11 = = 4:
            fonk4(b12 = "https:
        elif b11 = = 5:
            break
        else:
            print("Invalid b11!")
        if 1 <= b11 <= 4:
            fonk1()
            b1.clear()
if b13 = = "__main__":
    fonk6()