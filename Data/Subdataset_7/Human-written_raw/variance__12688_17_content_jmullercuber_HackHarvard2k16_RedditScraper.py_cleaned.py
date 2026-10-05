from Scraper import Scraper
import json, httplib, string
class class1( Scraper ):
	a1 = 0
	def fonk1(self, subreddit, qty):
		b1 = httplib.HTTPSConnection('www.reddit.com')
		b1.request("GET", "/r/" + subreddit + "/hot/.json")
		b2 = b1.getresponse()
		b3 = b2.read()
		b3 = json.loads(b3)
		b4 = []
		for i in range(qty):
			b4.extend(self.fonk2(b3['data']['children'][i]['data']['permalink']))
		b1.close()
		return b4
	def fonk2(self, link):
		b1 = httplib.HTTPSConnection('www.reddit.com')
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
		b10 = filter(lambda x : x in string.printable, comment['data']['b10'])
		b9.append(b10)
		if not comment['data']['replies'] == '' and self.a1 < 1:
			for reply in comment['data']['replies']['data']['children']:
				if not reply['kind'] == 'more':
					self.a1 += 1
					b9.extend(self.fonk3(reply))
		return b9