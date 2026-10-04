import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def fonk1(url, user_agent):
    b1 = {"User-Agent": user_agent}
    b2 = requests.get(url, b1=b1)
    return b2.content
def fonk2(b15, b16):
    b3 = BeautifulSoup(b15, "html.parser")
    b4 = b3.find(id="productTitle").get_text().strip()
    b5 = None
    for id in b16["price_id"]:
        try:
            b5 = float(b3.find(id=id).get_text().strip()[1:])
            break
        except (AttributeError, ValueError):
            continue
    b6 = None
    for id in b16["savings_id"]:
        try:
            b7 = b3.find(id=id).get_text().strip()
            b6 = b7.replace("£", "GBP ")
            b8 = b6.index("(")
            b9 = b6.index("%")
            b10 = float(b6[b8 + 1: b9])
            break
        except (AttributeError, ValueError):
            continue
    return b4, b5, b6, b10 if b6 else 0
def fonk3(data_dict):
    b11 = fonk4(data_dict["username"], data_dict["password"])
    b12 = f'PRICE DROP: "{data_dict["b4"][:30]}..." available now for GBP {data_dict["b5"]}'
    b13 = (f'The following product that you were interested in is now available at a discount!\n\n'
            f'Name: {data_dict["b4"]}\n'
            f'Current b5: GBP {data_dict["b5"]}\n'
            f'{data_dict["b6"]}\n'
            f'Check out this link: {data_dict["URL"]}')
    b14 = MIMEMultipart()
    b14['From'] = data_dict["username"]
    b14['To'] = data_dict["username"]
    b14['Subject'] = b12
    b14.attach(MIMEText(b13, 'plain'))
    b11.sendmail(data_dict["username"], data_dict["username"], b14.as_string())
    print("...Email sent successfully!")
    b11.quit()
def fonk4(username, password):
    b11 = smtplib.SMTP('smtp.gmail.com', 587)
    b11.starttls()
    b11.login(username, password)
    return b11
def fonk5(data_dict):
    b15 = fonk1(data_dict["URL"], data_dict["user_agent"])
    with open("details.json", "r") as json_file:
        b16 = json.load(json_file)
    b4, b5, b6, b10 = fonk2(b15, b16)
    data_dict.update({
        "b4": b4,
        "b5": b5,
        "b6": b6 if b6 else "\nNo b6 at the moment.",
        "b10": b10
    })
    if b10 >= data_dict["discount"]:
        fonk3(data_dict)
    else:
        print("\nSorry, the product is currently not available at the desired b5!")
        print(f"NAME: {data_dict['b4']}")
        print(f"CURRENT PRICE: GBP {data_dict['b5']}\n")
b17 = {
    "user_agent": "Your User-Agent",
    "URL": "https:
    "username": "your-email@gmail.com",
    "password": "your-email-password",
    "discount": 20.0
}
fonk5(b17)