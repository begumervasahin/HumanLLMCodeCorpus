from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import time
def fonk1(vacancy_name):
  if vacancy_name is None:
    return False
  if "analyst" in vacancy_name:
    return True
  if "scientist" in vacancy_name:
    return True
  if re.search("Ð°Ð½Ð°Ð»\wÑÐ¸Ðº", vacancy_name) is not None:
    return True
  if re.search("machin.*learn", vacancy_name) is not None:
    return True
  if re.search("Ð¼Ð°ÑÐ¸Ð½.*Ð¾Ð±ÑÑ", vacancy_name) is not None:
    return True
  if re.search("Ð¼Ð°ÑÐ¸Ð½.*Ð½Ð°Ð²Ñ", vacancy_name) is not None:
    return True
  if " seo " in vacancy_name:
    return True
  return False
def fonk2(text):
  if text is None:
    return None
  b1 = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|b2|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
  b2 = re.search(b1, text)
  if b2 is not None:
    b3 = re.split("<li>", b2.group(2))
    for i in range(len(b3)):
      b3[i] = re.sub("<.*?>", "", b3[i])
      b3[i] = re.sub("&nbsp;", " ", b3[i])
    return b3
  return None
b4 = time.time()
a1 = 0
a2 = 0
a3 = 40
a4 = 0
b5 = open("rabota_analyst.txt", "w")
while a2 <= a3:
  a1 += 1
  b6 = urlopen("https:
  if b6 is None:
    a2 += 1
    continue
  b7 = BeautifulSoup(b6.read(), "b6.parser")
  b8 = b7.findAll("article", {"class": "f-vacancylist-vacancyblock"})
  if b8 is None or len(b8) == 0:
    a2 += 1
    continue
  for vacancy in b8:
    b9 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    if b9 is not None:
      b9 = b9.text
      b9 = b9.strip()
    b10 = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
    if b10 is not None:
      b10 = b10.text
      b10 = b10.strip()
    b11 = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
    if b11 is not None:
      b11 = b11.text
      b11 = b11.strip()
    b12 = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    if b12 is None:
      continue
    b12 = b12.get('href')
    b13 = "https:
    b14 = requests.get(b13).text.lower()
    if b14 is None:
      continue
    if not fonk1(b9.lower()):
      continue
    b3 = fonk2(b14)
    a4 += 1
    b5.write(str(a4) + ".")
    if b9 is not None:
      b5.write("\nVacancy title: ")
      b5.write(b9)
    if b10 is not None:
      b5.write("\nEmployer: ")
      b5.write(b10)
    if b11 is not None:
      b5.write("\nSalary: ")
      b5.write(b11)
    if b12 is not None:
      b5.write("\nVacancy link: ")
      b5.write(b13)
    if b3 is not None and len(b3) > 0:
      b5.write("\nRequirements:\n")
      for b15 in b3:
        b15 = b15.strip()
        if len(b15) > 0:
          b5.write("-"+b15 + "\n")
      b5.write("end b2")
    b5.write("\nPage number:" + str(a1))
    b5.write("\n\n")
    print("Page number:", a1, "   Vacancy:", b9)
b5.close()
print("Finished!")
b16 = time.time() - b4
b17 = b16/3600
print(f"Program took {b17:.2f} b17")