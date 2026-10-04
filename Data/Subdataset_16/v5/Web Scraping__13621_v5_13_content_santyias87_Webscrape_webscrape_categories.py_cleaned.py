from selenium import webdriver
from bs4 import BeautifulSoup as soup
import math
import pandas as pd
b1 = pd.read_csv("geo.csv", b21="ISO-8859-1")
b2 = b1['city']
b3 = b1['b13']
b4 = b1['lng']
b5 = webdriver.FirefoxProfile()
b5.set_preference('permissions.default.stylesheet', 2)
b5.set_preference('permissions.default.image', 2)
b5.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
b6 = webdriver.Firefox(b5=b5)
b7 = {
    'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14,
    'Salad Bar': 20, 'Take Out': 24, 'American': 5, 'Asian': 28,
    'Australian': 47, 'Brazilian': 46, 'British': 30, 'Caribbean': 31,
    'Chinese': 7, 'European': 34, 'French': 35, 'Fusion': 36, 'German': 37,
    'Indian': 8, 'International': 9, 'Italian': 10, 'Japanese': 11,
    'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
    'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
}
for category, feature_id in b7.items():
    b8 = []
    for city_name, latitude, longitude in zip(b2, b3, b4):
        b9 = "https:
        b10 = (
            f"?&b11 = vegan-vegetarian&ft={feature_id}"
            f"&b12 = 25&metric=mi&limit=81&order=default"
            f"&b13 = {latitude}&lng={longitude}"
        )
        b14 = b9 + b10
        b6.get(b14)
        b15 = b6.page_source
        b16 = soup(b15, 'html.parser')
        b17 = int(b16.find("span", {"class": "total-results"}).text.strip())
        b18 = math.ceil(b17 / 81)
        for page_number in range(1, b18 + 1):
            if page_number > 1:
                b14 = b9 + b10 + f"&page={page_number}"
                b6.get(b14)
                b15 = b6.page_source
                b16 = soup(b15, 'html.parser')
            for venue in b16.findAll(b19 = {"class": "js-venues venues__item"}):
                b8.append(venue["b8-id"] + "\n")
    b20 = f"category_{category}.csv"
    with open(b20, "w", b21 = "utf-8") as file:
        file.writelines(b8)
b6.quit()