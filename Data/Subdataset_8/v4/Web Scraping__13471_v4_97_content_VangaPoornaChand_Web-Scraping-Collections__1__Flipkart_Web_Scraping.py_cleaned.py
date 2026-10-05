error")
from bs4 import BeautifulSoup
import requests
import csv
import os
def search_flipkart(product, pages):
    search_query = "/search?q=" + product + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
    file_name = f"Flipkart Scraping on {product}.csv"
    if os.path.exists(file_name):
        print("You have already searched for this...\nDeleting your previous results...")
        os.remove(file_name)
    for page_num in range(pages):
        try:
            with open(file_name, "a", newline='', encoding='utf-8') as file:
                csv_file = csv.writer(file)
                if page_num == 0:
                    csv_file.writerow(["TITLE", "Price", "Rating"])
                url = "https:
                print("Working on Page No :", page_num + 1)
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                products = soup.find_all(class_="_1UoZlX")
                for product in products:
                    title = product.find(class_='_3wU53n')
                    price = product.find(class_="_1vC4OE _2rQ-NK")
                    rating = product.find(class_="hGSR34")
                    rating = "No Rating" if rating is None else rating.text
                    csv_file.writerow([title.text.strip(), price.text[1:], rating.strip()])
                next_page_link = soup.find_all(class_="_3fVaIS")[-1].get("href")
                search_query = next_page_link
        except IndexError:
            print("Out Of Pages for your search!!!")
            break
        except Exception as e:
            print("An error occurred:", e)
            print("One Item Skipped Due to an internal error")
if __name__ == "__main__":
    product = input("Enter product you want to search: ")
    pages = int(input("Enter number of pages: "))
    search_flipkart(product, pages)