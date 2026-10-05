import requests
from bs4 import BeautifulSoup
import pprint
def get_mobile_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    main_divs = soup.find_all("div", class_="_1UoZlX")
    mobiles = []
    for div in main_divs:
        mobile_info = {}
        mobile_info["Name"] = div.find("div", class_="_3wU53n").text
        mobile_info["Price"] = div.find("div", class_="_1vC4OE _2rQ-NK").text
        mobile_rating = div.find("div", class_="hGSR34")
        if mobile_rating:
            mobile_info["Rating"] = mobile_rating.text
        details = div.find_all("li", class_="tVe95H")
        for detail in details:
            key, value = detail.text.split(": ")
            mobile_info[key] = value
        mobiles.append(mobile_info)
    return mobiles
def main():
    user_input = input("Enter page number: ")
    url = f"https:
    mobiles = get_mobile_info(url)
    pprint.pprint(mobiles)
if __name__ == "__main__":
    main()