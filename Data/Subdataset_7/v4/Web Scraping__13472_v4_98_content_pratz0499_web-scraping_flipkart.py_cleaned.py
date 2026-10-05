from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
b1 = "https:
b2 = uReq(b1)
b3 = b2.read()
b2.close()
b4 = soup(b3, "html.parser")
b5 = b4.findAll("div", {"class": "_3O0U0u"})
b6 = "products.csv"
b7 = open(b6, "w")
b8 = "Product_name,Pricing,Ratings\n"
b7.write(b8)
for container in b5:
    b9 = container.div.img["alt"]
    b10 = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    b11 = b10[0].text.strip()
    b12 = "".join(b11.split(","))
    b13 = b12.split("â¹")
    b14 = "Rs." + b13[1]
    b15 = b14.split("E")
    b16 = b15[0]
    b17 = container.findAll("div", {"class": "hGSR34"})
    b18 = b17[0].text
    b19 = b18.split(" ")
    b20 = b19[0]
    b7.write(b9.replace(",", "|") + "," + b16 + "," + b20 + "\n")
    print(b9.replace(",", "|") + "," + b16 + "," + b20 + "\n")
b7.close()