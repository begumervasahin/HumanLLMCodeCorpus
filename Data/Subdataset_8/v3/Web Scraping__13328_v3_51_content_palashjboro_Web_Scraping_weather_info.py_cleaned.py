import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'https:
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
main_section = soup.find(id='main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806')
day_elements = main_section.find_all(class_='date-time')
date_elements = main_section.find_all(class_='day-detail clearfix')
temp_elements = main_section.find_all('td', class_='temp')
desc_elements = main_section.find_all('td', class_='description')
rain_elements = main_section.find_all('td', class_='precip')
wind_elements = main_section.find_all('td', class_='wind')
humi_elements = main_section.find_all('td', class_='humidity')
days = [element.get_text() for element in day_elements]
dates = [element.get_text() for element in date_elements]
temperatures = [element.get_text() for element in temp_elements]
descriptions = [element.get_text() for element in desc_elements]
precipitations = [element.get_text() for element in rain_elements]
winds = [element.get_text() for element in wind_elements]
humidities = [element.get_text() for element in humi_elements]
weather_data = {
    'Day': days,
    'Date': dates,
    'Description': descriptions,
    'Temperature': temperatures,
    'Rain Percip': precipitations,
    'Wind': winds,
    'Humidity': humidities
}
weather_info = pd.DataFrame(weather_data)
print(weather_info)