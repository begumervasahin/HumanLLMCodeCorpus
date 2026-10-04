import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
output = open("rentpad_list.csv", "w+")
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
        response = requests.post(
            url="https:
            data=payload,
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = soup.find_all(itemprop="price")
        apartments = soup.find_all(itemprop="name")
        links = soup.find_all(itemprop="offers")
        for i, apartment in enumerate(apartments):
            if apartment.string is None:
                continue
            price = prices[i].string[1:].replace(",", "")
            link = links[i].find('a').get('href')
            print(f"{apartment.string}, {price}, {link}")
            output.write(f"{apartment.string},{price},{link}\n")
    except RequestException as e:
        print(f"Error fetching data from Rentpad: {e}")
scrape_rentpad("Mandaluyong")