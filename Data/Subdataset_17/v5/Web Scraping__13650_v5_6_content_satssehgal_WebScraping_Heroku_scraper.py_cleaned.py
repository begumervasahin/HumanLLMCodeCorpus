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
def scrape_books_data(pages_to_scrape=10):
    titles, prices, stars, urls = [], [], [], []
    pages = [f'http:
    for page_url in pages:
        response = requests.get(page_url)
        soup = bs4(response.text, 'html.parser')
        titles.extend([h3.get_text() for h3 in soup.find_all('h3')])
        prices.extend([price.get_text() for price in soup.find_all('p', class_='price_color')])
        stars.extend([star['class'][1] for star in soup.find_all('p', class_='star-rating')])
        base_url = 'http:
        image_urls = [
            base_url + img['src'].replace('../', '')
            for img in soup.select('div.image_container img.thumbnail')
        ]
        urls.extend(image_urls)
    data = {'Title': titles, 'Prices': prices, 'Stars': stars, 'URLs': urls}
    df = pd.DataFrame(data)
    df.index += 1
    return df
def save_to_csv(df, directory='csvfiles', filename='scrapedfile.csv'):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    df.to_csv(file_path)
    return file_path
def send_email_with_attachment(file_path):
    with open(file_path, 'rb') as file:
        encoded_file = base64.b64encode(file.read()).decode()
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject='Your File is Ready',
        html_content='<strong>Attached is Your Scraped File</strong>'
    )
    attachment = Attachment(
        file_content=FileContent(encoded_file),
        file_name=FileName('scraped.csv'),
        file_type=FileType('text/csv'),
        disposition=Disposition('attachment')
    )
    message.attachment = attachment
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f'Status Code: {response.status_code}')
        print(f'Response Body: {response.body}')
        print(f'Response Headers: {response.headers}')
    except Exception as e:
        print(f'Error: {e}')
def job():
    df = scrape_books_data()
    file_path = save_to_csv(df)
    send_email_with_attachment(file_path)
schedule.every().day.at('13:58').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)