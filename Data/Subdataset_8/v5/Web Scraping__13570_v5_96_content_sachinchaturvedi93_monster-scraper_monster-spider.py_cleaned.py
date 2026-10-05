import scrapy
import json
from bs4 import BeautifulSoup
from bs4.element import Comment
def is_element_visible(element):
    non_visible_tags = ['style', 'script', 'head', 'title', 'meta', '[document]']
    if element.parent.name in non_visible_tags:
        return False
    if isinstance(element, Comment):
        return False
    return True
def extract_visible_text(html_body):
    soup = BeautifulSoup(html_body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(is_element_visible, texts)
    return " ".join(t.strip() for t in visible_texts)
class MonsterSpider(scrapy.Spider):
    name = 'monster_spider'
    allowed_domains = ['monster.com']
    start_urls = [
        f'https:
        for i in range(2)
    ]
    def parse(self, response):
        results = json.loads(response.body)
        for result in results:
            job_id = result.get('MusangKingId')
            if job_id:
                detail_url = f'https:
                yield response.follow(detail_url, callback=self.parse_job_detail)
    def parse_job_detail(self, response):
        job_data = json.loads(response.body)
        job_detail = {
            "JobID": job_data.get('jobId', ''),
            "Title": job_data['companyInfo'].get('companyHeader', ''),
            "Location": job_data['companyInfo'].get('jobLocation', ''),
            "Company": job_data['companyInfo'].get('name', ''),
            "Job Category": job_data.get("jobCategory", ''),
            "Description": extract_visible_text(job_data.get("jobDescription", '')),
            "Company Size": job_data['companyInfo'].get("companySizeName", '')
        }
        for info in job_data['summary']['info']:
            job_detail[info['title']] = info.get('text', '')
        return job_detail