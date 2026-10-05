import scrapy
import json
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
def fonk1(element):
    if element.parent.b4 in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(body):
    b1 = BeautifulSoup(body, 'html.parser')
    b2 = b1.findAll(text=True)
    b3 = filter(tag_visible, b2)
    return " ".join(t.strip() for t in b3)
class class1(scrapy.Spider):
    b4 = 'monster-spider'
    b5 = ['monster.com']
    b6 = ['https:
    def fonk3(self, response):
        b7 = json.loads(response.body)
        for b11 in b7['data']:
            try:
                b8 = b11['MusangKingId']
                b9 = 'https:
                yield response.follow(b9, b10 = self.parse_detail)
            except Exception as e:
                self.logger.error('Error parsing job details: %s', e)
    def fonk4(self, response):
        b11 = json.loads(response.body)
        b12 = {
            "JobID": b11.get('jobId', ''),
            "Title": b11['companyInfo'].get('companyHeader', ''),
            "Location": b11['companyInfo'].get('jobLocation', ''),
            "Company": b11['companyInfo'].get('b4', ''),
            "Job Category": b11.get("jobCategory", ''),
            "Description": fonk2(b11.get("jobDescription", '')),
            "Company Size": b11['companyInfo'].get("companySizeName", '')
        }
        b13 = b11['summary'].get('b13', [])
        for i in b13:
            b12[i['title']] = i['text']
        yield b12