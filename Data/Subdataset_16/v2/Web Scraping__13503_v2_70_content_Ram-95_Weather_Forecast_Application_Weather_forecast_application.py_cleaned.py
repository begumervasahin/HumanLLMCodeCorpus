import requests
from bs4 import BeautifulSoup
import datetime
from prettytable import PrettyTable
import sys
def fonk1(title, message):
    print(f"{title}\n{message}")
b1 = {}
b2 = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
b3 = datetime.datetime.now().strftime("%d-%b-%Y")
b4 = datetime.datetime.strptime(b3, "%d-%b-%Y")
b5 = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
for i, country in b2.items():
    print(f'{i}. {country}')
while True:
    try:
        b6 = int(input('\nChoose any one of the above b2: \n'))
        if b6 in b2:
            break
        else:
            print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
    except ValueError:
        print('\n**** PLEASE ENTER A NUMBER. ****')
b7 = b2[b6]
b8 = input(f'Enter a location in {b7}: ').strip().lower()
b9 = int(input('Enter the number of days [1-14]: '))
b9 = 3 if b9 <= 0 or b9 > 14 else b9
b10 = f'https:
b11 = requests.get(b10, b5=b5)
b12 = BeautifulSoup(b11.text, 'lxml')
b13 = b12.find('tbody')
for i in range(b9):
    b14 = b4 + datetime.timedelta(days=i)
    try:
        b15 = b13.select_one(f"tr:nth-of-type({i + 1})")
        b16 = b15.select_one("td:nth-of-type(2)").text
        b17 = b15.select_one("td:nth-of-type(3)").text
        b18 = b15.select_one("td:nth-of-type(4)").text
        b1[b14.strftime("%d-%b-%Y")] = [b16, b17, b18]
    except AttributeError:
        print('Weather forecast not available for this location. Please enter a popular location.')
        sys.exit(8)
print(f'\n{b9}-Day Weather Forecast for {b8.title()}, {b7}:')
b19 = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
for date, details in b1.items():
    b19.add_row([date, *details])
print(b19)
if b3 in b1:
    fonk1(f'Today\'s Weather Update - {b8.title()}, {b7}',
                f'Min/Max Temp: {b1[b3][0]}\nWeather: {b1[b3][1]}\nFeels Like: {b1[b3][2]}')
else:
    print("Today's weather update is not available.")