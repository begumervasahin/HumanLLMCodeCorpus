import requests
from bs4 import BeautifulSoup
import datetime
from prettytable import PrettyTable
import sys
def balloon_tip(title, message):
    print(f"{title}\n{message}")
weather_details = {}
countries = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
curr_date = datetime.datetime.now().strftime("%d-%b-%Y")
date_1 = datetime.datetime.strptime(curr_date, "%d-%b-%Y")
headers = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
for i, country in countries.items():
    print(f'{i}. {country}')
while True:
    try:
        nation_choice = int(input('\nChoose any one of the above countries: \n'))
        if nation_choice in countries:
            break
        else:
            print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
    except ValueError:
        print('\n**** PLEASE ENTER A NUMBER. ****')
nation = countries[nation_choice]
area = input(f'Enter a location in {nation}: ').strip().lower()
time_period = int(input('Enter the number of days [1-14]: '))
time_period = 3 if time_period <= 0 or time_period > 14 else time_period
url = f'https:
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
temp = soup.find('tbody')
for i in range(time_period):
    end_date = date_1 + datetime.timedelta(days=i)
    try:
        row = temp.select_one(f"tr:nth-of-type({i + 1})")
        temperature = row.select_one("td:nth-of-type(2)").text
        weather_conditions = row.select_one("td:nth-of-type(3)").text
        feels_like = row.select_one("td:nth-of-type(4)").text
        weather_details[end_date.strftime("%d-%b-%Y")] = [temperature, weather_conditions, feels_like]
    except AttributeError:
        print('Weather forecast not available for this location. Please enter a popular location.')
        sys.exit(8)
print(f'\n{time_period}-Day Weather Forecast for {area.title()}, {nation}:')
table = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
for date, details in weather_details.items():
    table.add_row([date, *details])
print(table)
if curr_date in weather_details:
    balloon_tip(f'Today\'s Weather Update - {area.title()}, {nation}',
                f'Min/Max Temp: {weather_details[curr_date][0]}\nWeather: {weather_details[curr_date][1]}\nFeels Like: {weather_details[curr_date][2]}')
else:
    print("Today's weather update is not available.")