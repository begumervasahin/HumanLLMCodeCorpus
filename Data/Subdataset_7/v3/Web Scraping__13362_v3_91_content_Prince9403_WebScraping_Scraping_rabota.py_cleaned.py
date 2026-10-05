import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(b13):
    return b13.b1 = = 200
def fonk2(vacancy):
    b2 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    b3 = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
    b4 = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
    b5 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    b2 = b2.text.strip() if b2 else None
    b3 = b3.text.strip() if b3 else None
    b4 = b4.text.strip() if b4 else None
    b5 = b5.get('href') if b5 else None
    b6 = "https:
    return b2, b3, b4, b6
def fonk3(html_text):
    if not html_text:
        return None
    b7 = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|requirements|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
    b8 = re.search(b7, html_text)
    if b8:
        b9 = b8.group(2)
        b10 = re.split("<li>", b9)
        b10 = [re.sub("<.*?>", "", req) for req in b10]
        b10 = [re.sub("&nbsp;", " ", req) for req in b10]
        return [req.strip() for req in b10 if req.strip()]
    return None
def fonk4(b11 = 40):
    a1 = 0
    a2 = 0
    a3 = 0
    with open("rabota_analyst.txt", "w") as output_file:
        while a2 <= b11:
            a1 += 1
            b12 = f"https:
            b13 = requests.get(b12)
            if not fonk1(b13):
                a2 += 1
                continue
            b14 = BeautifulSoup(b13.text, "html.parser")
            b15 = b14.find_all("article", {"class": "f-vacancylist-vacancyblock"})
            if not b15:
                a2 += 1
                continue
            for vacancy in b15:
                b2, b3, b4, b6 = fonk2(vacancy)
                if not b2 or not is_valid_vacancy(b2):
                    continue
                b16 = requests.get(b6).text.lower() if b6 else None
                b10 = fonk3(b16)
                a3 += 1
                output_file.write(f"{a3}.\n")
                output_file.write(f"Vacancy b2: {b2}\n") if b2 else None
                output_file.write(f"Employer: {b3}\n") if b3 else None
                output_file.write(f"Salary: {b4}\n") if b4 else None
                output_file.write(f"Vacancy b5: {b6}\n") if b6 else None
                if b10:
                    output_file.write("Requirements:\n")
                    for requirement in b10:
                        output_file.write(f"- {requirement}\n")
                    output_file.write("End requirements\n")
                output_file.write(f"Page number: {a1}\n\n")
                print("Page number:", a1, "   Vacancy:", b2)
            output_file.close()
            print("Finished!")
            b17 = time.time() - start_time
            b18 = b17 / 3600
            print(f"Program took {b18:.2f} b18")
if b19 = = "__main__":
    fonk4()