from selenium import webdriver
from bs4 import BeautifulSoup as soup
import math
import pandas as pd
b1 = pd.read_csv("geo.csv", b22="ISO-8859-1")
b2 = b1.city
b3 = b1.lat
b4 = b1.lng
b5 = webdriver.FirefoxProfile()
b5.set_preference('permissions.default.stylesheet', 2)
b5.set_preference('permissions.default.image', 2)
b5.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
b6 = webdriver.Firefox(firefox_profile=b5)
b7 = {
    'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14,
    'Salad Bar': 20, 'Take Out': 24, 'American': 5, 'Asian': 28,
    'Australian': 47, 'Brazilian': 46, 'British': 30, 'Caribbean': 31,
    'Chinese': 7, 'European': 34, 'French': 35, 'Fusion': 36, 'German': 37,
    'Indian': 8, 'International': 9, 'Italian': 10, 'Japanese': 11,
    'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
    'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
}
b8 = list(b7.keys())
for category in b8:
    b9 = []
    for i in range(len(b2)):
        b10 = b2[i]
        b11 = b3[i]
        b12 = b4[i]
        b13 = "https:
        b14 = f"?&filters=vegan-vegetarian&ft={b7[category]}&radius=25&metric=mi&limit=81&order=default&lat={b11}&lng={b12}"
        b15 = b13 + b14
        b6.get(b15)
        b16 = b6.page_source
        b17 = soup(b16, 'html.parser')
        b18 = int(b17.find("span", {"class": "total-results"}).text.strip())
        b19 = math.ceil(b18 / 81)
        for count in range(1, b19 + 1):
            if count != 1:
                b15 = b13 + b14 + f"&page={count}"
                b6.get(b15)
                b16 = b6.page_source
                b17 = soup(b16, 'html.parser')
            for details in b17.findAll(b20 = {"class": "js-venues venues__item"}):
                b9.append(details["b9-id"] + "\n")
    b21 = f"category_{category}.csv"
    with open(b21, "w", b22 = "utf-8") as f:
        f.writelines(b9)
b6.quit()