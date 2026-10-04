import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search
logging.getLogger('scrapy').propagate = False
def get_urls(tag, n, language):
    return [url for url in search(tag, stop=n, lang=language)][:n]
def ask_user(question):
    response = input(f"{question} (y/n)\n").strip().lower()
    return response == 'y'
def create_file(path):
    if os.path.exists(path):
        if not ask_user('File already exists, replace?'):
            return False
    with open(path, 'w'):
        pass
    return True
class MailSpider(scrapy.Spider):
    name = 'email'
    def __init__(self, path, reject, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.reject = reject
    def parse(self, response):
        links = LxmlLinkExtractor(allow=()).extract_links(response)
        links = [str(link.url) for link in links]
        links.append(str(response.url))
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link)
    def parse_link(self, response):
        for word in self.reject:
            if word in response.url:
                return
        html_text = response.text
        mail_list = re.findall(r'\w+@\w+\.\w+', html_text)
        if mail_list:
            data = {'email': mail_list, 'link': [response.url] * len(mail_list)}
            df = pd.DataFrame(data)
            df.to_csv(self.path, mode='a', header=False, index=False)
def get_info(tag, n, language, path, reject=[]):
    if not create_file(path):
        return
    df = pd.DataFrame(columns=['email', 'link'])
    df.to_csv(path, mode='w', header=True, index=False)
    print('Collecting Google URLs...')
    google_urls = get_urls(tag, n, language)
    print('Searching for emails...')
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
    process.crawl(MailSpider, start_urls=google_urls, path=path, reject=reject)
    process.start()
    print('Cleaning emails...')
    df = pd.read_csv(path)
    df = df.drop_duplicates(subset='email').reset_index(drop=True)
    df.to_csv(path, mode='w', header=True, index=False)
    return df
if __name__ == "__main__":
    bad_words = ['facebook', 'instagram', 'youtube', 'twitter', 'wiki']
    df = get_info('mastering studio london', 300, 'en', 'studios.csv', reject=bad_words)
    print(df.head())