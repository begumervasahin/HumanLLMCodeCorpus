from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
url = "https:
with uReq(url) as uClient:
    page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div", class_="_3O0U0u")
filename = "products.csv"
with open(filename, "w") as f:
    headers = "Product_name,Pricing,Ratings\n"
    f.write(headers)
    for container in containers:
        product_name = container.div.img["alt"]
        price_container = container.find_all("div", class_="col col-5-12 _2o7WAb")
        price = price_container[0].text.strip()
        final_price = "Rs." + price.split("â¹")[1].split("E")[0].replace(",", "")
        rating_container = container.find_all("div", class_="hGSR34")
        final_rating = rating_container[0].text.split(" ")[0]
        f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
        print(product_name.replace(",", "|") + "," + final_price + "," + final_rating)