from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import re
import math
import pandas as pd
b1 = pd.read_csv("geo.csv", b17 = "ISO-8859-1")
b2 = b1.city
b3 = b1.lat
b4 = b1.lng
b5 = webdriver.FirefoxProfile()
b5.set_preference('permissions.default.stylesheet', 2)
b5.set_preference('permissions.default.image', 2)
b5.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
b6 = webdriver.Firefox(firefox_profile = b5)
b7 = {'Juice Bar':21,'Macrobiotic':12,
	 'Organic':13, 'Raw food':14, 'Salad Bar':20, 'Take Out':24, 'American':5, 'Asian':28, 'Australian':47, 'Brazilian':46, 'British':30, 'Caribbean':31,
	 'Chinese':7, 'European':34, 'French':35, 'Fusion':36, 'German':37,'Indian':8, 'International':9, 'Italian':10,'Japanese':11, 'Latin':45,
	 'Mediterranean':18, 'Mexican':25, 'Middle Eastern':39, 'Spanish':40, 'Taiwanese':41, 'Thai':15, 'Vietnamese':42, 'Western':16}
b8 = ['Juice Bar','Macrobiotic',
	 'Organic', 'Raw food', 'Salad Bar', 'Take Out', 'American', 'Asian', 'Australian', 'Brazilian', 'British', 'Caribbean',
	 'Chinese', 'European', 'French', 'Fusion', 'German','Indian', 'International', 'Italian','Japanese', 'Latin',
	 'Mediterranean', 'Mexican', 'Middle Eastern', 'Spanish', 'Taiwanese', 'Thai', 'Vietnamese', 'Western']
for j in range(len(b8)):
	b9 = list();
	for i in range(len(b2)):
		b10 = "https:
		b6.get(b10)
		b11 = b6.page_source
		b12 = soup(b11,'html.parser')
		b13 = int(b12.find("span", {"class":"total-results"}).text.strip())
		b14 = math.ceil(b13/81)
		for count in range(1, (b14+1)):
			if (count != 1):
				b10 = "https:
				b6.get(b10)
				b11 = b6.page_source
				b12 = soup(b11,'html.parser')
			for details in b12.findAll(b15 = {"class":"js-venues venues__item"}):
				b9.append(details["b9-id"]+"\n")
	b16 = "category_"+b8[j]+".csv"
	with open(b16,"w", b17 = "utf-8") as f:
		f.writelines(b9)
b6.quit()