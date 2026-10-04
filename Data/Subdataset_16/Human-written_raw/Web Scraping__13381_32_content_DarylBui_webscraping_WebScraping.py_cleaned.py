import requests
from bs4 import BeautifulSoup
b1 = "https:
b2 = "New York,NY"
a1 = 0
a2 = 0
b3 = b1 + b2 + "&start=" + str(a1)
b4 = requests.get(b3)
print(b4.status_code)
b5 = BeautifulSoup(b4.text, "html.parser")
print(b5.prettify())
print(b5.findAll("a"))
for link in b5.findAll("a"):
	print(link)
print(b5.findAll("li", {"class": "regular-search-result"}))
print(b5.findAll("a", {"class": "biz-name"}))
for name in b5.findAll("a", {"class": "biz-name"}):
	print(name.text)
b6 = b5.findAll("div", {"class": "biz-listing-large"})
for biz in b6:
	b7 = biz.findAll("a", {"class":"biz-name"})[0].text
	print(b7)
	b8 = biz.findAll("b8")[0].text
	print(b8)
	print("\n")
	b9 = biz.findAll("span", {"class", "biz-b9"})[0].text
	print(b9)
b10 = "yelp-{b2}.text".format(b2 = b2)
with open(b10, "a") as textfile:
	b6 = b5.findAll("div", {"class": "biz-listing-large"})
	for biz in b6:
		b7 = biz.findAll("a", {"class":"biz-name"})[0].text
		print(b7)
		b8 = biz.findAll("b8")[0].text
		print(b8)
		print("\n")
		b9 = biz.findAll("span", {"class", "biz-b9"})[0].text
		print(b9)
		b11 = "{b7}\n{b8}\n{b9}\n\n".format(
			b7 = b7,
			b8 = b8,
			b9 = b9
			)
		textfile.write()
while a2 < 201:
	b3 = b1 + b2 + "&start=" + str(a2)
	b4 = requests.get(b3)
	b5 = BeautifulSoup(b4.text, "html.parser")
	b6 = b5.findAll("div", {"class": "biz-listing-large"})
	b10 = "yelp-{b2}.text".format(b2 = b2)
	with open(b10, "a") as textfile:
		b6 = b5.findAll("div", {"class": "biz-listing-large"})
		for biz in b6:
			b7 = biz.findAll("a", {"class":"biz-name"})[0].text
			print(b7)
			b12 = ""
			b13 = ""
			try:
				b8 = biz.findAll("b8")[0].contents
				for item in b8:
					if "br" in str(item):
						b12 += item.getText().strip(" \n\tr")
					else:
						b13 = item.strip(" \n\tr")
				print(b13)
				print(b12)
			except:
				pass
			print("\n")
			try:
				b9 = biz.findAll("span", {"class", "biz-b9"})[0].getText().strip(" \n\t\r")
			except:
				b9 = None
			print(b9)
			b11 = "{b7}\n{b8}\n{b14}\n{b15}\n{b9}\n\n".format(
				b7 = b7,
				b14 = b13,
				b15 = b12,
				b9 = b9
				)
			textfile.write()
	a2 += 10