import requests
from bs4 import BeautifulSoup
import pandas as pd
def URLGen(country, job, location, salary):
    URLJob = "+".join(job.split())
    URLLoc = "+".join(location.split())
    sal = float(salary)/1000
    URLSal = "24"+str(sal)
    if country == 'US':
        URL = f"https:
    elif country == 'CA':
        URL = f"https:
    else:
        print("That's not a valid option.")
        URL = ''
    return URL
def extract_job_title_from_result(soup):
    jobs = []
    for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
    return jobs
def extract_location_from_result(soup):
    locations = []
    spans = soup.find_all("div", attrs={"class": "recJobLoc"})
    for span in spans:
        locations.append(span["data-rc-loc"])
    return locations
def extract_salary_from_result(soup):
    salaries = []
    for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard"}):
        try:
            salaries.append(div.find("span", attrs={"class": "salaryText"}).text.strip())
        except:
            salaries.append("Not specified")
    return salaries
def extract_summary_from_result(soup):
    summaries = []
    spans = soup.find_all("div", attrs={"class":"summary"})
    for span in spans:
        summaries.append(span.text.strip())
    return summaries
def findJobs(URL):
    if URL != '':
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        jobs = extract_job_title_from_result(soup)
        locations = extract_location_from_result(soup)
        salaries = extract_salary_from_result(soup)
        summaries = extract_summary_from_result(soup)
        fmt = '{:<10}{:<60}{:<70}{}'
        for i, (job, location, salary) in enumerate(zip(jobs, locations, salaries)):
            print(fmt.format(i, job, location, salary))
def PageGen(URL):
    pageUrls = [URL + f"&start={x}" for x in range(10, 40, 10)]
    return pageUrls
def main():
    country = input("Which country are you looking to work in (CA/US)?: ")
    job = input("Type of job you're looking for: ")
    location = input("Desired location: ")
    salary = input("Desired salary: ")
    URL = URLGen(country, job, location, salary)
    pageUrls = PageGen(URL)
    fmt = '{:<10}{:<60}{:<70}{}'
    print(fmt.format('', 'Job title', 'Location', 'Salary'))
    for x, page in enumerate(pageUrls, start=1):
        print(f"Page {x}")
        findJobs(page)
if __name__ == "__main__":
    main()