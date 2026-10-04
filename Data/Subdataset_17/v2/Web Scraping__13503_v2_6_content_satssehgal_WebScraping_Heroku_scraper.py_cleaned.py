import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
import base64
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId
import schedule
import time
SENDGRID_API_KEY = 'YOUR_SENDGRID_API_KEY'
FROM_EMAIL = 'your_email@example.com'
TO_EMAIL = 'recipient_email@example.com'
def scrape_books():
    prices, stars, titles, urlss = [], [], [], []
    pages_to_scrape = 10
    base_url = 'http:
    for page_num in range(1, pages_to_scrape + 1):
        url = base_url.format(page_num)
        page = requests.get(url)
        soup = bs4(page.text, 'html.parser')
        for h3 in soup.findAll('h3'):
            titles.append(h3.getText())
        for price in soup.findAll('p', class_='price_color'):
            prices.append(price.getText())
        for star in soup.findAll('p', class_='star-rating'):
            stars.append(star.get('class')[1])
        for div in soup.findAll('div', class_='image_container'):
            img_tag = div.find('img', class_='thumbnail')
            img_url = 'http:
            urlss.append(img_url)
    return pd.DataFrame({'Title': titles, 'Prices': prices, 'Stars': stars, 'URLs': urlss})
def save_to_csv(df, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
def send_email_with_attachment(file_path):
    with open(file_path, 'rb') as f:
        encoded_file = base64.b64encode(f.read()).decode()
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject='Your File is Ready',
        html_content='<strong>Attached is Your Scraped File</strong>'
    )
    attachment = Attachment(
        file_content=FileContent(encoded_file),
        file_type=FileType('text/csv'),
        file_name=FileName('scrapedfile.csv'),
        disposition=Disposition('attachment'),
        content_id=ContentId('Example Content ID')
    )
    message.attachment = attachment
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")
def job():
    df = scrape_books()
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'csvfiles', 'scrapedfile.csv')
    save_to_csv(df, file_path)
    send_email_with_attachment(file_path)
schedule.every().day.at('13:58').do(job)
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)