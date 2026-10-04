from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import base64
import os.path
from apikey import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import schedule
import time
from datetime import datetime
import pytz
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    a1 = 10
    b5 = [('http:
    for item in b5:
        b6 = requests.get(item)
        b7 = bs4(b6.text, 'html.parser')
        for i in b7.findAll('h3'):
            b3.append(i.getText())
        for j in b7.findAll('p', b8 = 'price_color'):
            b1.append(j.getText())
        for s in b7.findAll('p', b8 = 'star-rating'):
            for k,v in s.attrs.items():
                b2.append(v[1])
        b9 = b7.findAll('div', b8='image_container')
        for thumbs in b9:
            b10 = thumbs.find('img',b8='thumbnail')
            b11 = 'http:
            b12 = b11.replace("../","")
            b4.append(b12)
    b13 = {'Title': b3, 'Prices': b1, 'Stars':b2, "URLs":b4}
    b14 = pd.DataFrame(b13=b13)
    b14.index+=1
    b15 = os.path.dirname(os.path.realpath(__file__))
    b16 = "scrapedfile.csv"
    b17 = os.path.join(b15,'csvfiles/', b16)
    b14.to_csv(b17)
    with open(b17, 'rb') as f:
        b13 = f.read()
        f.close()
    b18 = base64.b64encode(b13).decode()
    b19 = Mail(
    b20 = FROM_EMAIL,
    b21 = TO_EMAIL,
    b22 = 'Your File is Ready',
    b23 = '<strong>Attached is Your Scraped File</strong>')
    b24 = Attachment()
    b24.b25 = FileContent(b18)
    b24.b26 = FileType('text/csv')
    b24.b27 = FileName('scraped.csv')
    b24.b28 = Disposition('b24')
    b24.b29 = ContentId('Example Content ID')
    b19.b24 = b24
    try:
        b30 = SendGridAPIClient(SENDGRID_API_KEY)
        b31 = b30.send(b19)
        print(b31.status_code)
        print(b31.body)
        print(b31.headers)
    except Exception as e:
         print(e)
schedule.every().day.at('13:58').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)