from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = "https:
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
filename = "products.csv"
f = open(filename, "w")
headers = "Product_name,Pricing,Ratings\n"
f.write(headers)
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()
    trim_price = "".join(price.split(","))
    rm_rupee = trim_price.split("â¹")
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split("E")
    final_price = split_price[0]
    rating_container = container.findAll("div", {"class": "hGSR34"})
    rating = rating_container[0].text
    split_rating = rating.split(" ")
    final_rating = split_rating[0]
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
f.close()