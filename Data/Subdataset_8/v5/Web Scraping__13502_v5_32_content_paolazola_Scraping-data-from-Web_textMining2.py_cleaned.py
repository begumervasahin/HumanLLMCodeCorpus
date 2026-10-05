import requests
import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import json
import pandas as pd
import time
from random import uniform
import math
import progressbar
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
def get_reviews_number(asin):
    while True:
        amazon_url = 'http:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
        }
        page = requests.get(amazon_url, headers=headers)
        time.sleep(uniform(3, 5))
        page_response = page.content
        time.sleep(uniform(3, 4))
        parser = html.fromstring(page_response)
        reviews_number = ' '.join(parser.xpath('
        reviews_number = reviews_number.replace(',', '')
        if reviews_number:
            return int(reviews_number)
def get_amazon_reviews(asin, reviews_number):
    reviews_per_page = 9
    base_url = 'http:
    review_url_pattern = base_url.replace('ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
                                          'ref=cm_cr_arp_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber={}')
    reviews = []
    for page_number in progressbar.progressbar(range(1, reviews_number
        url = review_url_pattern.format(page_number)
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}
        while True:
            page = requests.get(url, headers=headers)
            time.sleep(uniform(3, 6))
            page_response = page.content
            parser = html.fromstring(page_response)
            reviews_divs = parser.xpath('
            if reviews_divs:
                break
        for review_div in reviews_divs:
            review_data = {}
            data = [item.strip() for item in review_div.xpath('.
            review_data['author'] = data[0]
            review_data['rating'] = data[1]
            review_data['title'] = data[2]
            review_data['date'] = data[3]
            review_data['text'] = ' '.join(data[6:])
            reviews.append(review_data)
    return reviews
def get_tripadvisor_reviews(url):
    page = urllib.request.urlopen(url)
    time.sleep(uniform(2, 3))
    soup = BeautifulSoup(page, 'html.parser')
    pagination_details = soup.find('div', class_='pagination-details')
    total_reviews = int(pagination_details.text.split()[-3])
    review_urls = [url]
    for i in range(10, total_reviews, 10):
        review_urls.append(url.replace('Reviews-', f'Reviews-or{i}-'))
    reviews = []
    for review_url in progressbar.progressbar(review_urls):
        page = urllib.request.urlopen(review_url)
        time.sleep(uniform(2, 4))
        soup = BeautifulSoup(page, 'html.parser')
        review_scripts = soup.find_all('script', type='application/ld+json')
        for script in review_scripts:
            review_data = json.loads(script.text)
            review = {
                'name': review_data['name'],
                'author_location': review_data['author']['address']['addressLocality'],
                'title': review_data['name'],
                'date': review_data['datePublished'],
                'rating': review_data['reviewRating']['ratingValue'],
                'text': review_data['reviewBody']
            }
            reviews.append(review)
    return reviews
def amazon_tripadvisor_scraper(asin, tripadvisor_url):
    reviews_number = get_reviews_number(asin)
    amazon_reviews = get_amazon_reviews(asin, reviews_number)
    tripadvisor_reviews = get_tripadvisor_reviews(tripadvisor_url)
    return amazon_reviews, tripadvisor_reviews