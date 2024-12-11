import json
import http.client
import string
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, subreddit, qty):
        b1 = http.client.HTTPSConnection('www.reddit.com')
        b1.request("GET", f"/r/{subreddit}/hot/.json")
        b2 = b1.getresponse()
        b3 = b2.read()
        b3 = json.loads(b3)
        b4 = []
        for i in range(qty):
            b5 = b3['data']['children'][i]['data']['b5']
            b4.extend(self.fonk3(b5))
        b1.close()
        return b4
    def fonk3(self, link):
        b1 = http.client.HTTPSConnection('www.reddit.com')
        b1.request("GET", f"{link}/.json?b6 = 500")
        b2 = b1.getresponse()
        b7 = b2.read()
        b7 = json.loads(b7)
        b8 = b7[1]['data']['children']
        b9 = []
        for comment in b8:
            if 'b11' in comment['data']:
                self.a1 = 0
                b9.extend(self.fonk4(comment))
        return b9
    def fonk4(self, comment):
        b10 = []
        b11 = ''.join(filter(lambda x: x in string.printable, comment['data']['b11']))
        b10.append(b11)
        if comment['data']['replies'] != '' and self.a1 < 1:
            for reply in comment['data']['replies']['data']['children']:
                if reply['kind'] != 'more':
                    self.a1 += 1
                    b10.extend(self.fonk4(reply))
        return b10