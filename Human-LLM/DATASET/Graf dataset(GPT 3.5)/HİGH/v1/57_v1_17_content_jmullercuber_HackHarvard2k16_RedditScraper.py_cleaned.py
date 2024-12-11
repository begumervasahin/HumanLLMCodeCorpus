import json
import http.client
import string
class class1:
    a1 = 0
    def fonk1(self, b13, a2):
        b1 = http.client.HTTPSConnection('www.reddit.com')
        b1.request("GET", "/r/" + b13 + "/hot/.json")
        b2 = b1.getresponse()
        b3 = b2.read()
        b3 = json.loads(b3)
        b4 = []
        for i in range(a2):
            b4.extend(self.fonk2(b3['data']['children'][i]['data']['permalink']))
        b1.close()
        return b4
    def fonk2(self, link):
        b1 = http.client.HTTPSConnection('www.reddit.com')
        b1.request("GET", link + '/.json?b5 = 500')
        b2 = b1.getresponse()
        b6 = b2.read()
        b6 = json.loads(b6)
        b7 = b6[1]['data']['children']
        b8 = []
        for comment in b7:
            if 'b10' in comment['data']:
                self.a1 = 0
                b8.extend(self.fonk3(comment))
        return b8
    def fonk3(self, comment):
        b9 = []
        b10 = ''.join(filter(lambda x: x in string.printable, comment['data']['b10']))
        b9.append(b10)
        if 'replies' in comment['data'] and comment['data']['replies'] != '' and self.a1 < 1:
            for reply in comment['data']['replies']['data']['children']:
                if 'kind' in reply and reply['kind'] != 'more':
                    self.a1 += 1
                    b9.extend(self.fonk3(reply))
        return b9
if b11 = = "__main__":
    b12 = class1()
    b13 = 'Python'
    a2 = 3
    b4 = b12.fonk1(b13, a2)
    for document in b4:
        print(document)