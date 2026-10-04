import requests
from bs4 import BeautifulSoup
import json
import helper
def check_price(data_dict):
    headers = {"User-Agent": data_dict["user_agent"]}
    page = requests.get(data_dict["URL"], headers=headers)
    with open("details.json", "r") as json_file:
        json_data = json.load(json_file)
    soup = BeautifulSoup(page.content, "html.parser")
    data_dict["title"] = soup.find(id="productTitle").get_text().strip()
    data_dict["price"] = get_product_price(soup, json_data["price_id"])
    data_dict["savings"], data_dict["per_savings"] = get_discount_savings(soup, json_data["savings_id"])
    if data_dict["per_savings"] >= data_dict["discount"]:
        send_email(data_dict)
    else:
        notify_no_discount(data_dict)
def get_product_price(soup, price_ids):
    for price_id in price_ids:
        try:
            return float(soup.find(id=price_id).get_text()[1:])
        except:
            pass
    return None
def get_discount_savings(soup, savings_ids):
    savings = "No savings at the moment."
    per_savings = 0
    for savings_id in savings_ids:
        try:
            savings_text = soup.find(id=savings_id).get_text()
            savings_text = savings_text.replace("Â£", "GBP ")
            start = savings_text.index("(")
            stop = savings_text.index("%")
            per_savings = float(savings_text[start + 1: stop])
            return savings_text, per_savings
        except:
            pass
    return savings, per_savings
def send_email(data_dict):
    server = helper.login(data_dict["username"], data_dict["password"])
    subject = f"PRICE DROP: \"{data_dict['title'][:30]}...\" available now for GBP {data_dict['price']}"
    body = (
        f"The following product that you were interested in is now available at a discount!"
        f"\n\nName: {data_dict['title']}"
        f"\nCurrent price: GBP {data_dict['price']}"
        f"{data_dict['savings']}"
        f"\nCheck out this link:\n{data_dict['URL']}"
    )
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(data_dict["username"], data_dict["username"], msg)
    print("...Email sent successfully!")
    server.quit()
def notify_no_discount(data_dict):
    helper.login(data_dict["username"], data_dict["password"])
    print("\nSorry, the product is currently not available at the desired price!")
    print("NAME:", data_dict["title"])
    print("CURRENT PRICE: GBP", data_dict["price"], "\n")
