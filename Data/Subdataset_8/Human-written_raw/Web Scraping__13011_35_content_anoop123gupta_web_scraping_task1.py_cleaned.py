import requests
import pprint
import json
import os
from bs4 import BeautifulSoup
def top_scrape_list():
	if os.path.isfile("cache_file_for_task_1.json"):
		with open("cache_file_for_task_1.json","r+")as data:
			file=json.load(data)
			return(file)
	else:
		endpoint='https:
		req=requests.get(endpoint)
		result=req.text
		soup=BeautifulSoup(result,'html.parser')
		main=soup.find('div',class_='article')
		sub_main=main.find('div',class_='lister')
		tbody=sub_main.find('tbody',class_='lister-list')
		trs=tbody.find_all('tr')
		dic={}
		lit=[]
		rank=0
		list_year=[]
		for tr in trs:
			rank+=1
			td=tr.find('td',class_='titleColumn')
			a=td.find('a').text
			year=td.find('span').text
			year=int(year[1:5])
			if year not in list_year:
				list_year.append(year)
			link=td.find('a')
			link=("https:
			link=link
			rating=tr.find('td',class_='ratingColumn imdbRating')
			rate=(rating.text).strip()
			dic={'Title':a,'rank':rank,'year':year,'url':link,'rating':rate}
			lit.append(dic)
		with open("cache_file_for_task_1.json","w")as data:
			json.dump(lit,data)
movies=(top_scrape_list())