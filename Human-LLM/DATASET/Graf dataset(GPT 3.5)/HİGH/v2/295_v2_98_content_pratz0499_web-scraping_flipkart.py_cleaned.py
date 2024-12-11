from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
b1 = "https:
b2 = uReq(b1)
b3 = b2.read()
b2.close()
b4 = soup(b3, "html.parser")
b5 = b4.findAll("div", {"class": "_3O0U0u"})
b6 = "products.csv"
with open(b6, "w", b7 = "utf-8") as f:
    b8 = "Product_name,Pricing,Ratings\n"
    f.write(b8)
    for container in b5:
        b9 = container.find("div", {"class": "_4rR01T"}).text.strip()
        b10 = container.find("div", {"class": "_30jeq3 _1_WHN1"})
        b11 = b10.text.strip() if b10 else "N/A"
        b12 = container.find("div", {"class": "_3LWZlK"})
        b13 = b12.text.strip() if b12 else "N/A"
        print(b9.replace(",", "|") + "," + b11.replace(",", "") + "," + b13 + "\n")
        f.write(b9.replace(",", "|") + "," + b11.replace(",", "") + "," + b13 + "\n")