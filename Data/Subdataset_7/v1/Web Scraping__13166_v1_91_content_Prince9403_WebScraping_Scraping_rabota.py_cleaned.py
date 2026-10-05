from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
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
def fonk2(text):
    if text is None:
        return None
    b2 = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|b3|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
    b3 = re.search(b2, text)
    if b3 is not None:
        b4 = re.split("<li>", b3.group(2))
        for i in range(len(b4)):
            b4[i] = re.sub("<.*?>", "", b4[i])
            b4[i] = re.sub("&nbsp;", " ", b4[i])
        return b4
    return None
b5 = time.time()
a1 = 0
a2 = 0
a3 = 40
a4 = 0
b6 = open("rabota_analyst.txt", "w")
while a2 <= a3:
    a1 += 1
    b7 = f"https:
    b8 = urlopen(b7)
    if b8 is None:
        a2 += 1
        continue
    b9 = BeautifulSoup(b8.read(), "b8.parser")
    b10 = b9.findAll("article", {"class": "f-vacancylist-vacancyblock"})
    if b10 is None or len(b10) == 0:
        a2 += 1
        continue
    for vacancy in b10:
        b11 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
        if b11 is not None:
            b11 = b11.text.strip()
        b12 = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
        if b12 is not None:
            b12 = b12.text.strip()
        b13 = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
        if b13 is not None:
            b13 = b13.text.strip()
        b14 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
        if b14 is None:
            continue
        b14 = b14.get('href')
        b15 = "https:
        b16 = requests.get(b15).text.lower()
        if b16 is None:
            continue
        if not fonk1(b11.lower()):
            continue
        b4 = fonk2(b16)
        a4 += 1
        b6.write(str(a4) + ".\n")
        if b11 is not None:
            b6.write("Vacancy title: " + b11 + "\n")
        if b12 is not None:
            b6.write("Employer: " + b12 + "\n")
        if b13 is not None:
            b6.write("Salary: " + b13 + "\n")
        if b15 is not None:
            b6.write("Vacancy link: " + b15 + "\n")
        if b4 is not None and len(b4) > 0:
            b6.write("Requirements:\n")
            for b17 in b4:
                b17 = b17.strip()
                if len(b17) > 0:
                    b6.write("- " + b17 + "\n")
            b6.write("End b3\n")
        b6.write("Page number: " + str(a1) + "\n\n")
        print("Page number:", a1, "   Vacancy:", b11)
b6.close()
print("Finished!")
b18 = time.time() - b5
b19 = b18 / 3600
print(f"Program took {b19:.2f} b19")