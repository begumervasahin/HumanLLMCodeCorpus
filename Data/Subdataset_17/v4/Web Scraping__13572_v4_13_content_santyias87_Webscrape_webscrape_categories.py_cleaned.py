from selenium import webdriver
from bs4 import BeautifulSoup as soup
import math
import pandas as pd
city_data = pd.read_csv("geo.csv", encoding="ISO-8859-1")
city_names = city_data.city
city_lat = city_data.lat
city_lng = city_data.lng
ffp = webdriver.FirefoxProfile()
ffp.set_preference('permissions.default.stylesheet', 2)
ffp.set_preference('permissions.default.image', 2)
ffp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(firefox_profile=ffp)
feature = {
    'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14,
    'Salad Bar': 20, 'Take Out': 24, 'American': 5, 'Asian': 28,
    'Australian': 47, 'Brazilian': 46, 'British': 30, 'Caribbean': 31,
    'Chinese': 7, 'European': 34, 'French': 35, 'Fusion': 36, 'German': 37,
    'Indian': 8, 'International': 9, 'Italian': 10, 'Japanese': 11,
    'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
    'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
}
categories = list(feature.keys())
for category in categories:
    data = []
    for i in range(len(city_names)):
        city_name = city_names[i]
        latitude = city_lat[i]
        longitude = city_lng[i]
        base_url = "https:
        query_params = f"?&filters=vegan-vegetarian&ft={feature[category]}&radius=25&metric=mi&limit=81&order=default&lat={latitude}&lng={longitude}"
        url = base_url + query_params
        driver.get(url)
        page_html = driver.page_source
        soup_page = soup(page_html, 'html.parser')
        results_count = int(soup_page.find("span", {"class": "total-results"}).text.strip())
        loop_count = math.ceil(results_count / 81)
        for count in range(1, loop_count + 1):
            if count != 1:
                url = base_url + query_params + f"&page={count}"
                driver.get(url)
                page_html = driver.page_source
                soup_page = soup(page_html, 'html.parser')
            for details in soup_page.findAll(attrs={"class": "js-venues venues__item"}):
                data.append(details["data-id"] + "\n")
    filename = f"category_{category}.csv"
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(data)
driver.quit()