
import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'https:
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
main_section = soup.find(id='main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806')
day_elements = main_section.find_all(class_='date-time')
date_elements = main_section.find_all(class_='day-detail clearfix')
temp_elements = main_section.find_all('td', class_='temp')
desc_elements = main_section.find_all('td', class_='description')
rain_elements = main_section.find_all('td', class_='precip')
wind_elements = main_section.find_all('td', class_='wind')
humi_elements = main_section.find_all('td', class_='humidity')
days = [item.get_text() for item in day_elements]
dates = [item.get_text() for item in date_elements]
temperatures = [item.get_text() for item in temp_elements]
descriptions = [item.get_text() for item in desc_elements]
rain_percipitations = [item.get_text() for item in rain_elements]
winds = [item.get_text() for item in wind_elements]
humidities = [item.get_text() for item in humi_elements]
weather_info = pd.DataFrame({
    'Day': days,
    'Date': dates,
    'Description': descriptions,
    'Temperature': temperatures,
    'Rain Percip': rain_percipitations,
    'Wind': winds,
    'Humidity': humidities
})
print(weather_info)