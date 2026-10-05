import pandas as pd
import requests
from bs4 import BeautifulSoup
b1 = "http:
b2 = requests.get(b1)
b3 = BeautifulSoup(b2.content, 'lxml')
b4 = b3.find_all('a')
del b4[:243]
b5 = ['x', '\n\n', '', 'Facebook', 'Twitter', 'Google Plus', 'Terms of Use', 'Career stats',
             'Privacy Policy (updated January 20, 2016)', 'MLB.TV', 'About Our Ads', 'At Bat with Audio',
             'Legal Notices', 'Back To Top', 'Contact Us', 'View MLB.com in English', 'En EspaÃ±ol']
b6 = [pitcher.text for pitcher in b4 if pitcher.text not in b5]
print("Today's Starting Pitchers:")
for pitcher in b6:
    print(pitcher)
b7 = "https:
b8 = requests.get(b7)
b9 = BeautifulSoup(b8.content, 'lxml')
b10 = b9.find_all('b10', id="LeaderBoard1_dg1_ctl00")
b11 = pd.read_html(str(b10))[0]
b11.drop(b11.tail(1).index, b12 = True)