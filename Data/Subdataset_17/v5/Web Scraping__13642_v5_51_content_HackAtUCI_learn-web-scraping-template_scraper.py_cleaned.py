import re
import time
import csv
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
def get_html(driver, path):
    driver.get(f"https:
    time.sleep(2)
    return driver.find_element_by_tag_name("html").get_attribute("innerHTML")
def initialize_csv(file_name, fieldnames):
    file = open(file_name, "w", newline="")
    writer = csv.DictWriter(file, fieldnames)
    writer.writeheader()
    return writer
def get_qualifications(job):
    return [item.text.replace("\n", "") for item in job.find_all("div", class_="item")]
def get_prompt(job):
    return [prompt["href"] for prompt in job.find_all("a")]
def get_chromedriver_path():
    if sys.platform.startswith("darwin"):
        return "./webdrivers/chromedriver_mac"
    elif sys.platform.startswith("linux"):
        return "./webdrivers/chromedriver_linux"
    return "./webdrivers/chromedriver_windows.exe"
def extract_relative_paths(soup):
    navbar_menu = soup.find("div", class_="navbar-menu")
    positions_re = re.compile("/recruit/[a-z]+")
    return [tag["href"] for tag in navbar_menu.find_all(lambda tag: tag.has_attr("href") and positions_re.match(tag["href"]))]
def scrape_job_details(driver, relative_paths, writer):
    for relative_path in relative_paths:
        positions_html = get_html(driver, relative_path)
        soup = BeautifulSoup(positions_html, "html.parser")
        for job in soup.find_all("div", class_="job"):
            job_data = {
                "ROLE": job.find("div", class_="job-title").text.replace("\n", ""),
                "DESCRIPTION": job.find("span").text.replace("\n", ""),
                "QUALIFICATIONS": get_qualifications(job),
                "PROMPT": get_prompt(job),
            }
            writer.writerow(job_data)
if __name__ == "__main__":
    chromedriver_filename = get_chromedriver_path()
    driver = webdriver.Chrome(chromedriver_filename)
    recruit_html = get_html(driver, "/recruit")
    soup = BeautifulSoup(recruit_html, "html.parser")
    relative_paths = extract_relative_paths(soup)
    for path in relative_paths:
        print(path)
    fieldnames = ["ROLE", "DESCRIPTION", "QUALIFICATIONS", "PROMPT"]
    writer = initialize_csv("role.csv", fieldnames)
    scrape_job_details(driver, relative_paths, writer)
    driver.quit()