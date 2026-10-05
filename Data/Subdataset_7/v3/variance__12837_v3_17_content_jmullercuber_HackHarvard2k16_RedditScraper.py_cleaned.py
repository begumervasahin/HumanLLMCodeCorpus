import json
import http.client
import string
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, b14, a2):
        b1 = self.fonk3(b14)
        b2 = []
        for i in range(min(a2, len(b1))):
            b3 = b1[i]['data']['permalink']
            b4 = self.fonk4(b3)
            b2.extend(b4)
        return b2
    def fonk3(self, b14):
        with http.client.HTTPSConnection('www.reddit.com') as connection:
            connection.request("GET", f"/r/{b14}/hot/.json")
            b5 = connection.getresponse()
            b1 = json.loads(b5.read())['data']['children']
        return b1
    def fonk4(self, post_link):
        b6 = self.fonk5(post_link)
        b7 = []
        for comment in b6['data']['children']:
            if 'b10' in comment['data']:
                self.a1 = 0
                b8 = self.fonk6(comment)
                b7.extend(b8)
        return b7
    def fonk5(self, post_link):
        with http.client.HTTPSConnection('www.reddit.com') as connection:
            connection.request("GET", f"{post_link}/.json?b9 = 500")
            b5 = connection.getresponse()
            b6 = json.loads(b5.read())
        return b6
    def fonk6(self, comment):
        b8 = []
        b10 = ''.join(filter(lambda x: x in string.printable, comment['data']['b10']))
        b8.append(b10)
        if 'replies' in comment['data'] and comment['data']['replies'] != '' and self.a1 < 1:
            for reply in comment['data']['replies']['data']['children']:
                if 'kind' in reply and reply['kind'] != 'more':
                    self.a1 += 1
                    b11 = self.fonk6(reply)
                    b8.extend(b11)
        return b8
if b12 = = "__main__":
    b13 = class1()
    b14 = 'Python'
    a2 = 3
    b2 = b13.fonk2(b14, a2)
    for document in b2:
        print(document)