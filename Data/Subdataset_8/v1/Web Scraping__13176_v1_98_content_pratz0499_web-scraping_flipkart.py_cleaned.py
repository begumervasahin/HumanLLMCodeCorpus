from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = "https:
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
filename = "products.csv"
with open(filename, "w", encoding="utf-8") as f:
    headers = "Product_name,Pricing,Ratings\n"
    f.write(headers)
    for container in containers:
        product_name = container.find("div", {"class": "_4rR01T"}).text.strip()
        price_container = container.find("div", {"class": "_30jeq3 _1_WHN1"})
        price = price_container.text.strip() if price_container else "N/A"
        rating_container = container.find("div", {"class": "_3LWZlK"})
        rating = rating_container.text.strip() if rating_container else "N/A"
        print(product_name.replace(",", "|") + "," + price.replace(",", "") + "," + rating + "\n")
        f.write(product_name.replace(",", "|") + "," + price.replace(",", "") + "," + rating + "\n")