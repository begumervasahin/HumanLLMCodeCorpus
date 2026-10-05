import requests
from bs4 import BeautifulSoup
import pprint
def fetch_mobiles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    mobile_containers = soup.find_all("div", class_="_1UoZlX")
    mobiles = []
    for container in mobile_containers:
        mobile_info = {}
        mobile_info["Name"] = container.find("div", class_="_3wU53n").text
        mobile_info["Price"] = container.find("div", class_="_1vC4OE _2rQ-NK").text
        rating = container.find("div", class_="hGSR34")
        if rating:
            mobile_info["Rating"] = rating.text
        details = container.find_all("li", class_="tVe95H")
        for detail in details:
            key, value = detail.text.split(": ")
            mobile_info[key] = value
        mobiles.append(mobile_info)
    return mobiles
def main():
    user_input = input("Enter page number: ")
    url = f"https:
    mobiles = fetch_mobiles(url)
    pprint.pprint(mobiles)
if __name__ == "__main__":
    main()