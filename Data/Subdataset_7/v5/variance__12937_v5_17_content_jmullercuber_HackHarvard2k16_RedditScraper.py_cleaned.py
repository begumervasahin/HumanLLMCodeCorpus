import json
import http.client
import string
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, subreddit, qty):
        b1 = self.fonk3(f"/r/{subreddit}/hot/.json")
        b2 = []
        for i in range(min(qty, len(b1))):
            b3 = b1[i]['b6']['b3']
            b2.extend(self.fonk4(b3))
        return b2
    def fonk3(self, url):
        b4 = http.client.HTTPSConnection('www.reddit.com')
        b4.request("GET", url)
        b5 = b4.getresponse()
        b6 = b5.read()
        b4.close()
        return json.loads(b6)['b6']['children']
    def fonk4(self, link):
        b7 = self.fonk3(f"{link}/.json?limit=500")
        b8 = b7[1]['b6']['children']
        b9 = []
        for comment in b8:
            if 'b11' in comment['b6']:
                self.a1 = 0
                b9.extend(self.fonk5(comment))
        return b9
    def fonk5(self, comment):
        b10 = []
        b11 = ''.join(filter(lambda x: x in string.printable, comment['b6']['b11']))
        b10.append(b11)
        if comment['b6']['replies'] and self.a1 < 1:
            for reply in comment['b6']['replies']['b6']['children']:
                if reply['kind'] != 'more':
                    self.a1 += 1
                    b10.extend(self.fonk5(reply))
        return b10