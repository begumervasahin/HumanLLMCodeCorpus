import json
import requests
from bs4 import BeautifulSoup
class class1:
    def fonk1(self):
        self.b1 = {
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
    def fonk2(self):
        b2 = self.fonk3()
        print(f"{len(b2)} b2 found")
        for b10 in b2:
            print(b10)
    def fonk3(self, b3 = 3):
        b2 = []
        a1 = 0
        self.b1['pageNumber'] = a1
        while a1 < b3:
            b4 = {
                'searchRequestJson': json.dumps(self.b1),
                'clientOffset': '-300'
            }
            b5 = requests.post(
                b6 = 'https:
                b7 = b4,
                b8 = {'X-Requested-With': 'XMLHttpRequest'}
            )
            b9 = BeautifulSoup(b5.text, "lxml")
            if not b9.requisition:
                break
            for requisition in b9.findAll('requisition'):
                b10 = {
                    'jobid': requisition.jobid.text,
                    'title': requisition.postingtitle.text if requisition.postingtitle else requisition.retailpostingtitle.text,
                    'location': requisition.location.text
                }
                b2.append(b10)
            a1 += 1
            self.b1['pageNumber'] = a1
        return b2
if b11 = = '__main__':
    b12 = class1()
    b12.fonk2()