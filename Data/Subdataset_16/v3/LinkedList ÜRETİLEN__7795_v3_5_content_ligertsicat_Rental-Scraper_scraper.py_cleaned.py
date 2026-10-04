import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def fonk1(city):
    b1 = f"{city.lower()}_rentpad_list.csv"
    b2 = "https:
    b3 = {
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
        b4 = requests.post(b2, json=b3)
        b4.raise_for_status()
    except RequestException as e:
        print(f"Error fetching data: {e}")
        return
    b5 = BeautifulSoup(b4.text, 'html.parser')
    b6 = [price.get_text(strip=True)[1:].replace(",", "") for price in b5.find_all(itemprop="price")]
    b7 = [apt.get_text(strip=True) for apt in b5.find_all(itemprop="name")]
    b8 = [link.find('a').get('href') for link in b5.find_all(itemprop="offers")]
    with open(b1, "w") as output:
        for apartment, price, link in zip(b7, b6, b8):
            if not apartment:
                continue
            output.write(f"{apartment},{price},{link}\n")
            print(f"{apartment},{price},{link}")
if b9 = = "__main__":
    fonk1("Mandaluyong")