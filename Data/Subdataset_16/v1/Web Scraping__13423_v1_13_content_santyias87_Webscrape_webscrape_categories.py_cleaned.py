import math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.b5 import Options
from bs4 import BeautifulSoup as soup
b1 = pd.read_csv("geo.csv", b20="ISO-8859-1")
b2 = b1['city']
b3 = b1['lat']
b4 = b1['lng']
b5 = Options()
b5.set_preference('permissions.default.stylesheet', 2)
b5.set_preference('permissions.default.image', 2)
b5.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
b5.b6 = True
b7 = webdriver.Firefox(b5=b5)
b8 = {'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14, 'Salad Bar': 20, 'Take Out': 24, 'American': 5,
           'Asian': 28, 'Australian': 47, 'Brazilian': 46, 'British': 30, 'Caribbean': 31, 'Chinese': 7, 'European': 34,
           'French': 35, 'Fusion': 36, 'German': 37, 'Indian': 8, 'International': 9, 'Italian': 10, 'Japanese': 11, 'Latin': 45,
           'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39, 'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42,
           'Western': 16}
b9 = ['Juice Bar', 'Macrobiotic', 'Organic', 'Raw food', 'Salad Bar', 'Take Out', 'American', 'Asian', 'Australian', 'Brazilian',
       'British', 'Caribbean', 'Chinese', 'European', 'French', 'Fusion', 'German', 'Indian', 'International', 'Italian', 'Japanese',
       'Latin', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Spanish', 'Taiwanese', 'Thai', 'Vietnamese', 'Western']
for category in b9:
    b10 = []
    b11 = b8[category]
    for city_name, lat, lng in zip(b2, b3, b4):
        b12 = f"https:
        b7.get(b12)
        b13 = b7.page_source
        b14 = soup(b13, 'html.parser')
        b15 = b14.find("span", {"class": "total-results"})
        if b15:
            b16 = int(b15.text.strip())
            b17 = math.ceil(b16 / 81)
            for count in range(1, b17 + 1):
                if count > 1:
                    b12 = f"https:
                    b7.get(b12)
                    b13 = b7.page_source
                    b14 = soup(b13, 'html.parser')
                for details in b14.findAll(b18 = {"class": "js-venues venues__item"}):
                    b10.append(details["b10-id"] + "\n")
    b19 = f"category_{category}.csv"
    with open(b19, "w", b20 = "utf-8") as f:
        f.writelines(b10)
b7.quit()