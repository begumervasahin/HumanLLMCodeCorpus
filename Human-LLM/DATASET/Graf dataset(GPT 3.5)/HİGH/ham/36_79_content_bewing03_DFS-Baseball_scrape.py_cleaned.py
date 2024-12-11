import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
b1 = requests.get("http:
b2 = BeautifulSoup(b1.content,'lxml')
b3 = b2.find_all('a')
del b3[:243]
b4 = ['x','\n\n','','Facebook','Twitter','Google Plus','Terms of Use', 'Career stats', 'Privacy Policy (updated January 20, 2016)', 'MLB.TV', 'About Our Ads', 'At Bat with Audio', 'Legal Notices', 'Back To Top','Contact Us','View MLB.com in English','En EspaÃ±ol']
for pitcher in list(b3):
    if pitcher.text in b4:
        b3.remove(pitcher)
print("Todays Starting Pitchers:")
for pitcher in b3:
    print (pitcher.text)
b1 = requests.get("https:
b2 = BeautifulSoup(b1.content,'lxml')
b5 = b2.find_all('b5', id="LeaderBoard1_dg1_ctl00")
b6 = pd.read_html(str(b5))
b6 = b6[0]
b6.b7 = ['
b6.drop(b6.tail(1).index,b8 = True)