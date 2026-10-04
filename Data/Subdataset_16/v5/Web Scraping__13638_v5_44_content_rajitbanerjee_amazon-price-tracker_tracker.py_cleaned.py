import requests
from bs4 import BeautifulSoup
import json
import helper
def fonk1(data_dict):
    b1 = {"User-Agent": data_dict["user_agent"]}
    b2 = requests.get(data_dict["URL"], b1=b1)
    with open("details.json", "r") as json_file:
        b3 = json.load(json_file)
    b4 = BeautifulSoup(b2.content, "html.parser")
    data_dict["title"] = b4.find(b5 = "productTitle").get_text().strip()
    data_dict["price"] = fonk2(b4, b3["price_id"])
    data_dict["b6"], data_dict["a1"] = fonk3(b4, b3["savings_id"])
    if data_dict["a1"] >= data_dict["discount"]:
        fonk4(data_dict)
    else:
        fonk5(data_dict)
def fonk2(b4, price_ids):
    for price_id in price_ids:
        try:
            return float(b4.find(b5 = price_id).get_text()[1:])
        except:
            pass
    return None
def fonk3(b4, savings_ids):
    b6 = "No b6 at the moment."
    a1 = 0
    for savings_id in savings_ids:
        try:
            b7 = b4.find(b5=savings_id).get_text()
            b7 = b7.replace("Â£", "GBP ")
            b8 = b7.index("(")
            b9 = b7.index("%")
            a1 = float(b7[b8 + 1: b9])
            return b7, a1
        except:
            pass
    return b6, a1
def fonk4(data_dict):
    b10 = helper.login(data_dict["username"], data_dict["password"])
    b11 = f"PRICE DROP: \"{data_dict['title'][:30]}...\" available now for GBP {data_dict['price']}"
    b12 = (
        f"The following product that you were interested in is now available at a discount!"
        f"\n\nName: {data_dict['title']}"
        f"\nCurrent price: GBP {data_dict['price']}"
        f"{data_dict['b6']}"
        f"\nCheck out this link:\n{data_dict['URL']}"
    )
    b13 = f"Subject: {b11}\n\n{b12}"
    b10.sendmail(data_dict["username"], data_dict["username"], b13)
    print("...Email sent successfully!")
    b10.quit()
def fonk5(data_dict):
    helper.login(data_dict["username"], data_dict["password"])
    print("\nSorry, the product is currently not available at the desired price!")
    print("NAME:", data_dict["title"])
    print("CURRENT PRICE: GBP", data_dict["price"], "\n")
