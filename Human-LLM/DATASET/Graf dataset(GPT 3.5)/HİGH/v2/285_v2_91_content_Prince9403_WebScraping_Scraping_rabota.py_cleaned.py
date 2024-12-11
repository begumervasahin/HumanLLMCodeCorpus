import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(vacancy_name):
    if vacancy_name is None:
        return False
    b1 = ["analyst", "scientist", "Ð°Ð½Ð°Ð»Ð¸ÑÐ¸Ðº", "machin.*learn", "Ð¼Ð°ÑÐ¸Ð½.*Ð¾Ð±ÑÑ", "Ð¼Ð°ÑÐ¸Ð½.*Ð½Ð°Ð²Ñ", "seo"]
    for keyword in b1:
        if re.search(keyword, vacancy_name.lower()) is not None:
            return True
    return False
def fonk2(html_text):
    if html_text is None:
        return None
    b2 = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|requirements|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
    b3 = re.search(b2, html_text)
    if b3 is not None:
        b4 = b3.group(2)
        b5 = re.split("<li>", b4)
        for i in range(len(b5)):
            b5[i] = re.sub("<.*?>", "", b5[i])
            b5[i] = re.sub("&nbsp;", " ", b5[i])
        return b5
    return None
b6 = time.time()
a1 = 0
a2 = 0
a3 = 40
a4 = 0
b7 = open("rabota_analyst.txt", "w")
while a2 <= a3:
    a1 += 1
    b8 = f"https:
    b9 = requests.get(b8)
    if b9.status_code != 200:
        a2 += 1
        continue
    b10 = BeautifulSoup(b9.text, "html.parser")
    b11 = b10.findAll("article", {"class": "f-vacancylist-vacancyblock"})
    if not b11:
        a2 += 1
        continue
    for vacancy in b11:
        b12 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
        if b12:
            b12 = b12.text.strip()
        b13 = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
        if b13:
            b13 = b13.text.strip()
        b14 = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
        if b14:
            b14 = b14.text.strip()
        b15 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
        if not b15:
            continue
        b15 = b15.get('href')
        b16 = "https:
        b17 = requests.get(b16).text.lower()
        if not b17:
            continue
        if not fonk1(b12):
            continue
        b5 = fonk2(b17)
        a4 += 1
        b7.write(f"{a4}.\n")
        if b12:
            b7.write(f"Vacancy title: {b12}\n")
        if b13:
            b7.write(f"Employer: {b13}\n")
        if b14:
            b7.write(f"Salary: {b14}\n")
        if b16:
            b7.write(f"Vacancy link: {b16}\n")
        if b5:
            b7.write("Requirements:\n")
            for b18 in b5:
                b18 = b18.strip()
                if b18:
                    b7.write(f"- {b18}\n")
            b7.write("End requirements\n")
        b7.write(f"Page number: {a1}\n\n")
        print("Page number:", a1, "   Vacancy:", b12)
b7.close()
print("Finished!")
b19 = time.time() - b6
b20 = b19 / 3600
print(f"Program took {b20:.2f} b20")