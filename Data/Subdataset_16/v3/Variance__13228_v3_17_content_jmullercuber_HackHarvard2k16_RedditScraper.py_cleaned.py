import json
import http.client as httplib
import string
class class1:
    def fonk1(self, b14, a3):
        raise NotImplementedError("This method should be overridden.")
    def fonk2(self, link):
        raise NotImplementedError("This method should be overridden.")
    def fonk3(self, comment):
        raise NotImplementedError("This method should be overridden.")
class class2(class1):
    def fonk4(self):
        self.a1 = 1
        self.a2 = 0
    def fonk5(self, b14, a3):
        b1 = httplib.HTTPSConnection('www.reddit.com')
        b1.request("GET", f"/r/{b14}/hot/.json")
        b2 = b1.getresponse()
        b3 = json.loads(b2.read())
        b4 = []
        for i in range(min(a3, len(b3['data']['children']))):
            b5 = b3['data']['children'][i]['data']['b5']
            b4.extend(self.fonk6(b5))
        b1.close()
        return b4
    def fonk6(self, link):
        b1 = httplib.HTTPSConnection('www.reddit.com')
        b1.request("GET", f"{link}.json?b6 = 500")
        b2 = b1.getresponse()
        b7 = json.loads(b2.read())
        b8 = b7[1]['data']['children']
        b9 = []
        for comment in b8:
            if 'b11' in comment['data']:
                self.a2 = 0
                b9.extend(self.fonk7(comment))
        b1.close()
        return b9
    def fonk7(self, comment):
        b10 = []
        b11 = ''.join(filter(lambda x: x in string.printable, comment['data']['b11']))
        b10.append(b11)
        if comment['data'].get('replies') and self.a2 < self.a1:
            for reply in comment['data']['replies']['data']['children']:
                if reply['kind'] != 'more':
                    self.a2 += 1
                    b10.extend(self.fonk7(reply))
                    self.a2 -= 1
        return b10
if b12 = = "__main__":
    b13 = class2()
    b14 = "python"
    a3 = 5
    b4 = b13.fonk5(b14, a3)
    for doc in b4:
        print(doc)