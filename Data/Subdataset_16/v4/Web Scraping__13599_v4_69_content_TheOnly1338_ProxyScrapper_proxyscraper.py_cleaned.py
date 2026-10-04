import csv
import requests
from bs4 import BeautifulSoup
b1 = []
def fonk1():
    b2 = input("File Name: ")
    with open(b2 + '.txt', 'w', b3 = '') as file:
        b4 = csv.b4(file)
        b4.writerow(['IP', 'Port'])
        for row in b1:
            b4.writerow(row)
    print("File Saved Successfully")
def fonk2(b11):
    b5 = requests.get(b11)
    print(f"{b11} scraped successfully")
    return BeautifulSoup(b5.b7, "lxml")
def fonk3(b9):
    for row in b9.findAll('tr'):
        b6 = []
        for cell in row.findAll('td'):
            b7 = cell.b7.replace('&nbsp;', '')
            b6.append(b7)
        if b6:
            b1.append(b6[:2])
def fonk4(b11):
    b8 = fonk2(b11)
    fonk3(b9 = b8.find('b9', attrs={'id': 'proxylisttable'}))
def fonk5():
    print("   _______      ___      .______      .______       _______ .___________.___________. ")
    print("  /  _____|    /   \     |   _  \     |   _  \     |   ____||           |           | ")
    print(" |  |  __     /  ^  \    |  |_)  |    |  |_)  |    |  |__   `---|  |----`---|  |----` ")
    print(" |  | |_ |   /  /_\\  \\   |      /     |      /     |   __|      |  |        |  |      ")
    print(" |  |__| |  /  _____  \\  |  |\\  \\----.|  |\\  \\----.|  |____     |  |        |  |      ")
    print("  \\______| /__/     \\__\\ | _| `._____|| _| `._____||_______|    |__|        |__|      ")
    print("")
    print("Please Select A Source To Scrape From:")
    print(" 1. http:
    print(" 2. http:
    print(" 3. http:
    print(" 4. http:
    print(" 5. Exit")
    b10 = input("Option: ")
    return int(b10)
def fonk6():
    while True:
        b10 = fonk5()
        if b10 = = 1:
            fonk4(b11 = "https:
        elif b10 = = 2:
            fonk4(b11 = "https:
        elif b10 = = 3:
            fonk4(b11 = "https:
        elif b10 = = 4:
            fonk4(b11 = "https:
        elif b10 = = 5:
            break
        else:
            print("Invalid b10!")
        if 1 <= b10 <= 4:
            fonk1()
            break
if b12 = = "__main__":
    fonk6()