import pandas as pd
import requests
from bs4 import BeautifulSoup
b1 = requests.get('https:
b2 = BeautifulSoup(b1.content, 'html.parser')
b3 = b2.find(id='b3-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806')
b4 = b3.find_all(class_='date-time')
b5 = b3.find_all(class_='day-detail clearfix')
b6 = b3.find_all('td',class_='b13')
b7 = b3.find_all('td',class_='description')
b8 = b3.find_all('td',class_='precip')
b9 = b3.find_all('td',class_='b16')
b10 = b3.find_all('td',class_='humidity')
b11 = [item.get_text() for item in b4]
b12 = [item.get_text() for item in b5]
b13 = [item.get_text() for item in b6]
b14 = [item.get_text() for item in b7]
b15 = [item.get_text() for item in b8]
b16 = [item.get_text() for item in b9]
b17 = [item.get_text() for item in b10]
b18 = pd.DataFrame({
	'Day':b11,
	'Date': b12,
	'Description': b14,
	'Temperature': b13,
	'Rain Percip': b15,
	'Wind': b16,
	'Humidity': b17
	})
print(b18)