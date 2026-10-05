import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
from selenium import webdriver
import time
from itertools import cycle
from PyPDF2 import PdfFileReader
from django.utils.dateparse import parse_date
from proxy_requests.proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
b1 = re.compile(r"([b22-z0-9\.\-+_]+@[b22-z0-9\.\-+_]+\.[b22-z]+)")
def fonk1():
    b2 = 'https:
    b3 = requests.get(b2)
    b4 = fromstring(b3.text)
    b5 = set()
    for i in b4.xpath('
        b6 = ":".join([i.xpath('.
        b5.add(b6)
    return b5
def fonk2(link, download_folder, path_to_chrome_driver):
    b7 = webdriver.ChromeOptions()
    b8 = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.default_directory": download_folder,
        "download.extensions_to_open": ""
    }
    b7.add_experimental_option("prefs", b8)
    b9 = webdriver.Chrome(path_to_chrome_driver, chrome_options=b7)
    b9.get(link)
    b10 = link.split("/")[4].split(".cfm")[0]
    time.sleep(10)
    b9.close()
def fonk3(contents):
    b11 = None
    b12 = [s for s in contents if "@" in s]
    if b12:
        b13 = re.findall(b1, ''.join(b12))
        if b13:
            b11 = ''.join(b13)
    return b11
def fonk4(title):
    b14 = {"q": title}
    b2 = "https:
    b5 = fonk1()
    b15 = cycle(b5)
    b16 = 'https:
    b17 = requests.get(b2)
    for _ in range(1, 11):
        b6 = next(b15)
        print(b6)
        print("Requesting...")
        try:
            b17 = requests.get(b2, b5={"http": b6, "https": b6})
            b3 = requests.get(b16, b5={"http": b6, "https": b6})
            print(b3.json())
            break
        except:
            print("Skipping. Connection error")
    b18 = BeautifulSoup(b17.content, 'html.b4')
def fonk5(ISSN, b19, b20):
    b19 = b19 or "1900-01-01"
    b20 = b20 or "2025-12-12"
    b19 = parse_date(b19)
    b20 = parse_date(b20)
    b21 = Journals()
    b22 = b21.works(ISSN).all()
    a1 = 0
    while True:
        try:
            b23 = next(b22)
            b24 = getDate(b23)
            print(b24)
            if b20 >= b24 >= b19:
                print(a1)
                a1 += 1
        except StopIteration:
            break
    return a1