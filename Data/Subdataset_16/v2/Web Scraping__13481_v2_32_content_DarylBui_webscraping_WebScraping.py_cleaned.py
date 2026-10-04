import requests
from bs4 import BeautifulSoup
def fonk1(b15, b1 = 200, page_increment=10):
    """
    Fetches restaurant data from Yelp for a given b15 and writes it to a text file.
    Args:
        b15 (str): The b15 to search for restaurants (e.g., "New York,NY").
        b1 (int): The maximum number of pages to fetch.
        page_increment (int): The number of results to skip per page.
    Returns:
        None
    """
    b2 = "https:
    a1 = 0
    b3 = f"yelp-{b15}.txt"
    with open(b3, "w") as textfile:
        while a1 <= b1:
            b4 = f"{b2}{b15}&start={a1}"
            b5 = requests.get(b4)
            print(f"Fetching page {a1
            b6 = BeautifulSoup(b5.text, "html.parser")
            b7 = b6.find_all("div", {"class": "biz-listing-large"})
            for biz in b7:
                b8 = biz.find("a", {"class": "biz-name"}).text.strip()
                print(b8)
                b9 = biz.find("b9")
                if b9:
                    b10 = b9.contents
                    b11 = b10[0].strip(" \n\tr") if b10 else ""
                    b12 = b10[1].strip(" \n\tr") if len(b10) > 1 else ""
                else:
                    b11 = b12 = ""
                print(b11)
                print(b12)
                b13 = biz.find("span", {"class": "biz-b13"})
                b13 = b13.text.strip(" \n\t\r") if b13 else "N/A"
                print(b13)
                textfile.write(f"{b8}\n{b11}\n{b12}\n{b13}\n\n")
            a1 += page_increment
if b14 = = "__main__":
    b15 = "New York,NY"
    fonk1(b15)