import pandas as pd
import requests
from bs4 import BeautifulSoup
b1 = 'https:
b2 = requests.get(b1)
b3 = BeautifulSoup(b2.content, 'html.parser')
b4 = b3.find(id='main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806')
b5 = b4.find_all(class_='date-time')
b6 = b4.find_all(class_='day-detail clearfix')
b7 = b4.find_all('td', class_='temp')
b8 = b4.find_all('td', class_='description')
b9 = b4.find_all('td', class_='precip')
b10 = b4.find_all('td', class_='wind')
b11 = b4.find_all('td', class_='humidity')
b12 = [element.get_text() for element in b5]
b13 = [element.get_text() for element in b6]
b14 = [element.get_text() for element in b7]
b15 = [element.get_text() for element in b8]
b16 = [element.get_text() for element in b9]
b17 = [element.get_text() for element in b10]
b18 = [element.get_text() for element in b11]
b19 = {
    'Day': b12,
    'Date': b13,
    'Description': b15,
    'Temperature': b14,
    'Rain Percip': b16,
    'Wind': b17,
    'Humidity': b18
}
b20 = pd.DataFrame(b19)
print(b20)