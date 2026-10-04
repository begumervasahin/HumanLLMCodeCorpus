from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import Balloon_tip as Bt
def get_current_date():
    return datetime.datetime.now().strftime("%d-%b-%Y")
def display_countries(countries):
    for i in countries:
        print(f'{i}. {countries[i]}')
def get_user_country_choice(countries):
    while True:
        try:
            nation = int(input('\nChoose any one of the above Countries: \n'))
            if nation in countries:
                return countries[nation]
            else:
                print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
                display_countries(countries)
        except ValueError:
            print('\n**** PLEASE ENTER A NUMBER. ****')
def get_user_location(nation):
    return input(f'Enter a Location in {nation}: ').strip().lower()
def get_time_period():
    try:
        time_period = int(input('Enter the No. of Days [1-14]: '))
        return 3 if time_period <= 0 or time_period > 14 else time_period
    except ValueError:
        print('Invalid input. Setting time period to 3 days.')
        return 3
def fetch_weather_data(nation, area, time_period):
    url = f'https:
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'lxml')
def scrape_weather_data(soup, time_period, date_1):
    weather_details = {}
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
    return weather_details
def display_weather_forecast(weather_details, area, nation, time_period):
    print(f'\n{time_period}-Day Weather Forecast for {area.title()}, {nation}:')
    table = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
    for date, details in weather_details.items():
        table.add_row([date, *details])
    print(table)
def show_balloon_tip(weather_details, curr_date, area, nation):
    Bt.balloon_tip(f'Today\'s Weather Update - {area.title()}, {nation}',
                   f'Min/Max Temp: {weather_details[curr_date][0]}\nWeather: {weather_details[curr_date][1]}\nFeels Like: {weather_details[curr_date][2]}')
def main():
    countries = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
    curr_date = get_current_date()
    date_1 = datetime.datetime.strptime(curr_date, "%d-%b-%Y")
    display_countries(countries)
    nation = get_user_country_choice(countries)
    area = get_user_location(nation)
    time_period = get_time_period()
    soup = fetch_weather_data(nation, area, time_period)
    weather_details = scrape_weather_data(soup, time_period, date_1)
    display_weather_forecast(weather_details, area, nation, time_period)
    show_balloon_tip(weather_details, curr_date, area, nation)
if __name__ == "__main__":
    main()