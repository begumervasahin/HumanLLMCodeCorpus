import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
from urllib.request import urlopen
from crossref.restful import Journals
from django.utils.dateparse import parse_date
from lxml.html import fromstring
from selenium import webdriver
import time
import json
from proxy_requests.proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
from metadata import getDate
email_regex = re.compile(r"([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)")
def get_proxies():
    url = 'https:
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('
        proxy = ":".join([i.xpath('.
        proxies.add(proxy)
    return proxies
def download_pdf(link, download_folder, path_to_chrome_driver):
    options = webdriver.ChromeOptions()
    profile = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.default_directory": download_folder,
        "download.extensions_to_open": ""
    }
    options.add_experimental_option("prefs", profile)
    driver = webdriver.Chrome(path_to_chrome_driver, chrome_options=options)
    driver.get(link)
    filename = link.split("/")[4].split(".cfm")[0]
    time.sleep(10)
    driver.close()
def pdf_extraction(contents):
    email = None
    matching = [s for s in contents if "@" in s]
    if len(matching) != 0:
        match_list = re.findall(email_regex, ''.join(matching))
        if len(match_list) > 0:
            email = ''.join(match_list)
    return email
def get_total_citations(title):
    args = {"q": title}
    url = "https:
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    url_check = 'https:
    url_page = requests.get(url)
    for i in range(1, 11):
        proxy = next(proxy_pool)
        print(proxy)
        print("Requesting...")
        try:
            url_page = requests.get(url, proxies={"http": proxy, "https": proxy})
            response = requests.get(url_check, proxies={"http": proxy, "https": proxy})
            print(response.json())
            break
        except:
            print("Skipping. Connection error")
    soup = BeautifulSoup(url_page.content, 'html.parser')
def get_total_citations_for_journal(ISSN, start, end):
    if start is None:
        start = "1900-01-01"
    if end is None:
        end = "2025-12-12"
    start = parse_date(start)
    end = parse_date(end)
    journals = Journals()
    a = journals.works(ISSN).all()
    count = 0
    while True:
        try:
            b = next(a)
            date = getDate(b)
            print(date)
            if date > end or date < start:
                continue
            print(count)
            count += 1
        except StopIteration:
            break
    return count