import requests
from bs4 import BeautifulSoup
b1 = 'https:
def fonk1(url):
    try:
        b2 = requests.get(url)
        b2.raise_for_status()
        return b2.b5
    except requests.RequestException as e:
        print(f"Error fetching b5 from {url}: {e}")
        return None
def fonk2(b5):
    b3 = BeautifulSoup(b5, 'html.parser')
    b4 = [headline.text.strip() for headline in b3.find_all('h2', class_='entry-title')]
    return b4
def fonk3(b4):
    if b4:
        print("Headlines:")
        for headline in b4:
            print(f"- {headline}")
    else:
        print("No b4 found.")
def fonk4():
    b5 = fonk1(b1)
    if b5:
        b4 = fonk2(b5)
        fonk3(b4)
    else:
        print("Failed to retrieve or parse news b5.")
if b6 = = "__main__":
    fonk4()