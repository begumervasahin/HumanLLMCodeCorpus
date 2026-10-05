import pandas as pd
import requests
from bs4 import BeautifulSoup
mlb_res = requests.get("http:
mlb_soup = BeautifulSoup(mlb_res.content, 'lxml')
pitchers = mlb_soup.find_all('a')
del pitchers[:243]
stopwords = ['x', '\n\n', '', 'Facebook', 'Twitter', 'Google Plus', 'Terms of Use', 'Career stats',
             'Privacy Policy (updated January 20, 2016)', 'MLB.TV', 'About Our Ads', 'At Bat with Audio',
             'Legal Notices', 'Back To Top', 'Contact Us', 'View MLB.com in English', 'En EspaÃ±ol']
filtered_pitchers = [pitcher.text for pitcher in pitchers if pitcher.text not in stopwords]
print("Today's Starting Pitchers:")
for pitcher in filtered_pitchers:
    print(pitcher)
fangraphs_res = requests.get("https:
fangraphs_soup = BeautifulSoup(fangraphs_res.content, 'lxml')
table = fangraphs_soup.find_all('table', id="LeaderBoard1_dg1_ctl00")
df = pd.read_html(str(table))[0]
df.drop(df.tail(1).index, inplace=True)