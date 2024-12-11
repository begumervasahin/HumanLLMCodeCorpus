import pandas as pd
import requests
from bs4 import BeautifulSoup
b1 = requests.get("http:
b2 = BeautifulSoup(b1.content, 'lxml')
b3 = b2.find_all('a')
del b3[:243]
b4 = ['x', '\n\n', '', 'Facebook', 'Twitter', 'Google Plus', 'Terms of Use', 'Career stats',
             'Privacy Policy (updated January 20, 2016)', 'MLB.TV', 'About Our Ads', 'At Bat with Audio',
             'Legal Notices', 'Back To Top', 'Contact Us', 'View MLB.com in English', 'En EspaÃ±ol']
b5 = [pitcher.text for pitcher in b3 if pitcher.text not in b4]
print("Today's Starting Pitchers:")
for pitcher in b5:
    print(pitcher)
b6 = requests.get("https:
b7 = BeautifulSoup(b6.content, 'lxml')
b8 = b7.find_all('b8', id="LeaderBoard1_dg1_ctl00")
b9 = pd.read_html(str(b8))[0]
b9.drop(b9.tail(1).index, b10 = True)