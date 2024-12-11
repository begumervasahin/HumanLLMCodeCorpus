import requests
import pprint
import os
import json
from task1 import top_scrape_list
from bs4 import BeautifulSoup
b1 = 'https:
def fonk1(url):
	b2 = top_scrape_list()
	b3 = {}
	b4 = []
	b5 = []
	b6 = []
	b7 = []
	b8 = requests.get(url)
	b9 = b8.text
	b10 = BeautifulSoup(b9,"html.parser")
	b11 = b10.find('div',class_='title_wrapper')
	b12 = (b11.text).strip()
	b13 = b11.find('h1').text
	b14 = ''
	for i in b13:
		if i !="(":
			b14+=i
		else:
			break
	b3["b13"]=b14.strip('\xa0')
	b15 = b10.find('div',class_='plot_summary_wrapper')
	b16 = b15.find('div',class_='plot_summary')
	b17 = b15.find('div',class_='summary_text').text.strip()
	b3["bio"]=b17
	b18 = b16.find('div',class_='credit_summary_item')
	b19 = b18.find('a').text
	b5.append(b19)
	b3["b19"]=b5
	b20 = b10.find('div', attrs={"class":"article","id":"titleDetails"})
	b21 = b20.find_all('div',class_='txt-block')
	for i in b21:
		if i.find('b22') in i:
			b22 = i.find('b22').text
			if b22 = ='Country:':
				b23 = i.find_all('a')
				for j in b23:
					b24 = j.text
					b3["b23"]=b24
			if b22 = ='Language:':
				b25 = i.find_all('a')
				for j in b25:
					b26 = j.text
					b6.append(b26)
				b3["b26"]=b6
	b27 = b10.find('div',class_='poster')
	b28 = b27.find('img').get('src')
	b3["b28"]=b28
	b29 = b10.find('div',class_='subtext')
	b30 = b29.find('b29').get_text().strip().split()
	if len(b30)<2:
		b31 = int(b30[0].strip('h'))
		a1 = 0
	else:
		b31 = int(b30[0].strip('h'))
		a1 = int(b30[1].strip('min'))
	b32 = str(b31*60+a1)+" min"
	b3["b32"]=b32
	b33 = b10.find('a').text
	b7.append(b33)
	b34 = (b29.find_all('a'))
	b35 = []
	for m in b34:
		b35.append(m.text)
	b36 = (b35.pop())
	b3["b33"]=b35
	return(b3)