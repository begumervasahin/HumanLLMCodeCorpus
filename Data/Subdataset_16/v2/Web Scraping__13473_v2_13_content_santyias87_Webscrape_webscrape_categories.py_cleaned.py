import math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.b5 import Options
from bs4 import BeautifulSoup
b1 = pd.read_csv("geo.csv", b23="ISO-8859-1")
b2 = b1['city']
b3 = b1['b14']
b4 = b1['lng']
b5 = Options()
b5.set_preference('permissions.default.stylesheet', 2)
b5.set_preference('permissions.default.image', 2)
b5.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
b5.b6 = True
b7 = webdriver.Firefox(b5=b5)
b8 = {
    'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14, 'Salad Bar': 20,
    'Take Out': 24, 'American': 5, 'Asian': 28, 'Australian': 47, 'Brazilian': 46,
    'British': 30, 'Caribbean': 31, 'Chinese': 7, 'European': 34, 'French': 35,
    'Fusion': 36, 'German': 37, 'Indian': 8, 'International': 9, 'Italian': 10,
    'Japanese': 11, 'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
    'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
}
b9 = list(b8.keys())
for category in b9:
    b10 = []
    b11 = b8[category]
    for city_name, b14, lng in zip(b2, b3, b4):
        b12 = (
            f"https:
            f"&b13 = {b11}&radius=25&metric=mi&limit=81&order=default"
            f"&b14 = {b14}&lng={lng}"
        )
        b7.get(b12)
        b15 = b7.page_source
        b16 = BeautifulSoup(b15, 'html.parser')
        b17 = b16.find("span", class_="total-results")
        if not b17:
            continue
        b18 = int(b17.text.strip())
        b19 = math.ceil(b18 / 81)
        for count in range(1, b19 + 1):
            if count > 1:
                b20 = f"{b12}&page={count}"
                b7.get(b20)
                b15 = b7.page_source
                b16 = BeautifulSoup(b15, 'html.parser')
            b21 = b16.find_all(attrs={"class": "js-venues venues__item"})
            for details in b21:
                b10.append(details["b10-id"] + "\n")
    b22 = f"category_{category}.csv"
    with open(b22, "w", b23 = "utf-8") as file:
        file.writelines(b10)
b7.quit()