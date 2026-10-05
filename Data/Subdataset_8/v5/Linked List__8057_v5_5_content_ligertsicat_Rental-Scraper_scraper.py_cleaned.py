import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
RENTPAD_URL = "https:
CSV_FILE = "rentpad_list.csv"
def scrape_rentpad(city):
    payload = {
        "a": "31",
        "cityName": city,
        "propertyTypeIDs": [2, 3, 5],
        "furnishTypeIDs": [1, 2, 3],
        "placeIDs": [],
        "statusTypeIDs": [],
        "amenityIDs": [],
        "longMonthRateLow": "0",
        "longMonthRateHigh": "30,000",
        "numBedroomsLow": "0",
        "numBedroomsHigh": "0",
        "itemsPerPage": "1000",
        "pageNumber": "1",
        "lengthOfStay": "",
        "ham": "ham"
    }
    try:
        response = requests.post(url=RENTPAD_URL, data=payload)
        response.raise_for_status()
        html = BeautifulSoup(response.text, 'html.parser')
        prices = html.find_all(itemprop="price")
        apartments = html.find_all(itemprop="name")
        links = html.find_all(itemprop="offers")
        with open(CSV_FILE, "w+") as output:
            for price, apartment, link in zip(prices, apartments, links):
                if apartment.string:
                    price_value = price.string[1:].replace(",", "")
                    apartment_name = apartment.string
                    apartment_link = link.find('a').get('href')
                    output.write(f"{apartment_name},{price_value},{apartment_link}\n")
    except RequestException as e:
        print("Error during request:", e)
scrape_rentpad("Mandaluyong")