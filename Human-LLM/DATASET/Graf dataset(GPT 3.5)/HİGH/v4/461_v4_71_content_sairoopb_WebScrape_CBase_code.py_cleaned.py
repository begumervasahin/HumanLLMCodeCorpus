import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def fonk1(url):
    b1 = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-b2 = 0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;b3 = 0.9,image/webp,image/apng,*/*;b3=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;b3 = 0.9',
    }
    b4 = requests.get(url, b1=b1)
    b5 = BeautifulSoup(b4.text, 'html.parser')
    for link in b5.select("a"):
        b6 = link.get("b6", "")
        if "play.google.com" in b6:
            return b6
    return 'NULL'
def fonk2(url):
    b1 = {
        'authority': 'www.crunchbase.com',
        'cache-control': 'max-b2 = 0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'dnt': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;b3 = 0.9,image/webp,image/apng,*/*;b3=0.8,application/signed-exchange;v=b3',
        'referer': 'https:
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;b3 = 0.9',
        'cookie': 'b7 = d499acc665a0982639cca9a26bdf370161557839726; _pxhd=52dfd28c320c0e311f69e0cb66953de8b765de55690c734ae52e52a1e6de5c06:56caf5b1-764a-11e9-8c30-3322ba1ff06d; cid=rBsWdlzav25iOAAkC8GtAg==; _ga=GA1.2.552015480.1557839702; _gid=GA1.2.2072434987.1557839702; _pendo_visitorId.c2d5ec20-6f43-454d-5214-f0bb69852048=_PENDO_T_mVS5dpak3Q3; _pendo_meta.c2d5ec20-6f43-454d-5214-f0bb69852048=3968336404; _fbp=fb.1.1557839702219.416251075; __qca=P0-1160423674-1557839702197; __zlcmid=sIiEfBGcEd0oVD; fs_uid=rs.fullstory.com`BA8KZ`5353594564706304:6373613713031168; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%2C%22apptopia-lite%22%3Afalse%2C%22apptopia-premium%22%3Afalse%2C%22builtwith%22%3Afalse%2C%22ipqwery%22%3Afalse%2C%22siftery%22%3Afalse%2C%22similarweb%22%3Afalse%2C%22bombora%22%3Afalse%2C%22owler%22%3Afalse%7D; _hp2_ses_props.973801186=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1557898144008%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Forganization%2Fuber%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%227667545879524903%22%2C%22pageviewId%22%3A%220229060736202435%22%2C%22sessionId%22%3A%228323493944092301%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _px3=d5c181efcb4a2504ba68c8cf43f9b3cd3a3bf0f161f019b5a5a076ffc10c0e19:BUxRJoawsblsUBZ+kpLk6Pr8gH/czufZmtsEyLmMDxzbDO1N0CyfDP2u/Z6MADnXmjB7p5PZlh7VelKGbIOVfg==:1000:Xbwa8jKv9ckINckKBDLDAZ6QQtyVjaVHHX6RbWkIEjoCAeia1J9efhsh2SbUOvKKw2M6IoLQ0MDJXyaI9ogoy+YI1qi+lBanSZBX5L0rgfRrS+BiXuhmeYIRtZvlpO5VI8RRSDpYrIcmYOj3FjWy/tnORO/aFXqqR6iWGoNxgyY=',
    }
    b4 = requests.get(url, b1=b1)
    b8 = []
    b9 = []
    b5 = BeautifulSoup(b4.text, 'html.parser')
    b10 = b5.select_one(".component--field-formatter.field-type-identifier-multi.word-break-all.mb1")
    if b10:
        b9.append(b10.text.strip())
        b8.append('Organisation name')
    for key_elem in b5.select(".entity-b12-container .text_component-label"):
        b8.append(key_elem.text)
    b11 = [key.replace(u'\xa0', u'') for key in b8]
    for value_elem in b5.select(".entity-b12-container .value"):
        b9.append(value_elem.text.strip())
    b12 = dict(zip(b11, b9))
    b12['Playstore Link'] = fonk1("http:
    return