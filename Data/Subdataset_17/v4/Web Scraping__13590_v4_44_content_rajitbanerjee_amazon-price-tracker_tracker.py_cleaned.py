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
    for price_id in json_data["price_id"]:
        try:
            data_dict["price"] = float(soup.find(id=price_id).get_text()[1:])
            break
        except:
            pass
    try:
        for savings_id in json_data["savings_id"]:
            try:
                savings = soup.find(id=savings_id).get_text()
                break
            except:
                pass
        data_dict["savings"] = savings.replace("Â£", "GBP ")
        start = data_dict["savings"].index("(")
        stop = data_dict["savings"].index("%")
        data_dict["per_savings"] = float(data_dict["savings"][start + 1: stop])
        print("Discount available:", data_dict["per_savings"], "%")
    except:
        print("No discount is currently available!")
        data_dict["savings"] = "\nNo savings at the moment."
        data_dict["per_savings"] = 0
    if data_dict["per_savings"] >= data_dict["discount"]:
        send_email(data_dict)
    else:
        helper.login(data_dict["username"], data_dict["password"])
        print("\nSorry, the product is currently not available at the desired price!")
        print("NAME:", data_dict["title"])
        print("CURRENT PRICE: GBP", data_dict["price"], "\n")
def send_email(data_dict):
    server = helper.login(data_dict["username"], data_dict["password"])
    subject = f"PRICE DROP: \"{data_dict['title'][:30]}...\" available now for GBP {data_dict['price']}"
    body = (f"The following product that you were interested in is now available at a discount!"
            f"\n\nName: {data_dict['title']}"
            f"\nCurrent price: GBP {data_dict['price']}"
            f"{data_dict['savings']}"
            f"\nCheck out this link:\n{data_dict['URL']}")
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(data_dict["username"], data_dict["username"], msg)
    print("...Email sent successfully!")
    server.quit()
