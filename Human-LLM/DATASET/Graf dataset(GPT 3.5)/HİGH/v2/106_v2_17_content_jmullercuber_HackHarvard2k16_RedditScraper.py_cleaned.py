import json
import http.client
import string
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, b16, a2):
        b1 = http.client.HTTPSConnection('www.reddit.com')
        b1.request("GET", f"/r/{b16}/hot/.json")
        b2 = b1.getresponse()
        b3 = b2.read()
        b3 = json.loads(b3)
        b4 = []
        for i in range(a2):
            b5 = b3['data']['children'][i]['data']['permalink']
            b6 = self.fonk3(b5)
            b4.extend(b6)
        b1.close()
        return b4
    def fonk3(self, post_link):
        b1 = http.client.HTTPSConnection('www.reddit.com')
        b1.request("GET", f"{post_link}/.json?b7 = 500")
        b2 = b1.getresponse()
        b8 = b2.read()
        b8 = json.loads(b8)
        b9 = b8[1]['data']['children']
        b10 = []
        for comment in b9:
            if 'b12' in comment['data']:
                self.a1 = 0
                b11 = self.fonk4(comment)
                b10.extend(b11)
        b1.close()
        return b10
    def fonk4(self, comment):
        b11 = []
        b12 = ''.join(filter(lambda x: x in string.printable, comment['data']['b12']))
        b11.append(b12)
        if 'replies' in comment['data'] and comment['data']['replies'] != '' and self.a1 < 1:
            for reply in comment['data']['replies']['data']['children']:
                if 'kind' in reply and reply['kind'] != 'more':
                    self.a1 += 1
                    b13 = self.fonk4(reply)
                    b11.extend(b13)
        return b11
if b14 = = "__main__":
    b15 = class1()
    b16 = 'Python'
    a2 = 3
    b4 = b15.fonk2(b16, a2)
    for document in b4:
        print(document)