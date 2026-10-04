import requests
from bs4 import BeautifulSoup
def fonk1(b15, b1 = 200, page_increment=10):
    b2 = "https:
    a1 = 0
    b3 = f"yelp-{b15}.txt"
    with open(b3, "w") as textfile:
        while a1 <= b1:
            b4 = b2 + b15 + "&start=" + str(a1)
            b5 = requests.get(b4)
            print(f"Fetching page {a1
            b6 = BeautifulSoup(b5.text, "html.parser")
            b7 = b6.findAll("div", {"class": "biz-listing-large"})
            for biz in b7:
                b8 = biz.findAll("a", {"class": "biz-name"})[0].text.strip()
                print(b8)
                try:
                    b9 = biz.findAll("b9")[0].contents
                    b10 = ""
                    b11 = ""
                    for item in b9:
                        if "br" in str(item):
                            b11 += item.getText().strip(" \n\tr")
                        else:
                            b10 = item.strip(" \n\tr")
                    print(b10)
                    print(b11)
                except:
                    b10 = ""
                    b11 = ""
                try:
                    b12 = biz.findAll("span", {"class": "biz-b12"})[0].getText().strip(" \n\t\r")
                except:
                    b12 = "N/A"
                print(b12)
                b13 = f"{b8}\n{b10}\n{b11}\n{b12}\n\n"
                textfile.write(b13)
            a1 += page_increment
if b14 = = "__main__":
    b15 = "New York,NY"
    fonk1(b15)