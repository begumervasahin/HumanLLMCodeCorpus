import requests
from bs4 import BeautifulSoup
import re
import time
def is_valid_response(response):
    return response.status_code == 200
def extract_vacancy_info(vacancy):
    title = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    employer = vacancy.find('a', {'class': 'f-text-dark-bluegray f-visited-enable'})
    salary = vacancy.find('p', {'class': 'fd-beefy-soldier -price'})
    link = vacancy.find('a', {'class': 'f-visited-enable ga_listing'})
    title = title.text.strip() if title else None
    employer = employer.text.strip() if employer else None
    salary = salary.text.strip() if salary else None
    link = link.get('href') if link else None
    full_link = "https:
    return title, employer, salary, full_link
def get_requirements(html_text):
    if not html_text:
        return None
    pattern = "<p.*(ÑÑÐµÐ±Ð¾Ð²Ð°Ð½Ð¸Ñ|requirements|Ð²Ð¸Ð¼Ð¾Ð³Ð¸).*?<ul>(.*?)</ul>"
    requirements_match = re.search(pattern, html_text)
    if requirements_match:
        requirements_text = requirements_match.group(2)
        requirements_list = re.split("<li>", requirements_text)
        requirements_list = [re.sub("<.*?>", "", req) for req in requirements_list]
        requirements_list = [re.sub("&nbsp;", " ", req) for req in requirements_list]
        return [req.strip() for req in requirements_list if req.strip()]
    return None
def scrape_vacancies(max_faults=40):
    page_number = 0
    num_faults = 0
    vacancy_number = 0
    with open("rabota_analyst.txt", "w") as output_file:
        while num_faults <= max_faults:
            page_number += 1
            url = f"https:
            response = requests.get(url)
            if not is_valid_response(response):
                num_faults += 1
                continue
            bsObj = BeautifulSoup(response.text, "html.parser")
            vacancy_list = bsObj.find_all("article", {"class": "f-vacancylist-vacancyblock"})
            if not vacancy_list:
                num_faults += 1
                continue
            for vacancy in vacancy_list:
                title, employer, salary, full_link = extract_vacancy_info(vacancy)
                if not title or not is_valid_vacancy(title):
                    continue
                vacancy_text = requests.get(full_link).text.lower() if full_link else None
                requirements_list = get_requirements(vacancy_text)
                vacancy_number += 1
                output_file.write(f"{vacancy_number}.\n")
                output_file.write(f"Vacancy title: {title}\n") if title else None
                output_file.write(f"Employer: {employer}\n") if employer else None
                output_file.write(f"Salary: {salary}\n") if salary else None
                output_file.write(f"Vacancy link: {full_link}\n") if full_link else None
                if requirements_list:
                    output_file.write("Requirements:\n")
                    for requirement in requirements_list:
                        output_file.write(f"- {requirement}\n")
                    output_file.write("End requirements\n")
                output_file.write(f"Page number: {page_number}\n\n")
                print("Page number:", page_number, "   Vacancy:", title)
            output_file.close()
            print("Finished!")
            seconds = time.time() - start_time
            hours = seconds / 3600
            print(f"Program took {hours:.2f} hours")
if __name__ == "__main__":
    scrape_vacancies()