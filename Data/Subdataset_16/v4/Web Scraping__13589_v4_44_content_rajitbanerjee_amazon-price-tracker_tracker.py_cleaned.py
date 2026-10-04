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
    for price_id in b3["price_id"]:
        try:
            data_dict["price"] = float(b4.find(b5 = price_id).get_text()[1:])
            break
        except:
            pass
    try:
        for savings_id in b3["savings_id"]:
            try:
                b6 = b4.find(b5=savings_id).get_text()
                break
            except:
                pass
        data_dict["b6"] = b6.replace("Â£", "GBP ")
        b7 = data_dict["b6"].index("(")
        b8 = data_dict["b6"].index("%")
        data_dict["per_savings"] = float(data_dict["b6"][b7 + 1: b8])
        print("Discount available:", data_dict["per_savings"], "%")
    except:
        print("No discount is currently available!")
        data_dict["b6"] = "\nNo b6 at the moment."
        data_dict["per_savings"] = 0
    if data_dict["per_savings"] >= data_dict["discount"]:
        fonk2(data_dict)
    else:
        helper.login(data_dict["username"], data_dict["password"])
        print("\nSorry, the product is currently not available at the desired price!")
        print("NAME:", data_dict["title"])
        print("CURRENT PRICE: GBP", data_dict["price"], "\n")
def fonk2(data_dict):
    b9 = helper.login(data_dict["username"], data_dict["password"])
    b10 = f"PRICE DROP: \"{data_dict['title'][:30]}...\" available now for GBP {data_dict['price']}"
    b11 = (f"The following product that you were interested in is now available at a discount!"
            f"\n\nName: {data_dict['title']}"
            f"\nCurrent price: GBP {data_dict['price']}"
            f"{data_dict['b6']}"
            f"\nCheck out this link:\n{data_dict['URL']}")
    b12 = f"Subject: {b10}\n\n{b11}"
    b9.sendmail(data_dict["username"], data_dict["username"], b12)
    print("...Email sent successfully!")
    b9.quit()
