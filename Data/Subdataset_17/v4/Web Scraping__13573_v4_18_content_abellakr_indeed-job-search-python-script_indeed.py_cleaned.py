import requests
from bs4 import BeautifulSoup
import pandas as pd
def URLGen(country, job, location, salary):
    URLJob = "+".join(job.split())
    URLLoc = "+".join(location.split())
    sal = float(salary) / 1000
    URLSal = "24" + str(sal)
    if country == 'US':
        URL = f"https:
    elif country == 'CA':
        URL = f"https:
    else:
        print("Invalid country option.")
        URL = ''
    return URL
def extract_job_title_from_result(soup):
    jobs = []
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return jobs
def extract_location_from_result(soup):
    locations = [span.text for span in soup.find_all("span", attrs={"class": "location"})]
    return locations
def extract_salary_from_result(soup):
    salaries = []
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        try:
            salaries.append(div.find("nobr").text)
        except:
            try:
                div_two = div.find(name="div", attrs={"class": "sjcl"})
                div_three = div_two.find("div")
                salaries.append(div_three.strip())
            except:
                salaries.append("Nothing found")
    return salaries
def extract_summary_from_result(soup):
    summaries = [span.text.strip() for span in soup.find_all("span", attrs={"class": "summary"})]
    return summaries
def findJobs(URL):
    if URL:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        jobs = extract_job_title_from_result(soup)
        locations = extract_location_from_result(soup)
        salaries = extract_salary_from_result(soup)
        fmt = '%-10s%-60s%-70s%s'
        for i, (job, location, salary) in enumerate(zip(jobs, locations, salaries)):
            print(fmt % (i, job, location, salary))
def PageGen(URL):
    return [URL + "&start=" + str(x) for x in range(10, 40, 10)]
country = input("Which country are you looking to work in (CA/US)?: ")
job = input("Type of job you're looking for: ")
location = input("Desired location: ")
salary = input("Desired salary: ")
URL = URLGen(country, job, location, salary)
pageUrls = PageGen(URL)
x = 1
fmt = '%-10s%-60s%-70s%s'
print(fmt % ('', 'Job Title', 'Location', 'Salary'))
for page in pageUrls:
    print("Page " + str(x))
    findJobs(page)
    x += 1