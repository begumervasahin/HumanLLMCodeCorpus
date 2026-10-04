import math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
def setup_driver():
    options = Options()
    options.set_preference('permissions.default.stylesheet', 2)
    options.set_preference('permissions.default.image', 2)
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    options.headless = True
    return webdriver.Firefox(options=options)
def get_city_data(filepath):
    return pd.read_csv(filepath, encoding="ISO-8859-1")
def get_total_results(soup_page):
    results_span = soup_page.find("span", class_="total-results")
    return int(results_span.text.strip()) if results_span else 0
def fetch_data_for_category(driver, category, feature_code, cities):
    data = []
    for city_name, lat, lng in zip(cities['city'], cities['lat'], cities['lng']):
        base_url = (
            f"https:
            f"&ft={feature_code}&radius=25&metric=mi&limit=81&order=default"
            f"&lat={lat}&lng={lng}"
        )
        driver.get(base_url)
        page_html = driver.page_source
        soup_page = BeautifulSoup(page_html, 'html.parser')
        results_count = get_total_results(soup_page)
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
    return data
def save_data_to_csv(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(data)
def main():
    feature_mapping = {
        'Juice Bar': 21, 'Macrobiotic': 12, 'Organic': 13, 'Raw food': 14, 'Salad Bar': 20,
        'Take Out': 24, 'American': 5, 'Asian': 28, 'Australian': 47, 'Brazilian': 46,
        'British': 30, 'Caribbean': 31, 'Chinese': 7, 'European': 34, 'French': 35,
        'Fusion': 36, 'German': 37, 'Indian': 8, 'International': 9, 'Italian': 10,
        'Japanese': 11, 'Latin': 45, 'Mediterranean': 18, 'Mexican': 25, 'Middle Eastern': 39,
        'Spanish': 40, 'Taiwanese': 41, 'Thai': 15, 'Vietnamese': 42, 'Western': 16
    }
    driver = setup_driver()
    city_data = get_city_data("geo.csv")
    for category, feature_code in feature_mapping.items():
        data = fetch_data_for_category(driver, category, feature_code, city_data)
        filename = f"category_{category}.csv"
        save_data_to_csv(data, filename)
    driver.quit()
if __name__ == "__main__":
    main()