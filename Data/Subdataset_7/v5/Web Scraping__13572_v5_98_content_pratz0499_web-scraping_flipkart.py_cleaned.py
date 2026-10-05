from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
b1 = "https:
with uReq(b1) as uClient:
    b2 = uClient.read()
b3 = soup(b2, "html.parser")
b4 = b3.find_all("div", class_="_3O0U0u")
b5 = "products.csv"
with open(b5, "w") as f:
    b6 = "Product_name,Pricing,Ratings\n"
    f.write(b6)
    for container in b4:
        b7 = container.div.img["alt"]
        b8 = container.find_all("div", class_="col col-5-12 _2o7WAb")
        b9 = b8[0].text.strip()
        b10 = "Rs." + b9.split("â¹")[1].split("E")[0].replace(",", "")
        b11 = container.find_all("div", class_="hGSR34")
        b12 = b11[0].text.split(" ")[0]
        f.write(b7.replace(",", "|") + "," + b10 + "," + b12 + "\n")
        print(b7.replace(",", "|") + "," + b10 + "," + b12)