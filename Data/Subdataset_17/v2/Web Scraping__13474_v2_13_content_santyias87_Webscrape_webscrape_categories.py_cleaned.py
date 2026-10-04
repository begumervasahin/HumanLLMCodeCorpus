import math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
city_data = pd.read_csv("geo.csv", encoding="ISO-8859-1")
city_names = city_data['city']
city_lat = city_data['lat']
city_lng = city_data['lng']
options = Options()
options.set_preference('permissions.default.stylesheet', 2)
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
options.headless = True
driver = webdriver.Firefox(options=options)
feature_mapping = {
    'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14, 'Salad Bar': 20,
    'Take Out': 24, 'American': 5, 'Asian': 28, 'Australian': 47, 'Brazilian': 46,
    'British': 30, 'Caribbean': 31, 'Chinese': 7, 'European': 34, 'French': 35,
    'Fusion': 36, 'German': 37, 'Indian': 8, 'International': 9, 'Italian': 10,
    'Japanese': 11, 'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
    'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
}
categories = list(feature_mapping.keys())
for category in categories:
    data = []
    feature_code = feature_mapping[category]
    for city_name, lat, lng in zip(city_names, city_lat, city_lng):
        base_url = (
            f"https:
            f"&ft={feature_code}&radius=25&metric=mi&limit=81&order=default"
            f"&lat={lat}&lng={lng}"
        )
        driver.get(base_url)
        page_html = driver.page_source
        soup_page = BeautifulSoup(page_html, 'html.parser')
        results_span = soup_page.find("span", class_="total-results")
        if not results_span:
            continue
        results_count = int(results_span.text.strip())
        loop_count = math.ceil(results_count / 81)
        for count in range(1, loop_count + 1):
            if count > 1:
                paginated_url = f"{base_url}&page={count}"
                driver.get(paginated_url)
                page_html = driver.page_source
                soup_page = BeautifulSoup(page_html, 'html.parser')
            venue_items = soup_page.find_all(attrs={"class": "js-venues venues__item"})
            for details in venue_items:
                data.append(details["data-id"] + "\n")
    filename = f"category_{category}.csv"
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(data)
driver.quit()