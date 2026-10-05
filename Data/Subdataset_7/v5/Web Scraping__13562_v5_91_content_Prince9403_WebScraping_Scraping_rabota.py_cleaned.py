import requests
import re
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fonk1(vacancy_name):
    if not vacancy_name:
        return False
    b1 = ["analyst", "scientist", "Ð°Ð½Ð°Ð»Ð¸ÑÐ¸Ðº", "machin.*learn", "Ð¼Ð°ÑÐ¸Ð½.*Ð¾Ð±ÑÑ", "Ð¼Ð°ÑÐ¸Ð½.*Ð½Ð°Ð²Ñ", "seo"]
    return any(re.search(keyword, vacancy_name.lower()) for keyword in b1)
def fonk2(text):
    if not text:
        return None
    b2 = r"<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|b3|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
    b3 = re.search(b2, text, re.IGNORECASE | re.DOTALL)
    if b3:
        b4 = re.split(r"<li>", b3.group(2))
        return [re.sub(r"<.*?>", "", req).strip().replace("&nbsp;", " ") for req in b4 if req.strip()]
    return None
def fonk3(vacancy):
    b5 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    b6 = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
    b7 = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
    b8 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    if b5:
        b5 = b5.text.strip()
    if b6:
        b6 = b6.text.strip()
    if b7:
        b7 = b7.text.strip()
    if b8:
        b8 = b8.get('href')
    return b5, b6, b7, b8
def fonk4(a4):
    b9 = f"https:
    b10 = requests.get(b9)
    if not b10.ok:
        return None
    b11 = BeautifulSoup(b10.text, "html.parser")
    return b11.findAll("article", {"class": "f-vacancylist-vacancyblock"})
def fonk5():
    b12 = time.time()
    a1 = 40
    b13 = open("rabota_analyst.txt", "w")
    a2 = 0
    a3 = 0
    a4 = 0
    while a2 <= a1:
        a4 += 1
        b14 = fonk4(a4)
        if not b14:
            a2 += 1
            continue
        for vacancy in b14:
            b5, b6, b7, b8 = fonk3(vacancy)
            if not fonk1(b5):
                continue
            b15 = requests.get(f"https:
            b4 = fonk2(b15)
            a3 += 1
            b13.write(f"{a3}.\n")
            if b5:
                b13.write(f"Vacancy title: {b5}\n")
            if b6:
                b13.write(f"Employer: {b6}\n")
            if b7:
                b13.write(f"Salary: {b7}\n")
            if b8:
                b13.write(f"Vacancy link: https:
            if b4:
                b13.write("Requirements:\n")
                for requirement in b4:
                    b13.write(f"- {requirement}\n")
                b13.write("end b3\n")
            b13.write(f"Page number: {a4}\n\n")
            print("Page number:", a4, "   Vacancy:", b5)
    b13.close()
    print("Finished!")
    b16 = time.time() - b12
    b17 = b16 / 3600
    print(f"Program took {b17:.2f} b17")
if b18 = = "__main__":
    fonk5()