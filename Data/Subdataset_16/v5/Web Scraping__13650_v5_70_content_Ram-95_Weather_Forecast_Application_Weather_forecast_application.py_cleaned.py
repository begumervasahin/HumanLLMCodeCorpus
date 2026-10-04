from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import Balloon_tip as Bt
def fonk1():
    return datetime.datetime.now().strftime("%d-%b-%Y")
def fonk2(b13):
    for i in b13:
        print(f'{i}. {b13[i]}')
def fonk3(b13):
    while True:
        try:
            b1 = int(input('\nChoose any one of the above Countries: \n'))
            if b1 in b13:
                return b13[b1]
            else:
                print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
                fonk2(b13)
        except ValueError:
            print('\n**** PLEASE ENTER A NUMBER. ****')
def fonk4(b1):
    return input(f'Enter a Location in {b1}: ').strip().lower()
def fonk5():
    try:
        b2 = int(input('Enter the No. of Days [1-14]: '))
        return 3 if b2 <= 0 or b2 > 14 else b2
    except ValueError:
        print('Invalid input. Setting time period to 3 days.')
        return 3
def fonk6(b1, b16, b2):
    b3 = f'https:
    b4 = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    b5 = requests.get(b3, b4=b4)
    return BeautifulSoup(b5.text, 'lxml')
def fonk7(b17, b2, b15):
    b6 = {}
    b7 = b17.find('tbody')
    for i in range(b2):
        b8 = b15 + datetime.timedelta(days=i)
        try:
            b9 = b7.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(2)").text
            b10 = b7.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(3)").text
            b11 = b7.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(4)").text
            b6[b8.strftime("%d-%b-%Y")] = [b9, b10, b11]
        except AttributeError:
            print('Weather Forecast NOT AVAILABLE for this location. Please enter a popular location.')
            sys.exit(8)
    return b6
def fonk8(b6, b16, b1, b2):
    print(f'\n{b2}-Day Weather Forecast for {b16.title()}, {b1}:')
    b12 = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
    for date, details in b6.items():
        b12.add_row([date, *details])
    print(b12)
def fonk9(b6, b14, b16, b1):
    Bt.balloon_tip(f'Today\'s Weather Update - {b16.title()}, {b1}',
                   f'Min/Max Temp: {b6[b14][0]}\nWeather: {b6[b14][1]}\nFeels Like: {b6[b14][2]}')
def fonk10():
    b13 = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
    b14 = fonk1()
    b15 = datetime.datetime.strptime(b14, "%d-%b-%Y")
    fonk2(b13)
    b1 = fonk3(b13)
    b16 = fonk4(b1)
    b2 = fonk5()
    b17 = fonk6(b1, b16, b2)
    b6 = fonk7(b17, b2, b15)
    fonk8(b6, b16, b1, b2)
    fonk9(b6, b14, b16, b1)
if b18 = = "__main__":
    fonk10()