import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
res = requests.get("http:
soup = BeautifulSoup(res.content,'lxml')
pitchers = soup.find_all('a')
del pitchers[:243]
stopwords = ['x','\n\n','','Facebook','Twitter','Google Plus','Terms of Use', 'Career stats', 'Privacy Policy (updated January 20, 2016)', 'MLB.TV', 'About Our Ads', 'At Bat with Audio', 'Legal Notices', 'Back To Top','Contact Us','View MLB.com in English','En EspaÃ±ol']
for pitcher in list(pitchers):
    if pitcher.text in stopwords:
        pitchers.remove(pitcher)
print("Todays Starting Pitchers:")
for pitcher in pitchers:
    print (pitcher.text)
res = requests.get("https:
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table', id="LeaderBoard1_dg1_ctl00")
df = pd.read_html(str(table))
df = df[0]
df.columns = ['
df.drop(df.tail(1).index,inplace=True)