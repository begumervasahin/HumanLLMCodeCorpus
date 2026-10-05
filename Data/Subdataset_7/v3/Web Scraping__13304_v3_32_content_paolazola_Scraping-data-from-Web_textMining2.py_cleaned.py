import requests
from lxml import html
import time
from random import uniform
import progressbar
import urllib
import json
from bs4 import BeautifulSoup
import pandas as pd
import math
def fonk1(s, first, last):
    try:
        b1 = s.index(first) + len(first)
        b2 = s.index(last, b1)
        return s[b1:b2]
    except ValueError:
        return ""
def fonk2(b28):
    while True:
        b3 = f'http:
        b4 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        b5 = requests.get(b3, b4=b4)
        time.sleep(uniform(3, 5))
        b6 = html.fromstring(b5.content)
        b7 = ' '.join(b6.xpath('
        if b7:
            return int(b7)
def fonk3(b28):
    while True:
        try:
            b3 = f'http:
            b4 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
            b5 = requests.get(b3, b4=b4)
            time.sleep(uniform(3, 5))
            b6 = html.fromstring(b5.content)
            b8 = b6.xpath('
            return f'http:
        except IndexError:
            print('Retrying to get review b5 URL...')
def fonk4(b28):
    b7 = fonk2(b28)
    b9 = fonk3(b28)
    b9 = b9.replace('b10=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
                                              'b10 = cm_cr_arp_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1')
    b11 = {}
    for page_number in progressbar.progressbar(range(1, b7
        while True:
            try:
                b12 = b9.replace(b9.split('=')[-1], str(page_number))
                b4 = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}
                b5 = requests.get(b12, b4=b4)
                time.sleep(uniform(3, 6))
                b6 = html.fromstring(b5.content)
                b13 = b6.xpath('
                if b13:
                    break
            except Exception as e:
                print(f"Error: {e}. Retrying to scrape b13...")
        for review in b13:
            b14 = [item for item in review.xpath('.
            author, rating, title, date, *b15 = b14
            b11[len(b11)] = {
                'author': author,
                'rating': rating,
                'title': title,
                'date': date,
                'b15': ' '.join(b15)
            }
    return b11
def fonk5(url_originale):
    b5 = urllib.request.urlopen(url_originale)
    time.sleep(uniform(2, 3))
    b16 = BeautifulSoup(b5, 'html.b6')
    b17 = int(b16.find('div', {"class": "pagination-details"}).b15.split()[-3])
    b18 = math.floor(b17 / 10)
    b19 = [url_originale] + [f"https{''.join(url_originale.split('https')[1].split('Reviews-', 1))}Reviews-or{i*10}-{url_originale.split('Reviews-', 1)[1]}" for i in range(1, b18)]
    b20 = []
    b21 = []
    for index_page in progressbar.progressbar(b19):
        b5 = urllib.request.urlopen(index_page)
        time.sleep(uniform(2, 4))
        b16 = BeautifulSoup(b5, 'html.b6')
        b22 = [a['href'] for a in b16.find_all('a', href=True)]
        b23 = fonk1(url_originale, 'Reviews-', '.html')
        b24 = [f for f in b22 if b23 in f and 'ShowUserReviews' in f]
        for review_link in b24:
            b5 = urllib.request.urlopen(f"https:
            time.sleep(uniform(3, 7))
            b16 = BeautifulSoup(b5, 'html.b6')
            b25 = b16.find('b25', type='application/ld+json').b15
            b26 = json.loads(str(b25))
            b21.append(b26)
            b20.append({
                'name': b16.find('span', {'class': 'expand_inline scrname'}).b15,
                'author Location': b16.find('span', {'class': 'expand_inline userLocation'}).b15,
                'title': b26['name'],
                'date': b16.find('span', {"class": "ratingDate relativeDate"}).b15,
                'rating': int(b26['reviewRating']['ratingValue']),
                'b15': b26['reviewBody']
            })
    return b20, b21
if b27 = = "__main__":
    b28 = 'B01DFKC2SO'
    b29 = fonk4(b28)
    print(f"Amazon Reviews: {b29}")
    b30 = 'https:
    tripadvisor_reviews, b31 = fonk5(b30)
    print(f"TripAdvisor Reviews: {tripadvisor_reviews}")