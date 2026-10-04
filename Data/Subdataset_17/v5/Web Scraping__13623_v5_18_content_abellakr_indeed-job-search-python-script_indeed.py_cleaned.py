import requests
from bs4 import BeautifulSoup
import pandas as pd
def generate_url(country, job, location, salary):
    job_formatted = "+".join(job.split())
    location_formatted = "+".join(location.split())
    salary_formatted = "24" + str(float(salary) / 1000)
    if country == 'US':
        url = f"https:
    elif country == 'CA':
        url = f"https:
    else:
        print("Invalid country option.")
        url = ''
    return url
def extract_job_titles(soup):
    return [a["title"] for a in soup.find_all(name="a", attrs={"data-tn-element": "jobTitle"})]
def extract_locations(soup):
    return [span.text for span in soup.find_all("span", attrs={"class": "location"})]
def extract_salaries(soup):
    salaries = []
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        try:
            salaries.append(div.find("nobr").text)
        except AttributeError:
            try:
                div_sjcl = div.find(name="div", attrs={"class": "sjcl"})
                div_salary = div_sjcl.find("div")
                salaries.append(div_salary.text.strip())
            except AttributeError:
                salaries.append("Nothing found")
    return salaries
def extract_summaries(soup):
    return [span.text.strip() for span in soup.find_all("span", attrs={"class": "summary"})]
def find_jobs(url):
    if url:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        jobs = extract_job_titles(soup)
        locations = extract_locations(soup)
        salaries = extract_salaries(soup)
        for i, (job, location, salary) in enumerate(zip(jobs, locations, salaries)):
            print(f"{i:<10}{job:<60}{location:<70}{salary}")
def generate_paginated_urls(base_url):
    return [base_url + "&start=" + str(x) for x in range(10, 40, 10)]
country = input("Which country are you looking to work in (CA/US)?: ")
job = input("Type of job you're looking for: ")
location = input("Desired location: ")
salary = input("Desired salary: ")
url = generate_url(country, job, location, salary)
page_urls = generate_paginated_urls(url)
print(f"{'':<10}{'Job Title':<60}{'Location':<70}{'Salary'}")
for page_number, page_url in enumerate(page_urls, start=1):
    print(f"Page {page_number}")
    find_jobs(page_url)