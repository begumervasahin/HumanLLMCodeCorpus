import requests
from bs4 import BeautifulSoup
import datetime
from prettytable import PrettyTable
import sys
def fonk1(title, message):
    print(f"{title}\n{message}")
def fonk2(b14):
    for i, country in b14.items():
        print(f'{i}. {country}')
    while True:
        try:
            b1 = int(input('\nChoose any one of the above b14: \n'))
            if b1 in b14:
                return b14[b1]
            else:
                print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
        except ValueError:
            print('\n**** PLEASE ENTER A NUMBER. ****')
def fonk3(b17, b18, b19, b16):
    b2 = {}
    b3 = f'https:
    b4 = requests.get(b3, b16=b16)
    b5 = BeautifulSoup(b4.text, 'lxml')
    b6 = b5.find('tbody')
    if not b6:
        print('Weather forecast not available for this location. Please enter a popular location.')
        sys.exit(8)
    b7 = datetime.datetime.strptime(b15, "%d-%b-%Y")
    for i in range(b19):
        b8 = b7 + datetime.timedelta(days=i)
        try:
            b9 = b6.select_one(f"tr:nth-of-type({i + 1})")
            b10 = b9.select_one("td:nth-of-type(2)").text
            b11 = b9.select_one("td:nth-of-type(3)").text
            b12 = b9.select_one("td:nth-of-type(4)").text
            b2[b8.strftime("%d-%b-%Y")] = [b10, b11, b12]
        except AttributeError:
            print('Weather forecast not available for this location. Please enter a popular location.')
            sys.exit(8)
    return b2
def fonk4(b2, b18, b17, b19):
    print(f'\n{b19}-Day Weather Forecast for {b18.title()}, {b17}:')
    b13 = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
    for date, details in b2.items():
        b13.add_row([date, *details])
    print(b13)
def fonk5():
    b14 = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
    global b15
    b15 = datetime.datetime.now().strftime("%d-%b-%Y")
    b16 = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
    b17 = fonk2(b14)
    b18 = input(f'Enter a location in {b17}: ').strip().lower()
    b19 = int(input('Enter the number of days [1-14]: '))
    b19 = 3 if b19 <= 0 or b19 > 14 else b19
    b2 = fonk3(b17, b18, b19, b16)
    fonk4(b2, b18, b17, b19)
    if b15 in b2:
        fonk1(f'Today\'s Weather Update - {b18.title()}, {b17}',
                    f'Min/Max Temp: {b2[b15][0]}\nWeather: {b2[b15][1]}\nFeels Like: {b2[b15][2]}')
    else:
        print("Today's weather update is not available.")
if b20 = = "__main__":
    fonk5()