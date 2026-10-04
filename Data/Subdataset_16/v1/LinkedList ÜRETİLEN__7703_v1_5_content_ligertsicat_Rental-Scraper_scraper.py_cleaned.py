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
    b5 = BeautifulSoup(b4.text, 'b5.parser')
    b6 = b5.find_all(itemprop="b9")
    b7 = b5.find_all(itemprop="name")
    b8 = b5.find_all(itemprop="offers")
    with open(b1, "w") as output:
        for i, apartment in enumerate(b7):
            if apartment.string is None:
                continue
            b9 = b6[i].string[1:].replace(",", "")
            b10 = b8[i].find('a').get('href')
            output.write(f"{apartment.string},{b9},{b10}\n")
            print(f"{apartment.string},{b9},{b10}")
if b11 = = "__main__":
    fonk1("Mandaluyong")