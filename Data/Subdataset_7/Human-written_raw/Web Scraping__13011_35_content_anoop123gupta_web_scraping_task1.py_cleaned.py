import requests
import pprint
import json
import os
from bs4 import BeautifulSoup
def fonk1():
	if os.path.isfile("cache_file_for_task_1.json"):
		with open("cache_file_for_task_1.json","r+")as data:
			b1 = json.load(data)
			return(b1)
	else:
		b2 = 'https:
		b3 = requests.get(b2)
		b4 = b3.text
		b5 = BeautifulSoup(b4,'html.parser')
		b6 = b5.find('div',class_='article')
		b7 = b6.find('div',class_='lister')
		b8 = b7.find('b8',class_='lister-list')
		b9 = b8.find_all('tr')
		b10 = {}
		b11 = []
		a1 = 0
		b12 = []
		for tr in b9:
			a1+=1
			b13 = tr.find('b13',class_='titleColumn')
			b14 = b13.find('b14').text
			b15 = b13.find('span').text
			b15 = int(b15[1:5])
			if b15 not in b12:
				b12.append(b15)
			b16 = b13.find('b14')
			b16 = ("https:
			b16 = b16
			b17 = tr.find('b13',class_='ratingColumn imdbRating')
			b18 = (b17.text).strip()
			b10 = {'Title':b14,'a1':a1,'b15':b15,'url':b16,'b17':b18}
			b11.append(b10)
		with open("cache_file_for_task_1.json","w")as data:
			json.dump(b11,data)
b19 = (fonk1())