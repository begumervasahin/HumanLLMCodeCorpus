import string
import time
import requests
from bs4 import BeautifulSoup
import helper
import json
def fonk1(data_dict):
    b1 = {}
    b1["User-Agent"] = data_dict["user_agent"]
    b2 = requests.get(data_dict["URL"], b1=b1)
    b3 = open("details.json", "r+")
    b4 = json.load(b3)
    b5 = BeautifulSoup(b2.content, "html.parser")
    data_dict["title"] = b5.find(b6 = "productTitle").get_text().strip()
    for b6 in b4["price_id"]:
        try:
            data_dict["price"] = float(
                b5.find(b6 = b6).get_text()[1:])
            break
        except:
            pass
    try:
        for b6 in b4["savings_id"]:
            try:
                b7 = b5.find(b6=b6).get_text()
                break
            except:
                pass
        data_dict["b7"] = b7.replace("Â£", "GBP ")
        b8 = data_dict["b7"].index("(")
        b9 = data_dict["b7"].index("%")
        data_dict["per_savings"] = float(data_dict["b7"][b8 + 1: b9])
        print("Discount available:", data_dict["per_savings"], "%")
    except:
        print("No discount is currently available!")
        data_dict["b7"] = "\nNo b7 at the moment."
        data_dict["per_savings"] = 0
    if data_dict["per_savings"] >= data_dict["discount"]:
        fonk2(data_dict)
    else:
        helper.login(data_dict["username"], data_dict["password"])
        print("\nSorry, the product is currently not available at the desired price!")
        print("NAME:", data_dict["title"])
        print("CURRENT PRICE: GBP", data_dict["price"], "\n")
    b3.close()
def fonk2(data_dict):
    b10 = helper.login(data_dict["username"], data_dict["password"])
    b11 = "PRICE DROP: \"" + \
        data_dict["title"][:30] + "...\" available now for GBP " + \
        str(data_dict["price"])
    b12 = "The following product that you were interested in is now available at a discount!" +\
        "\n\nName: " + data_dict["title"] + \
        "\nCurrent price: GBP " + str(data_dict["price"]) + \
        data_dict["b7"] + \
        "\nCheck out this link:\n" + data_dict["URL"]
    b13 = "Subject: {0}\n\n{1}".format(b11, b12)
    b10.sendmail(data_dict["username"], data_dict["username"], b13)
    print("...Email sent successfully!")
    b10.quit()
    exit()