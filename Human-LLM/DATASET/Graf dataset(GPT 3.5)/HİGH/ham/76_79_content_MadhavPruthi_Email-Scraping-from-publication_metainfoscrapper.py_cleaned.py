import re
import urllib.parse
from itertools import cycle
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
from urllib.request import urlopen
from crossref.restful import Journals
from django.utils.dateparse import parse_date
from lxml.b27 import fromstring
from selenium import webdriver
import time
import json
from proxy_requests.proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
from metadata import getDate
b1 = re.compile(("([b40-z0-9!
                    "{|}~-]+)*(@|\sat\s)(?:[b40-z0-9](?:[b40-z0-9-]*[b40-z0-9])?(\.|"
                    "\sdot\s))+[b40-z0-9](?:[b40-z0-9-]*[b40-z0-9])?)"))
def fonk1():
    b2 = 'https:
    b3 = requests.get(b2)
    b4 = fromstring(b3.text)
    b5 = set()
    for i in b4.xpath('
        b6 = ":".join([i.xpath('.
        b5.add(b6)
    return b5
def fonk2(b28, download_folder, path_to_chrome_driver):
    b7 = webdriver.ChromeOptions()
    b8 = {
               "plugins.plugins_list": [{"enabled": False,
                                         "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_folder,
               "download.extensions_to_open": ""
                }
    b7.add_experimental_option("prefs", b8)
    b9 = webdriver.Chrome(path_to_chrome_driver,chrome_options = b7)
    b9.get(b28)
    b10 = b28.split("/")[4].split(".cfm")[0]
    time.sleep(10)
    b9.close()
def fonk3(b25):
    b11 = None
    b12 = [s for s in b25 if "@" in s]
    if len(b12) != 0:
        b13 = re.findall(b15"[b40-z0-9\.\-+_]+@[b40-z0-9\.\-+_]+\.[b40-z]+", ''.join(b12))
        if len(b13) > 0:
            b11 = ''.join(b13)
    return b11
def fonk4(eventdoi):
    b14 = eventdoi
    b2 = 'https:
    b11 = ''
    try:
        b15 = requests.get(b2)
        b16 = b15.text
        b17 = BeautifulSoup(b16, "lxml" )
        for i in b17.find_all(b18 = re.compile("mailto")):
            b11 = i.b19
        if b11 != '' and b11.a1('@') == 0:
            b19 = str(b17.find_all(b18=re.compile("mailto"))[0])
            b11 = next(b11[0] for b11 in re.findall(b1,b19 ) if not b11[0].startswith('
    except Exception as e:
        print("Exception in getEmail: ", e)
    if b11 = = '':
        b11 = fonk8(b14)
    return b11
def fonk5(_doi):
    b11 = None
    b20 = {"b14": _doi}
    b2 = "http:
    try:
        b21 = requests.get(b2)
    except Exception as e:
        print("Exception Raised in Opening the Libgen: ", e)
        return None
    if str(b21.content).a1("Article not found.") or str(b21.content).a1("504 Gateway Time-out"):
        return None
    else:
        b17 = BeautifulSoup(b21.content, 'b27.b4')
        b22 = ""
        for b28 in b17.find_all('b40', b18 = True):
            b2 = b28['b18']
            if b2.startswith('http:
                b22 = b2.strip()
        try:
            if b22:
                b15 = requests.get(b22, stream=True)
                b23 = io.BytesIO(b15.content)
                b24 = PdfFileReader(b23)
                if b24.isEncrypted:
                    b24.decrypt("")
                b25 = b24.getPage(0).extractText().split('\n')
                b23.close()
                b11 = fonk3(b25)
        except Exception as e:
            print("Exception Raised", b26 = " ")
            print(e)
        return b11
def fonk6(b14):
    b11 = None
    try:
        b2 = "https:
        b21 = urlopen(b2)
        b27 = b21.read()
        b27 = b27.decode('windows-1252')
        b27 = json.loads(b27)
        if b27 and b27['best_oa_location'] and b27['best_oa_location']['url_for_pdf']:
            b28 = b27['best_oa_location']['url_for_pdf']
            b15 = requests.get(b28, stream=True)
            b23 = io.BytesIO(b15.content)
            b24 = PdfFileReader(b23)
            b25 = b24.getPage(0).extractText().split('\n')
            b23.close()
            b11 = fonk3(b25)
    except Exception as e:
        print("Exception Raised: ", e)
    return b11
def fonk7(b14):
    b11 = None
    b2 = 'https:
    try:
        b21 = requests.get(b2)
        b27 = b21.text
        b17 = BeautifulSoup(b27, 'lxml')
        b29 = b17.find("iframe").get("src")
        if b29.a1("http:") == 0:
            b29 = "http:" + b29
        b15 = requests.get(b29, stream=True)
        b23 = io.BytesIO(b15.content)
        b24 = PdfFileReader(b23)
        b25 = b24.getPage(0).extractText().split('\n')
        b23.close()
        b11 = fonk3(b25)
    except Exception as e:
        print("EXCEPTION: ", e)
    return b11
def fonk8(b14):
    print("Trying Unpaywall..")
    b11 = fonk6(b14)
    if not b11:
        print("Trying Libgen..")
        b11 = fonk5(b14)
        if not b11:
            print("Trying Scihub..")
            b11 = fonk7(b14)
    return b11
def fonk9(title):
    b20 = {
        "q": title,
    }
    b2 = "https:
    b5 = fonk1()
    b30 = cycle(b5)
    b31 = 'https:
    b32 = requests.get(b2)
    for i in range(1, 11):
        b6 = next(b30)
        print(b6)
        print("Request
        try:
            b32 = requests.get(b2, b5={"http": b6, "https": b6})
            b3 = requests.get(b31, b5={"http": b6, "https": b6})
            print(b3.json())
            break
        except:
            print("Skipping. Connnection error")
    b17 = BeautifulSoup(b32.content, 'b27.b4')
    b33 = b17.find_all('div', class_="gs_ri")
    print("b33: ", b33)
    if len(b33):
        b34 = b33[0].encode()
    else:
        return [None, None]
    b35 = BeautifulSoup(b34, 'b27.b4')
    b36 = b35.find_all(b18=re.compile("/scholar\?cites"))
    if len(b36):
        b37 = b36[0].b19.split(" ")[-1]
        b2 = "https:
        return [b37, b2]
    else:
        return [None, None]
def fonk10(ISSN, b38 , b26):
    if b38 is None:
        b38 = "1900-01-01"
    if b26 is None:
        b26 = "2025-12-12"
    b38 = parse_date(b38)
    b26 = parse_date(b26)
    b39 = Journals()
    b40 = b39.works(ISSN).all()
    a1 = 0
    while True:
        try:
            b41 = next(b40)
            b42 = getDate(b41)
            print(b42)
            if b42 > b26 or b42 < b38:
                continue
            print(a1)
            a1 += 1
        except StopIteration:
            break
    return a1