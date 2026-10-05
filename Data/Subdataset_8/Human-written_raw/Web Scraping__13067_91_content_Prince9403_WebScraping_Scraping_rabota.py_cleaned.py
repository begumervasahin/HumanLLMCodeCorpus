from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import time
def check_if_appropriate(vacancy_name):
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
def get_requirements_from_html(text):
  if text is None:
    return None
  pattern = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|requirements|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
  requirements = re.search(pattern, text)
  if requirements is not None:
    requirements_list = re.split("<li>", requirements.group(2))
    for i in range(len(requirements_list)):
      requirements_list[i] = re.sub("<.*?>", "", requirements_list[i])
      requirements_list[i] = re.sub("&nbsp;", " ", requirements_list[i])
    return requirements_list
  return None
start_time = time.time()
page_number = 0
num_faults = 0
max_num_faults = 40
vacancy_number = 0
output_file = open("rabota_analyst.txt", "w")
while num_faults <= max_num_faults:
  page_number += 1
  html = urlopen("https:
  if html is None:
    num_faults += 1
    continue
  bsObj = BeautifulSoup(html.read(), "html.parser")
  vacancy_list = bsObj.findAll("article", {"class": "f-vacancylist-vacancyblock"})
  if vacancy_list is None or len(vacancy_list) == 0:
    num_faults += 1
    continue
  for vacancy in vacancy_list:
    vacancy_title = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    if vacancy_title is not None:
      vacancy_title = vacancy_title.text
      vacancy_title = vacancy_title.strip()
    vacancy_employer = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
    if vacancy_employer is not None:
      vacancy_employer = vacancy_employer.text
      vacancy_employer = vacancy_employer.strip()
    vacancy_salary = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
    if vacancy_salary is not None:
      vacancy_salary = vacancy_salary.text
      vacancy_salary = vacancy_salary.strip()
    vacancy_link = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    if vacancy_link is None:
      continue
    vacancy_link = vacancy_link.get('href')
    full_vacancy_link = "https:
    vacancy_text = requests.get(full_vacancy_link).text.lower()
    if vacancy_text is None:
      continue
    if not check_if_appropriate(vacancy_title.lower()):
      continue
    requirements_list = get_requirements_from_html(vacancy_text)
    vacancy_number += 1
    output_file.write(str(vacancy_number) + ".")
    if vacancy_title is not None:
      output_file.write("\nVacancy title: ")
      output_file.write(vacancy_title)
    if vacancy_employer is not None:
      output_file.write("\nEmployer: ")
      output_file.write(vacancy_employer)
    if vacancy_salary is not None:
      output_file.write("\nSalary: ")
      output_file.write(vacancy_salary)
    if vacancy_link is not None:
      output_file.write("\nVacancy link: ")
      output_file.write(full_vacancy_link)
    if requirements_list is not None and len(requirements_list) > 0:
      output_file.write("\nRequirements:\n")
      for requirement in requirements_list:
        requirement = requirement.strip()
        if len(requirement) > 0:
          output_file.write("-"+requirement + "\n")
      output_file.write("end requirements")
    output_file.write("\nPage number:" + str(page_number))
    output_file.write("\n\n")
    print("Page number:", page_number, "   Vacancy:", vacancy_title)
output_file.close()
print("Finished!")
seconds = time.time() - start_time
hours = seconds/3600
print(f"Program took {hours:.2f} hours")