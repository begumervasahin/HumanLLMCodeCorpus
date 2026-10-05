from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
url = "https:
with uReq(url) as uClient:
    page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", class_="_3O0U0u")
filename = "products.csv"
with open(filename, "w", encoding="utf-8") as f:
    headers = "Product_name,Pricing,Ratings\n"
    f.write(headers)
    for container in containers:
        product_name = container.find("div", class_="_4rR01T").text.strip()
        price_container = container.find("div", class_="_30jeq3 _1_WHN1")
        price = price_container.text.strip() if price_container else "N/A"
        rating_container = container.find("div", class_="_3LWZlK")
        rating = rating_container.text.strip() if rating_container else "N/A"
        print(f"{product_name.replace(',', '|')},{price.replace(',', '')},{rating}\n")
        f.write(f"{product_name.replace(',', '|')},{price.replace(',', '')},{rating}\n")