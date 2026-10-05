import requests
from bs4 import BeautifulSoup
import re
import time
def is_appropriate_vacancy(vacancy_name):
    if vacancy_name is None:
        return False
    keywords = ["analyst", "scientist", "Ð°Ð½Ð°Ð»Ð¸ÑÐ¸Ðº", "machin.*learn", "Ð¼Ð°ÑÐ¸Ð½.*Ð¾Ð±ÑÑ", "Ð¼Ð°ÑÐ¸Ð½.*Ð½Ð°Ð²Ñ", "seo"]
    for keyword in keywords:
        if re.search(keyword, vacancy_name.lower()) is not None:
            return True
    return False
def get_requirements(html_text):
    if html_text is None:
        return None
    pattern = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|requirements|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
    requirements_match = re.search(pattern, html_text)
    if requirements_match is not None:
        requirements_text = requirements_match.group(2)
        requirements_list = re.split("<li>", requirements_text)
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
    url = f"https:
    response = requests.get(url)
    if response.status_code != 200:
        num_faults += 1
        continue
    bsObj = BeautifulSoup(response.text, "html.parser")
    vacancy_list = bsObj.findAll("article", {"class": "f-vacancylist-vacancyblock"})
    if not vacancy_list:
        num_faults += 1
        continue
    for vacancy in vacancy_list:
        vacancy_title = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
        if vacancy_title:
            vacancy_title = vacancy_title.text.strip()
        vacancy_employer = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
        if vacancy_employer:
            vacancy_employer = vacancy_employer.text.strip()
        vacancy_salary = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
        if vacancy_salary:
            vacancy_salary = vacancy_salary.text.strip()
        vacancy_link = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
        if not vacancy_link:
            continue
        vacancy_link = vacancy_link.get('href')
        full_vacancy_link = "https:
        vacancy_text = requests.get(full_vacancy_link).text.lower()
        if not vacancy_text:
            continue
        if not is_appropriate_vacancy(vacancy_title):
            continue
        requirements_list = get_requirements(vacancy_text)
        vacancy_number += 1
        output_file.write(f"{vacancy_number}.\n")
        if vacancy_title:
            output_file.write(f"Vacancy title: {vacancy_title}\n")
        if vacancy_employer:
            output_file.write(f"Employer: {vacancy_employer}\n")
        if vacancy_salary:
            output_file.write(f"Salary: {vacancy_salary}\n")
        if full_vacancy_link:
            output_file.write(f"Vacancy link: {full_vacancy_link}\n")
        if requirements_list:
            output_file.write("Requirements:\n")
            for requirement in requirements_list:
                requirement = requirement.strip()
                if requirement:
                    output_file.write(f"- {requirement}\n")
            output_file.write("End requirements\n")
        output_file.write(f"Page number: {page_number}\n\n")
        print("Page number:", page_number, "   Vacancy:", vacancy_title)
output_file.close()
print("Finished!")
seconds = time.time() - start_time
hours = seconds / 3600
print(f"Program took {hours:.2f} hours")