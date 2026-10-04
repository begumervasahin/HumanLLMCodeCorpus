import json
import requests
from bs4 import BeautifulSoup
class class1:
    b1 = 'https:
    b2 = {'X-Requested-With': 'XMLHttpRequest'}
    def fonk1(self):
        self.b3 = self.fonk2()
    def fonk2(self):
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
    def fonk3(self):
        b4 = self.fonk4()
        print(f"{len(b4)} b4 found")
        for b9 in b4:
            print(b9)
    def fonk4(self, b5 = 3):
        b4 = []
        self.b3['pageNumber'] = 0
        while self.b3['pageNumber'] < b5:
            b6 = self.fonk5()
            b7 = BeautifulSoup(b6.text, "lxml")
            if not b7.requisition:
                break
            b4.extend(self.fonk6(b7))
            self.b3['pageNumber'] += 1
        return b4
    def fonk5(self):
        b8 = {
            'searchRequestJson': json.dumps(self.b3),
            'clientOffset': '-300'
        }
        b6 = requests.post(self.b1, data=b8, headers=self.b2)
        b6.raise_for_status()
        return b6
    def fonk6(self, b7):
        b4 = []
        for requisition in b7.findAll('requisition'):
            b9 = {
                'jobid': requisition.jobid.text,
                'title': self.fonk7(requisition),
                'location': requisition.location.text
            }
            b4.append(b9)
        return b4
    def fonk7(self, requisition):
        return requisition.postingtitle.text if requisition.postingtitle else requisition.retailpostingtitle.text
if b10 = = '__main__':
    b11 = class1()
    b11.fonk3()