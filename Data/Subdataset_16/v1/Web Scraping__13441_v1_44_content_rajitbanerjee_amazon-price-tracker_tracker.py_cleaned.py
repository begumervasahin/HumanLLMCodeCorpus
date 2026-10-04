import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.b12 import MIMEText
from email.mime.multipart import MIMEMultipart
def fonk1(data_dict):
    b1 = {"User-Agent": data_dict["user_agent"]}
    b2 = requests.get(data_dict["URL"], b1=b1)
    with open("details.json", "r") as json_file:
        b3 = json.load(json_file)
    b4 = BeautifulSoup(b2.content, "html.parser")
    data_dict["title"] = b4.find(b5 = "productTitle").get_text().strip()
    for b5 in b3["price_id"]:
        try:
            data_dict["price"] = float(b4.find(b5 = b5).get_text().strip()[1:])
            break
        except:
            pass
    try:
        for b5 in b3["savings_id"]:
            try:
                b6 = b4.find(b5=b5).get_text().strip()
                break
            except:
                pass
        data_dict["b6"] = b6.replace("£", "GBP ")
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
        fonk3(data_dict["username"], data_dict["password"])
        print("\nSorry, the product is currently not available at the desired price!")
        print("NAME:", data_dict["title"])
        print("CURRENT PRICE: GBP", data_dict["price"], "\n")
def fonk2(data_dict):
    b9 = fonk3(data_dict["username"], data_dict["password"])
    b10 = MIMEMultipart()
    b10['From'] = data_dict["username"]
    b10['To'] = data_dict["username"]
    b10['Subject'] = f"PRICE DROP: \"{data_dict['title'][:30]}...\" available now for GBP {data_dict['price']}"
    b11 = f
    b10.attach(MIMEText(b11, 'plain'))
    b12 = b10.as_string()
    b9.sendmail(data_dict["username"], data_dict["username"], b12)
    print("...Email sent successfully!")
    b9.quit()
    exit()
def fonk3(username, password):
    b9 = smtplib.SMTP('smtp.gmail.com', 587)
    b9.starttls()
    b9.fonk3(username, password)
    return b9
b13 = {
    "user_agent": "Your User-Agent",
    "URL": "https:
    "username": "your-email@gmail.com",
    "password": "your-email-password",
    "discount": 20.0
}
fonk1(b13)