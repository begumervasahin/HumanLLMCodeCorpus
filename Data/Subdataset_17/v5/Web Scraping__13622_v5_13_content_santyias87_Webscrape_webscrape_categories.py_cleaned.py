from selenium import webdriver
from bs4 import BeautifulSoup as soup
import math
import pandas as pd
city_data = pd.read_csv("geo.csv", encoding="ISO-8859-1")
city_names = city_data['city']
city_lat = city_data['lat']
city_lng = city_data['lng']
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.stylesheet', 2)
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(firefox_profile=firefox_profile)
features = {
    'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14,
    'Salad Bar': 20, 'Take Out': 24, 'American': 5, 'Asian': 28,
    'Australian': 47, 'Brazilian': 46, 'British': 30, 'Caribbean': 31,
    'Chinese': 7, 'European': 34, 'French': 35, 'Fusion': 36, 'German': 37,
    'Indian': 8, 'International': 9, 'Italian': 10, 'Japanese': 11,
    'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
    'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
}
for category, feature_id in features.items():
    data = []
    for city_name, latitude, longitude in zip(city_names, city_lat, city_lng):
        base_url = "https:
        query_params = (
            f"?&filters=vegan-vegetarian&ft={feature_id}"
            f"&radius=25&metric=mi&limit=81&order=default"
            f"&lat={latitude}&lng={longitude}"
        )
        url = base_url + query_params
        driver.get(url)
        page_html = driver.page_source
        soup_page = soup(page_html, 'html.parser')
        results_count = int(soup_page.find("span", {"class": "total-results"}).text.strip())
        loop_count = math.ceil(results_count / 81)
        for page_number in range(1, loop_count + 1):
            if page_number > 1:
                url = base_url + query_params + f"&page={page_number}"
                driver.get(url)
                page_html = driver.page_source
                soup_page = soup(page_html, 'html.parser')
            for venue in soup_page.findAll(attrs={"class": "js-venues venues__item"}):
                data.append(venue["data-id"] + "\n")
    filename = f"category_{category}.csv"
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(data)
driver.quit()