from bs4 import BeautifulSoup
import urllib3
import requests
import asyncio
class Scraper:
	def __init__(self):
		self.rates = {}
		self.strs = {}
		self.keys = {}
		self.key = 0
		self.scrape()
	def try_generate_key(self, cStr):
		if cStr not in self.strs:
			self.strs[cStr] = self.key
			self.keys[self.key] = cStr
			self.key += 1
	def scrape(self):
		url = "http:
		http = urllib3.PoolManager()
		request_main = http.request('GET', url)
		soup_main = BeautifulSoup(request_main.data, "lxml")
		target = soup_main.find("ul", class_="currencyList ratestable")
		for a in target.find_all("a"):
			self.try_generate_key(a.text)
			page_url = a['href'] + "&amount=1"
			request = http.request('GET', page_url)
			soup = BeautifulSoup(request.data, "lxml")
			table = soup.find_all("table")
			for t in table:
				t_body = t.find("tbody")
				rows = t_body.find_all("tr")
				for r in rows:
					c = r.find_all("td")
					c = [item.text.strip() for item in c]
					self.try_generate_key(c[0])
					forward = (self.strs[a.text], self.strs[c[0]])
					if forward not in self.rates:
						self.rates[forward] = float(c[1])
						self.rates[(forward[1], forward[0])] = float(c[2])
if __name__ == '__main__':
	s = Scraper()
	print(s.rates)