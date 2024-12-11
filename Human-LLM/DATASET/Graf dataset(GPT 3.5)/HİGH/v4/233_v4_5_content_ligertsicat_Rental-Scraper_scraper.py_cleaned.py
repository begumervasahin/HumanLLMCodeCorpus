import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
b1 = open("rentpad_list.csv", "w+")
def fonk1(city):
    b2 = {
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
        b3 = requests.post(
            b4 = "https:
            b5 = b2,
        )
        b6 = BeautifulSoup(b3.text, 'b6.parser')
        b7 = b6.find_all(itemprop="b10")
        b8 = b6.find_all(itemprop="name")
        b9 = b6.find_all(itemprop="offers")
        a1 = 0
        for apartment in b8:
            if apartment.string is None:
                continue
            b10 = b7[a1].string[1:].replace(",", "")
            b11 = b9[a1].find('a').get('href')
            b1.write(apartment.string + "," + b10 + "," + b11 + "\n")
            a1 += 1
    except RequestException as e:
        print("Error during request:", e)
fonk1("Mandaluyong")
b1.close()