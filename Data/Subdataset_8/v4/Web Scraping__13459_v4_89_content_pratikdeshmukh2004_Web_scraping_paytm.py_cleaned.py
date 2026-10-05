
import requests
import webbrowser
import random
from bs4 import BeautifulSoup
url = requests.get("https:
soup = BeautifulSoup(url.text, "lxml")
print("***********Welcome to {}*************".format(soup.title.text))
main_div = soup.find("div", class_="_1_Nn")
all_categories = main_div.find_all("a")
for idx, category in enumerate(all_categories, start=1):
    print(idx, category.text)
selected_category = input("Which category do you want to explore (enter the corresponding number): ")
selected_category_url = "https:
url2 = requests.get(selected_category_url)
soup2 = BeautifulSoup(url2.text, "lxml")
main_div_products = soup2.find("div", class_="_3RA-")
product_divs = main_div_products.find_all("div", class_="_1fje")
count = 1
product_links = []
color_code = str(random.randint(31, 37))
for product_div in product_divs:
    product_info = product_div.find_all("div", class_="_2i1r")
    for info in product_info:
        print("\033[1;{};40m".format(color_code) + str(count) + " " + info.find("a").get("title"))
        count += 1
        price = info.find("a").find("span")
        print("  Price: " + price.text)
        print(" " + info.find("div", class_="_27VV").text)
        product_links.append("https:
selected_product = int(input("Which product do you want to view (enter the corresponding number): "))
webbrowser.open_new_tab(product_links[selected_product - 1])