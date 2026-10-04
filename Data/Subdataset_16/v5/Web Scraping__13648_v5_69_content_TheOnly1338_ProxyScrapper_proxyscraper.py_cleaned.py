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
def fonk2(url):
    b5 = requests.get(url)
    print(f"{url} scraped successfully")
    return BeautifulSoup(b5.b7, "lxml")
def fonk3(table):
    for row in table.find_all('tr'):
        b6 = []
        for cell in row.find_all('td'):
            b7 = cell.b7.strip()
            b6.append(b7)
        if b6:
            b1.append(b6[:2])
def fonk4(url):
    b8 = fonk2(url)
    b9 = b8.find('table', attrs={'id': 'proxylisttable'})
    if b9:
        fonk3(b9)
    else:
        print("Proxy table not found on the page.")
def fonk5():
    print()
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
            fonk4("https:
        elif b10 = = 2:
            fonk4("https:
        elif b10 = = 3:
            fonk4("https:
        elif b10 = = 4:
            fonk4("https:
        elif b10 = = 5:
            break
        else:
            print("Invalid b10!")
        if 1 <= b10 <= 4:
            fonk1()
            break
if b11 = = "__main__":
    fonk6()