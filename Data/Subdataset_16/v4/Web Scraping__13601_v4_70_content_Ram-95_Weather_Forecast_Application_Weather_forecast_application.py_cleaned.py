from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import Balloon_tip as Bt
b1 = {}
b2 = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
b3 = datetime.datetime.now().strftime("%d-%b-%Y")
b4 = datetime.datetime.strptime(b3, "%d-%b-%Y")
b5 = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
for i in b2:
    print(f'{i}. {b2[i]}')
while True:
    try:
        b6 = int(input('\nChoose any one of the above Countries: \n'))
        if b6 in b2.keys():
            break
        else:
            print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
            for i in b2:
                print(f'{i}. {b2[i]}')
    except ValueError:
        print('\n**** PLEASE ENTER A NUMBER. ****')
b6 = b2[b6]
b7 = input(f'Enter a Location in {b6}: ').strip().lower()
try:
    b8 = int(input('Enter the No. of Days [1-14]: '))
    b8 = 3 if b8 <= 0 or b8 > 14 else b8
except ValueError:
    print('Invalid input. Setting time period to 3 days.')
    b8 = 3
b9 = f'https:
b10 = requests.get(b9, b5=b5)
b11 = b10.text
b12 = BeautifulSoup(b11, 'lxml')
b13 = b12.find('tbody')
for i in range(b8):
    b14 = b4 + datetime.timedelta(days=i)
    try:
        b15 = b13.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(2)").text
        b16 = b13.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(3)").text
        b17 = b13.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(4)").text
        b1[b14.strftime("%d-%b-%Y")] = [b15, b16, b17]
    except AttributeError:
        print('Weather Forecast NOT AVAILABLE for this location. Please enter a popular location.')
        sys.exit(8)
print(f'\n{b8}-Day Weather Forecast for {b7.title()}, {b6}:')
b18 = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
for date, details in b1.items():
    b18.add_row([date, *details])
print(b18)
Bt.balloon_tip(f'Today\'s Weather Update - {b7.title()}, {b6}',
               f'Min/Max Temp: {b1[b3][0]}\nWeather: {b1[b3][1]}\nFeels Like: {b1[b3][2]}')