from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
b1 = "https:
with uReq(b1) as uClient:
    b2 = uClient.read()
b3 = soup(b2, "html.parser")
b4 = b3.findAll("div", class_="_3O0U0u")
b5 = "products.csv"
with open(b5, "w", b6 = "utf-8") as f:
    b7 = "Product_name,Pricing,Ratings\n"
    f.write(b7)
    for container in b4:
        b8 = container.find("div", class_="_4rR01T").text.strip()
        b9 = container.find("div", class_="_30jeq3 _1_WHN1")
        b10 = b9.text.strip() if b9 else "N/A"
        b11 = container.find("div", class_="_3LWZlK")
        b12 = b11.text.strip() if b11 else "N/A"
        print(f"{b8.replace(',', '|')},{b10.replace(',', '')},{b12}\n")
        f.write(f"{b8.replace(',', '|')},{b10.replace(',', '')},{b12}\n")