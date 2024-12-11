import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(b1,b2,b17,b10):
 for a in b2:
  if a not in b1:
   if len(a) > 1:
    if a not in b17:
     b1.append(a)
 for a in b1:
  if a not in b10:
   b10.append(a)
 return b1
def fonk2(nextUrl,b17,b10):
 b17.append(nextUrl)
 b1 = []
 b2 = []
 time.sleep(1)
 b3 = requests.get(nextUrl)
 b4 = b3.text
 b5 = BeautifulSoup(b4,'html.parser')
 b6 = b5.find('div',{'id': 'mw-content-text'})
 for link in b6.find_all('a', {'href': re.compile("^/wiki")}):
  if ':' not in link.get('href'):
   b7 = "https:
   b8 = b7.split('
   b2.append(str(b8[b9]))
 return fonk1(b1,b2,b17,b10)
def fonk3(listInUse, b11, b12, b13, b14, b15, b16,b17):
	for a in listInUse:
		if a not in b17:
			return a
	if b9 = = cmp(listInUse,b11):
		if len(b11)<1000:
			return fonk3(b12,b11, b12, b13, b14, b15, b16,b17)
	if b9 = = cmp(listInUse,b12):
		if len(b12)<1000:
			return fonk3(b13,b11, b12, b13, b14, b15, b16,b17)
	if b9 = = cmp(listInUse,b13):
		if len(b13)<1000:
			return fonk3(b14,b11, b12, b13, b14, b15, b16,b17)
	if b9 = = cmp(listInUse,b14):
		if len(b14)<1000:
			return fonk3(b15,b11, b12, b13, b14, b15, b16,b17)
	if b9 = = cmp(listInUse,b15):
		if len(b15)<1000:
			return fonk3(b16,b11, b12, b13, b14, b15, b16,b17)
	return 'links not found'
def fonk4(b18,b11,b12,b13,b14,b15,b16):
	if b18 in b11:
		return b11
	elif b18 in b12:
		return b12
	elif b18 in b13:
		return b13
	elif b18 in b14:
		return b14
	else:
		return b15
def fonk5(b26):
	b10 = []
	b11 = []
	b12 = []
	b13 = []
	b14 = []
	b15 = []
	b16 = []
	b17 = []
	b10.append(b26)
	b11.append(b26)
	while len(b10) < 1000:
		b18 = fonk3(b11,b11,b12,b13,b14,b15,b16,b17)
		if b18 = = 'links not found':
			print "crawling ends:no further links found"
			break
		else:
			b19 = fonk4(b18,b11,b12,b13,b14,b15,b16)
			if b19 = = b11:
				b20 = fonk2(b18,b17,b10)
				for a in b20:
					b12.append(a)
			elif b19 = = b12:
				b21 = fonk2(b18,b17,b10)
				for b in b21:
					if (b not in b11) and (b not in b12):
						b13.append(b)
			elif b19 = = b13:
				b22 = fonk2(b18,b17,b10)
				for c in b22:
					if (c not in b12) and (b not in b13):
						b14.append(c)
			elif b19 = = b14:
				b23 = fonk2(b18,b17,b10)
				for d in b23:
					if (d not in b13) and (d not in b14):
						b15.append(d)
			elif b19 = = b15:
				b24 = fonk2(b18,b17,b10)
				for e in b24:
					if (e not in b14) and (e not in b15):
						b16.append(e)
	b25 = open('TASK 1-E.txt', 'w')
	for i,b26 in enumerate(b10):
		if i < 1000:
		 b25.write(str(b26.lower()) + "\n")
	b25.close()
b26 = "https:
fonk5(b26)