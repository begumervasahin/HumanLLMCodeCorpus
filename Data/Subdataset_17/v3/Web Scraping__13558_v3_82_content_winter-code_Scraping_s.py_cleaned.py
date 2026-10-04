import json
import requests
from bs4 import BeautifulSoup
class AppleJobsScraper:
    def __init__(self):
        self.base_url = 'https:
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}
        self.search_request = self._initialize_search_request()
    @staticmethod
    def _initialize_search_request():
        return {
            "searchString": "",
            "jobType": 0,
            "sortBy": "req_open_dt",
            "sortOrder": "1",
            "language": None,
            "autocomplete": None,
            "delta": 0,
            "numberOfResults": 0,
            "pageNumber": 0,
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
        jobs = self._scrape_jobs()
        print(f"Total jobs found: {len(jobs)}")
        for job in jobs:
            print(job)
    def _scrape_jobs(self, max_pages=3):
        jobs = []
        for page_number in range(max_pages):
            self.search_request['pageNumber'] = page_number
            payload = {
                'searchRequestJson': json.dumps(self.search_request),
                'clientOffset': '-300'
            }
            response = requests.post(url=self.base_url, data=payload, headers=self.headers)
            soup = BeautifulSoup(response.text, "lxml")
            if not soup.requisition:
                break
            jobs.extend(self._extract_jobs(soup))
        return jobs
    @staticmethod
    def _extract_jobs(soup):
        jobs = []
        for requisition in soup.find_all('requisition'):
            job = {
                'jobid': requisition.jobid.text,
                'title': requisition.postingtitle.text if requisition.postingtitle else requisition.retailpostingtitle.text,
                'location': requisition.location.text
            }
            jobs.append(job)
        return jobs
if __name__ == '__main__':
    scraper = AppleJobsScraper()
    scraper.scrape()