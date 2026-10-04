import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def fonk1(city, output_file):
    b1 = {
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
        b2 = requests.post(
            b3 = "https:
            b4 = b1,
        )
        b2.raise_for_status()
        b5 = BeautifulSoup(b2.text, 'html.parser')
        b6 = b5.find_all(itemprop="b10")
        b7 = b5.find_all(itemprop="name")
        b8 = b5.find_all(itemprop="offers")
        with open(output_file, "w", b9 = 'utf-8') as file:
            file.write("Apartment Name,Price,Link\n")
            for i, apartment in enumerate(b7):
                if apartment.string is None:
                    continue
                b10 = b6[i].string[1:].replace(",", "")
                b11 = b8[i].find('a').get('href')
                print(f"{apartment.string}, {b10}, {b11}")
                file.write(f"{apartment.string},{b10},{b11}\n")
    except RequestException as e:
        print(f"Error fetching b4 from Rentpad: {e}")
if b12 = = "__main__":
    fonk1("Mandaluyong", "rentpad_list.csv")