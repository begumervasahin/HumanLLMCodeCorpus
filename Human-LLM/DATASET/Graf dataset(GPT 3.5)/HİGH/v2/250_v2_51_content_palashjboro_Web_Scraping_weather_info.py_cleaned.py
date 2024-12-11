
import pandas as pd
import requests
from bs4 import BeautifulSoup
b1 = requests.get('https:
b2 = BeautifulSoup(b1.content, 'html.parser')
b3 = b2.find(id='main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806')
b4 = b3.find_all(class_='date-time')
b5 = b3.find_all(class_='day-detail clearfix')
b6 = b3.find_all('td', class_='temp')
b7 = b3.find_all('td', class_='description')
b8 = b3.find_all('td', class_='precip')
b9 = b3.find_all('td', class_='wind')
b10 = b3.find_all('td', class_='humidity')
b11 = [element.get_text() for element in b4]
b12 = [element.get_text() for element in b5]
b13 = [element.get_text() for element in b6]
b14 = [element.get_text() for element in b7]
b15 = [element.get_text() for element in b8]
b16 = [element.get_text() for element in b9]
b17 = [element.get_text() for element in b10]
b18 = pd.DataFrame({
    'Day': b11,
    'Date': b12,
    'Description': b14,
    'Temperature': b13,
    'Rain Percip': b15,
    'Wind': b16,
    'Humidity': b17
})
print(b18)