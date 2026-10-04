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
    quals_list = [item.text.replace("\n", "") for item in job.find_all("div", class_="item")]
    return quals_list
def get_prompt(job):
    prompts_list = [prompt["href"] for prompt in job.find_all("a")]
    return prompts_list
if __name__ == "__main__":
    chromedriver_filename = "./webdrivers/chromedriver_windows.exe"
    if sys.platform.startswith("darwin"):
        chromedriver_filename = "./webdrivers/chromedriver_mac"
    elif sys.platform.startswith("linux"):
        chromedriver_filename = "./webdrivers/chromedriver_linux"
    driver = webdriver.Chrome(chromedriver_filename)
    recruit_html = get_html(driver, "/recruit")
    soup = BeautifulSoup(recruit_html, "html.parser")
    navbar_menu = soup.find("div", class_="navbar-menu")
    positions_re = re.compile("/recruit/[a-z]+")
    relative_path_tags = navbar_menu.find_all(
        lambda tag: tag.has_attr("href") and positions_re.match(tag["href"])
    )
    relative_paths = [tag["href"] for tag in relative_path_tags]
    for path in relative_paths:
        print(path)
    fieldnames = ["ROLE", "DESCRIPTION", "QUALIFICATIONS", "PROMPT"]
    writer = initialize_csv("role.csv", fieldnames)
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
    driver.quit()