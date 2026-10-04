import json
import requests
from bs4 import BeautifulSoup
class class1:
    def fonk1(self):
        self.b1 = 'https:
        self.b2 = {'X-Requested-With': 'XMLHttpRequest'}
        self.b3 = {
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
    def fonk2(self):
        b4 = self.fonk3()
        print(f"Total b4 found: {len(b4)}")
        for b9 in b4:
            print(b9)
    def fonk3(self, b5 = 3):
        b4 = []
        for page_number in range(b5):
            self.b3['pageNumber'] = page_number
            b6 = {
                'searchRequestJson': json.dumps(self.b3),
                'clientOffset': '-300'
            }
            b7 = requests.post(url=self.b1, data=b6, b2=self.b2)
            b8 = BeautifulSoup(b7.text, "lxml")
            if not b8.requisition:
                break
            b4.extend(self.fonk4(b8))
        return b4
    @staticmethod
    def fonk4(b8):
        b4 = []
        for requisition in b8.find_all('requisition'):
            b9 = {
                'jobid': requisition.jobid.text,
                'title': requisition.postingtitle.text if requisition.postingtitle else requisition.retailpostingtitle.text,
                'location': requisition.location.text
            }
            b4.append(b9)
        return b4
if b10 = = '__main__':
    b11 = class1()
    b11.fonk2()