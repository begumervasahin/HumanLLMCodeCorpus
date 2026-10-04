import csv
import requests
from bs4 import BeautifulSoup
b1 = []
def fonk1():
    b2 = input("File Name: ")
    with open(b2 + '.csv', 'w', b3 = '') as file:
        b4 = csv.b4(file)
        b4.writerow(['IP', 'Port'])
        for row in b1:
            b4.writerow(row)
    print("File Saved Successfully")
def fonk2(b13):
    b5 = requests.get(b13)
    print(b13 + "  scraped successfully")
    return BeautifulSoup(b5.text, "lxml")
def fonk3(table):
    for row in table.findAll('tr'):
        b6 = []
        b7 = row.findAll('td')
        if len(b7) > 1:
            b8 = b7[0].text.strip()
            b9 = b7[1].text.strip()
            b6.append(b8)
            b6.append(b9)
            b1.append(b6)
def fonk4(b13):
    b10 = fonk2(b13)
    fonk3(b10.find('table', b11 = {'id': 'proxylisttable'}))
def fonk5():
    print("   _______      ___      .______      .______       _______ .___________.___________. ")
    print("  /  _____|    /   \     |   _  \     |   _  \     |   ____||           |           | ")
    print(" |  |  __     /  ^  \    |  |_)  |    |  |_)  |    |  |__   `---|  |----`---|  |----` ")
    print(" |  | |_ |   /  /_\  \   |      /     |      /     |   __|      |  |        |  |      ")
    print(" |  |__| |  /  _____  \  |  |\  \----.|  |\  \----.|  |____     |  |        |  |      ")
    print("  \______| /__/     \__\ | _| `._____|| _| `._____||_______|    |__|        |__|      ")
    print("")
    print("Please Select A Source To Scrape From:")
    print(" 1. http:
    print(" 2. http:
    print(" 3. http:
    print(" 4. http:
    print(" 5. Exit")
    b12 = input("Option: ")
    return int(b12)
while True:
    b12 = fonk5()
    if b12 = = 1:
        fonk4(b13 = "https:
    elif b12 = = 2:
        fonk4(b13 = "https:
    elif b12 = = 3:
        fonk4(b13 = "https:
    elif b12 = = 4:
        fonk4(b13 = "https:
    elif b12 = = 5:
        break
    else:
        print("Invalid b12!")
    if 1 <= b12 <= 4:
        fonk1()
        b1.clear()
