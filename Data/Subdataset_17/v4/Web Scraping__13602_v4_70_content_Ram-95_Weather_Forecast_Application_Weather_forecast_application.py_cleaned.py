from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import Balloon_tip as Bt
weather_details = {}
countries = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
curr_date = datetime.datetime.now().strftime("%d-%b-%Y")
date_1 = datetime.datetime.strptime(curr_date, "%d-%b-%Y")
headers = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
for i in countries:
    print(f'{i}. {countries[i]}')
while True:
    try:
        nation = int(input('\nChoose any one of the above Countries: \n'))
        if nation in countries.keys():
            break
        else:
            print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
            for i in countries:
                print(f'{i}. {countries[i]}')
    except ValueError:
        print('\n**** PLEASE ENTER A NUMBER. ****')
nation = countries[nation]
area = input(f'Enter a Location in {nation}: ').strip().lower()
try:
    time_period = int(input('Enter the No. of Days [1-14]: '))
    time_period = 3 if time_period <= 0 or time_period > 14 else time_period
except ValueError:
    print('Invalid input. Setting time period to 3 days.')
    time_period = 3
url = f'https:
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')
temp = soup.find('tbody')
for i in range(time_period):
    end_date = date_1 + datetime.timedelta(days=i)
    try:
        temperature = temp.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(2)").text
        weather_conditions = temp.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(3)").text
        feels_like = temp.select_one(f"tr:nth-of-type({i+1}) td:nth-of-type(4)").text
        weather_details[end_date.strftime("%d-%b-%Y")] = [temperature, weather_conditions, feels_like]
    except AttributeError:
        print('Weather Forecast NOT AVAILABLE for this location. Please enter a popular location.')
        sys.exit(8)
print(f'\n{time_period}-Day Weather Forecast for {area.title()}, {nation}:')
table = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
for date, details in weather_details.items():
    table.add_row([date, *details])
print(table)
Bt.balloon_tip(f'Today\'s Weather Update - {area.title()}, {nation}',
               f'Min/Max Temp: {weather_details[curr_date][0]}\nWeather: {weather_details[curr_date][1]}\nFeels Like: {weather_details[curr_date][2]}')