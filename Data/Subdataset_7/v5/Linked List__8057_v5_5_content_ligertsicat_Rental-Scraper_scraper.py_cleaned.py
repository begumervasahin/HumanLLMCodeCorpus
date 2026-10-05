import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
b1 = "https:
b2 = "rentpad_list.csv"
def fonk1(city):
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
        b4 = requests.post(url=b1, data=b3)
        b4.raise_for_status()
        b5 = BeautifulSoup(b4.text, 'b5.parser')
        b6 = b5.find_all(itemprop="price")
        b7 = b5.find_all(itemprop="name")
        b8 = b5.find_all(itemprop="offers")
        with open(b2, "w+") as output:
            for price, apartment, link in zip(b6, b7, b8):
                if apartment.string:
                    b9 = price.string[1:].replace(",", "")
                    b10 = apartment.string
                    b11 = link.find('a').get('href')
                    output.write(f"{b10},{b9},{b11}\n")
    except RequestException as e:
        print("Error during request:", e)
fonk1("Mandaluyong")