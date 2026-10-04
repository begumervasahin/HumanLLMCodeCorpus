import json
import http.client
import string
from Scraper import Scraper
class class1(Scraper):
    b1 = 'www.reddit.com'
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, subreddit, qty):
        b2 = self.fonk5(subreddit)
        b3 = []
        for i in range(qty):
            b4 = b2['data']['children'][i]['data']['b4']
            b3.extend(self.fonk3(b4))
        return b3
    def fonk3(self, b4):
        b5 = self.fonk6(b4)
        b6 = b5[1]['data']['children']
        b7 = []
        for comment in b6:
            if 'b9' in comment['data']:
                self.a1 = 0
                b7.extend(self.fonk4(comment))
        return b7
    def fonk4(self, comment):
        b8 = []
        b9 = ''.join(filter(lambda x: x in string.printable, comment['data']['b9']))
        b8.append(b9)
        if comment['data']['replies'] and self.a1 < 1:
            for reply in comment['data']['replies']['data']['children']:
                if reply['kind'] != 'more':
                    self.a1 += 1
                    b8.extend(self.fonk4(reply))
        return b8
    def fonk5(self, subreddit):
        b10 = http.client.HTTPSConnection(self.b1)
        b10.request("GET", f"/r/{subreddit}/hot/.json")
        b11 = b10.getresponse()
        b2 = json.loads(b11.read())
        b10.close()
        return b2
    def fonk6(self, b4):
        b10 = http.client.HTTPSConnection(self.b1)
        b10.request("GET", f"{b4}.json?b12 = 500")
        b11 = b10.getresponse()
        b5 = json.loads(b11.read())
        b10.close()
        return b5