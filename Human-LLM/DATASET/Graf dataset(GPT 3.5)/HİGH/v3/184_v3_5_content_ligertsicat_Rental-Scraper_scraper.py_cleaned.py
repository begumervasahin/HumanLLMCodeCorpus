import requests
from bs4 import BeautifulSoup
b1 = "rentpad_list.csv"
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
        b3 = requests.post("https:
        b3.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return
    b4 = BeautifulSoup(b3.text, 'b4.parser')
    b5 = b4.find_all(itemprop="b8")
    b6 = b4.find_all(itemprop="name")
    b7 = b4.find_all(itemprop="offers")
    with open(b1, "w+") as output:
        a1 = 0
        for apartment in b6:
            if apartment.string is None:
                continue
            b8 = b5[a1].string[1:].replace(",", "")
            b9 = b7[a1].find('a').get('href')
            output.write(f"{apartment.string},{b8},{b9}\n")
            print(f"{apartment.string},{b8},{b9}")
            a1 += 1
fonk1("Mandaluyong")