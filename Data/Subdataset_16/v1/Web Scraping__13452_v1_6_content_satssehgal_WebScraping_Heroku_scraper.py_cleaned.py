import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
import base64
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import schedule
import time
from datetime import datetime
import pytz
b1 = 'YOUR_SENDGRID_API_KEY'
b2 = 'your_email@example.com'
b3 = 'recipient_email@example.com'
def fonk1():
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    a1 = 10
    b8 = [('http:
    for item in b8:
        b9 = requests.get(item)
        b10 = bs4(b9.text, 'html.parser')
        for i in b10.findAll('h3'):
            b6.append(i.getText())
        for j in b10.findAll('p', b11 = 'price_color'):
            b4.append(j.getText())
        for s in b10.findAll('p', b11 = 'star-rating'):
            b5.append(s.get('class')[1])
        b12 = b10.findAll('div', b11='image_container')
        for thumbs in b12:
            b13 = thumbs.find('img', b11='thumbnail')
            b14 = 'http:
            b15 = b14.replace("../", "")
            b7.append(b15)
    b16 = {'Title': b6, 'Prices': b4, 'Stars': b5, "URLs": b7}
    b17 = pd.DataFrame(b16=b16)
    b17.b22 += 1
    b18 = os.path.dirname(os.path.realpath(__file__))
    b19 = os.path.join(b18, 'csvfiles')
    os.makedirs(b19, b20 = True)
    b21 = os.path.join(b19, 'scrapedfile.csv')
    b17.to_csv(b21, b22 = False)
    with open(b21, 'rb') as f:
        b16 = f.read()
        b23 = base64.b64encode(b16).decode()
    b24 = Mail(
        b25 = b2,
        b26 = b3,
        b27 = 'Your File is Ready',
        b28 = '<strong>Attached is Your Scraped File</strong>'
    )
    b29 = Attachment()
    b29.b30 = FileContent(b23)
    b29.b31 = FileType('text/csv')
    b29.b32 = FileName('scrapedfile.csv')
    b29.b33 = Disposition('b29')
    b29.b34 = ContentId('Example Content ID')
    b24.b29 = b29
    try:
        b35 = SendGridAPIClient(b1)
        b36 = b35.send(b24)
        print(b36.status_code)
        print(b36.body)
        print(b36.headers)
    except Exception as e:
        print(e)
schedule.every().day.at('13:58').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)