import requests
import webbrowser
import random
from bs4 import BeautifulSoup
def fetch_and_parse(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")
def display_categories(categories):
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category.text}")
def get_user_choice(message, options):
    while True:
        try:
            choice = int(input(message))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def display_products(products):
    count = 1
    color_code = str(random.randint(31, 37))
    product_links = []
    for product in products:
        title = product.find("a").get("title")
        price = product.find("a").find("span").text
        description = product.find("div", class_="_27VV").text
        print(f"\033[1;{color_code};40m{count}. {title}")
        print(f"  Price: {price}")
        print(f" {description}")
        product_links.append("https:
        count += 1
    return product_links
def main():
    homepage_url = "https:
    homepage_soup = fetch_and_parse(homepage_url)
    print("***********Welcome to {}*************".format(homepage_soup.title.text))
    main_div = homepage_soup.find("div", class_="_1_Nn")
    all_categories = main_div.find_all("a")
    display_categories(all_categories)
    selected_category = get_user_choice("Which category do you want to explore? Enter the corresponding number: ", all_categories)
    selected_category_url = "https:
    category_soup = fetch_and_parse(selected_category_url)
    main_div_products = category_soup.find("div", class_="_3RA-")
    product_divs = main_div_products.find_all("div", class_="_1fje")
    product_links = display_products(product_divs)
    selected_product = get_user_choice("Which product do you want to view? Enter the corresponding number: ", product_divs)
    webbrowser.open_new_tab(product_links[selected_product - 1])
if __name__ == "__main__":
    main()