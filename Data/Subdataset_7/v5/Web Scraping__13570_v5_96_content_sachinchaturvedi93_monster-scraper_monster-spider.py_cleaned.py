import scrapy
import json
from bs4 import BeautifulSoup
from bs4.element import Comment
def fonk1(element):
    b1 = ['style', 'script', 'head', 'title', 'meta', '[document]']
    if element.parent.b5 in b1:
        return False
    if isinstance(element, Comment):
        return False
    return True
def fonk2(html_body):
    b2 = BeautifulSoup(html_body, 'html.parser')
    b3 = b2.findAll(text=True)
    b4 = filter(is_element_visible, b3)
    return " ".join(t.strip() for t in b4)
class class1(scrapy.Spider):
    b5 = 'monster_spider'
    b6 = ['monster.com']
    b7 = [
        f'https:
        for i in range(2)
    ]
    def fonk3(self, response):
        b8 = json.loads(response.body)
        for result in b8:
            b9 = result.get('MusangKingId')
            if b9:
                b10 = f'https:
                yield response.follow(b10, b11 = self.parse_job_detail)
    def fonk4(self, response):
        b12 = json.loads(response.body)
        b13 = {
            "JobID": b12.get('jobId', ''),
            "Title": b12['companyInfo'].get('companyHeader', ''),
            "Location": b12['companyInfo'].get('jobLocation', ''),
            "Company": b12['companyInfo'].get('b5', ''),
            "Job Category": b12.get("jobCategory", ''),
            "Description": fonk2(b12.get("jobDescription", '')),
            "Company Size": b12['companyInfo'].get("companySizeName", '')
        }
        for info in b12['summary']['info']:
            b13[info['title']] = info.get('text', '')
        return b13