import requests
from bs4 import BeautifulSoup
b1 = 'https:
def fonk1(url):
    try:
        b2 = requests.get(url)
        b2.raise_for_status()
        return b2.b6
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None
def fonk2(b6):
    if not b6:
        print("No b6 to parse.")
        return
    b3 = BeautifulSoup(b6, 'html.parser')
    b4 = b3.find_all('h2', class_='entry-title')
    for headline in b4:
        print(headline.get_text(b5 = True))
def fonk3():
    b6 = fonk1(b1)
    fonk2(b6)
if b7 = = "__main__":
    fonk3()