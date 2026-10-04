import requests
from bs4 import BeautifulSoup
def generate_url(country, job, location, salary):
    job_query = "+".join(job.split())
    location_query = "+".join(location.split())
    salary_query = "24" + str(int(salary)
    if country == 'US':
        url = f"https:
    elif country == 'CA':
        url = f"https:
    else:
        print("That's not a valid option.")
        url = ''
    return url
def extract_job_titles(soup):
    job_titles = [a["title"] for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard"})
                  for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"})]
    return job_titles
def extract_locations(soup):
    locations = [div["data-rc-loc"] for div in soup.find_all(name="div", attrs={"class":"recJobLoc"})]
    return locations
def extract_salaries(soup):
    salaries = []
    for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard"}):
        try:
            salary = div.find("span", attrs={"class": "salaryText"}).text.strip()
        except AttributeError:
            salary = "Not specified"
        salaries.append(salary)
    return salaries
def extract_summaries(soup):
    summaries = [div.text.strip() for div in soup.find_all(name="div", attrs={"class":"summary"})]
    return summaries
def find_jobs(url):
    if not url:
        return
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    jobs = extract_job_titles(soup)
    locations = extract_locations(soup)
    salaries = extract_salaries(soup)
    fmt = '{:<10}{:<60}{:<70}{}'
    for i, (job, location, salary) in enumerate(zip(jobs, locations, salaries)):
        print(fmt.format(i, job, location, salary))
def generate_page_urls(base_url):
    return [base_url + f"&start={x}" for x in range(10, 40, 10)]
def main():
    country = input("Which country are you looking to work in (CA/US)?: ")
    job = input("Type of job you're looking for: ")
    location = input("Desired location: ")
    salary = input("Desired salary: ")
    base_url = generate_url(country, job, location, salary)
    page_urls = generate_page_urls(base_url)
    fmt = '{:<10}{:<60}{:<70}{}'
    print(fmt.format('', 'Job Title', 'Location', 'Salary'))
    for page_number, page_url in enumerate(page_urls, start=1):
        print(f"Page {page_number}")
        find_jobs(page_url)
if __name__ == "__main__":
    main()