import json
import requests
from bs4 import BeautifulSoup
class AppleJobsScraper:
    BASE_URL = 'https:
    HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
    def __init__(self):
        self.search_request = self._initialize_search_request()
    def _initialize_search_request(self):
        return {
            "searchString": "",
            "jobType": 0,
            "sortBy": "req_open_dt",
            "sortOrder": "1",
            "language": None,
            "autocomplete": None,
            "delta": 0,
            "numberOfResults": 0,
            "pageNumber": None,
            "internalExternalIndicator": 0,
            "lastRunDate": 0,
            "countryLang": None,
            "filters": {
                "locations": {
                    "location": [{
                        "type": 0,
                        "code": "USA",
                        "countryCode": None,
                        "stateCode": None,
                        "cityCode": None,
                        "cityName": None
                    }]
                },
                "languageSkills": None,
                "jobFunctions": None,
                "retailJobSpecs": None,
                "businessLine": None,
                "hiringManagerId": None
            },
            "requisitionIds": None
        }
    def scrape(self):
        jobs = self.scrape_jobs()
        print(f"{len(jobs)} jobs found")
        for job in jobs:
            print(job)
    def scrape_jobs(self, max_pages=3):
        jobs = []
        self.search_request['pageNumber'] = 0
        while self.search_request['pageNumber'] < max_pages:
            response = self._fetch_jobs_page()
            soup = BeautifulSoup(response.text, "lxml")
            if not soup.requisition:
                break
            jobs.extend(self._parse_jobs(soup))
            self.search_request['pageNumber'] += 1
        return jobs
    def _fetch_jobs_page(self):
        payload = {
            'searchRequestJson': json.dumps(self.search_request),
            'clientOffset': '-300'
        }
        response = requests.post(self.BASE_URL, data=payload, headers=self.HEADERS)
        response.raise_for_status()
        return response
    def _parse_jobs(self, soup):
        jobs = []
        for requisition in soup.findAll('requisition'):
            job = {
                'jobid': requisition.jobid.text,
                'title': self._get_job_title(requisition),
                'location': requisition.location.text
            }
            jobs.append(job)
        return jobs
    def _get_job_title(self, requisition):
        return requisition.postingtitle.text if requisition.postingtitle else requisition.retailpostingtitle.text
if __name__ == '__main__':
    scraper = AppleJobsScraper()
    scraper.scrape()