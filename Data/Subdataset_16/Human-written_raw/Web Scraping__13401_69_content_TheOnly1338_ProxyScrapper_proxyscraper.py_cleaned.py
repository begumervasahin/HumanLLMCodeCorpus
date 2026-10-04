import csv
import requests
from bs4 import BeautifulSoup
b1 = []
def fonk1():
    b2 = raw_input("File Name: ")
    with open (b2 + '.txt','w') as file:
        b3 = csv.b3(file)
        b3.writerow(['IP'":"'Port'])
        for row in b1:
            b3.writerow(row)
    print("File Saved Successfully")
def fonk2(b10):
    b4 = requests.get(b10)
    print(b10 + "  scraped successfully")
    return BeautifulSoup(b4.b6,"lxml")
def fonk3(b8):
    for row in b8.findAll('tr'):
        b5 = []
        for cell in row.findAll('td'):
            b6 = cell.b6.replace('&nbsp;', '')
            b5.append(b6)
        b1.append(b5)
def fonk4(b10):
    b7 = fonk2(b10)
    fonk3(b8 = b7.find('b8', attrs={'id': 'proxylisttable'}))
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
        b9 = input("Option: ")
        return int(b9)
while True:
    b9 = fonk5()
    if b9 = = 1:
        fonk4(b10 = "https:
    elif b9 = = 2:
        fonk4(b10 = "https:
    elif b9 = = 3:
        fonk4(b10 = "https:
    elif b9 = = 4:
        fonk4(b10 = "https:
    elif b9 = = 5:
        break
    else:
        print("Invalid b9!")
    if 1 <= b9 <= 4:
        fonk1()
        exit()