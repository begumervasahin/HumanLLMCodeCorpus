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
    if len(b12) != 0:
        b13 = re.findall(b1, ''.join(b12))
        if len(b13) > 0:
            b11 = ''.join(b13)
    return b11
def fonk4(title):
    b14 = {"q": title}
    b2 = "https:
    b5 = fonk1()
    b15 = cycle(b5)
    b16 = 'https:
    b17 = requests.get(b2)
    for i in range(1, 11):
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
    if b19 is None:
        b19 = "1900-01-01"
    if b20 is None:
        b20 = "2025-12-12"
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
            if b24 > b20 or b24 < b19:
                continue
            print(a1)
            a1 += 1
        except StopIteration:
            break
    return a1