import requests
from bs4 import BeautifulSoup
output_file = "rentpad_list.csv"
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
        response = requests.post("https:
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return
    html = BeautifulSoup(response.text, 'html.parser')
    prices = html.find_all(itemprop="price")
    apartments = html.find_all(itemprop="name")
    links = html.find_all(itemprop="offers")
    with open(output_file, "w+") as output:
        i = 0
        for apartment in apartments:
            if apartment.string is None:
                continue
            price = prices[i].string[1:].replace(",", "")
            link = links[i].find('a').get('href')
            output.write(f"{apartment.string},{price},{link}\n")
            print(f"{apartment.string},{price},{link}")
            i += 1
scrape_rentpad("Mandaluyong")