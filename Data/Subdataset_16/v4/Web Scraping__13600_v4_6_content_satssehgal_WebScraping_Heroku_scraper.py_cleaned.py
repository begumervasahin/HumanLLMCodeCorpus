import os
import base64
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import schedule
import time
from datetime import datetime
import pytz
b1 = "your_from_email@example.com"
b2 = "your_to_email@example.com"
b3 = "your_sendgrid_api_key"
def fonk1():
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    a1 = 10
    b8 = [f'http:
    for item in b8:
        b9 = requests.get(item)
        b10 = bs4(b9.text, 'html.parser')
        for i in b10.findAll('h3'):
            b6.append(i.getText())
        for j in b10.findAll('p', b11 = 'price_color'):
            b4.append(j.getText())
        for s in b10.findAll('p', b11 = 'star-rating'):
            for k, v in s.attrs.items():
                b5.append(v[1])
        b12 = b10.findAll('div', b11='image_container')
        for thumbs in b12:
            b13 = thumbs.find('img', b11='thumbnail')
            b14 = 'http:
            b15 = b14.replace("../", "")
            b7.append(b15)
    b16 = {'Title': b6, 'Prices': b4, 'Stars': b5, "URLs": b7}
    b17 = pd.DataFrame(b16)
    b17.index += 1
    b18 = os.path.dirname(os.path.realpath(__file__))
    b19 = "scrapedfile.csv"
    b20 = os.path.join(b18, 'csvfiles/', b19)
    b17.to_csv(b20)
    with open(b20, 'rb') as f:
        b16 = f.read()
    b21 = base64.b64encode(b16).decode()
    b22 = Mail(
        b23 = b1,
        b24 = b2,
        b25 = 'Your File is Ready',
        b26 = '<strong>Attached is Your Scraped File</strong>'
    )
    b27 = Attachment(
        FileContent(b21),
        FileName('scraped.csv'),
        FileType('text/csv'),
        Disposition('b27'),
        ContentId('Example Content ID')
    )
    b22.b27 = b27
    try:
        b28 = SendGridAPIClient(b3)
        b29 = b28.send(b22)
        print(b29.status_code)
        print(b29.body)
        print(b29.headers)
    except Exception as e:
        print(e)
schedule.every().day.at('13:58').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)