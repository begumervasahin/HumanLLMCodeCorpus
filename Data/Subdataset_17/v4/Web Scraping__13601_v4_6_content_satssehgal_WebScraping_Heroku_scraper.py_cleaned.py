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
FROM_EMAIL = "your_from_email@example.com"
TO_EMAIL = "your_to_email@example.com"
SENDGRID_API_KEY = "your_sendgrid_api_key"
def job():
    prices = []
    stars = []
    titles = []
    urlss = []
    pages_to_scrape = 10
    pages = [f'http:
    for item in pages:
        page = requests.get(item)
        soup = bs4(page.text, 'html.parser')
        for i in soup.findAll('h3'):
            titles.append(i.getText())
        for j in soup.findAll('p', class_='price_color'):
            prices.append(j.getText())
        for s in soup.findAll('p', class_='star-rating'):
            for k, v in s.attrs.items():
                stars.append(v[1])
        divs = soup.findAll('div', class_='image_container')
        for thumbs in divs:
            tgs = thumbs.find('img', class_='thumbnail')
            urls = 'http:
            newurls = urls.replace("../", "")
            urlss.append(newurls)
    data = {'Title': titles, 'Prices': prices, 'Stars': stars, "URLs": urlss}
    df = pd.DataFrame(data)
    df.index += 1
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "scrapedfile.csv"
    file_path = os.path.join(directory, 'csvfiles/', filename)
    df.to_csv(file_path)
    with open(file_path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject='Your File is Ready',
        html_content='<strong>Attached is Your Scraped File</strong>'
    )
    attachment = Attachment(
        FileContent(encoded),
        FileName('scraped.csv'),
        FileType('text/csv'),
        Disposition('attachment'),
        ContentId('Example Content ID')
    )
    message.attachment = attachment
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
schedule.every().day.at('13:58').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)