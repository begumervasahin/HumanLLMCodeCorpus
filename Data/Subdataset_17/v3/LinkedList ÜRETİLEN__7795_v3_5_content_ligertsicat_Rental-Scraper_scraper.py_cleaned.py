import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def scrape_rentpad(city):
    output_file = f"{city.lower()}_rentpad_list.csv"
    url = "https:
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
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except RequestException as e:
        print(f"Error fetching data: {e}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = [price.get_text(strip=True)[1:].replace(",", "") for price in soup.find_all(itemprop="price")]
    apartments = [apt.get_text(strip=True) for apt in soup.find_all(itemprop="name")]
    links = [link.find('a').get('href') for link in soup.find_all(itemprop="offers")]
    with open(output_file, "w") as output:
        for apartment, price, link in zip(apartments, prices, links):
            if not apartment:
                continue
            output.write(f"{apartment},{price},{link}\n")
            print(f"{apartment},{price},{link}")
if __name__ == "__main__":
    scrape_rentpad("Mandaluyong")