import json
import requests
from bs4 import BeautifulSoup
class AppleJobsScraper:
    def __init__(self):
        self.search_request = {
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
        pageno = 0
        self.search_request['pageNumber'] = pageno
        while pageno < max_pages:
            payload = {
                'searchRequestJson': json.dumps(self.search_request),
                'clientOffset': '-300'
            }
            response = requests.post(
                url='https:
                data=payload,
                headers={'X-Requested-With': 'XMLHttpRequest'}
            )
            soup = BeautifulSoup(response.text, "lxml")
            if not soup.requisition:
                break
            for requisition in soup.findAll('requisition'):
                job = {
                    'jobid': requisition.jobid.text,
                    'title': requisition.postingtitle.text if requisition.postingtitle else requisition.retailpostingtitle.text,
                    'location': requisition.location.text
                }
                jobs.append(job)
            pageno += 1
            self.search_request['pageNumber'] = pageno
        return jobs
if __name__ == '__main__':
    scraper = AppleJobsScraper()
    scraper.scrape()