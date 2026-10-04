import csv
import re
import requests
from bs4 import BeautifulSoup
class Scrappy:
    def __init__(self, cookie, host, user_agent):
        self.cookie = cookie
        self.host = host
        self.user_agent = user_agent
        self.urls = []
        self.page = 1
    def request_next_page(self):
        headers = {
            'User-Agent': self.user_agent,
            'Cookie': self.cookie
        }
        url = f"https:
        response = requests.get(url, headers=headers)
        self.page += 1
        return BeautifulSoup(response.content, 'html.parser')
    def append_urls(self, soup):
        listings = soup.find_all('a', href=re.compile('/listing/'))
        for listing in listings:
            self.urls.append(f"https:
    def scrape_report(self, url):
        headers = {
            'User-Agent': self.user_agent,
            'Cookie': self.cookie
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = []
        for row in ROWS:
            element = soup.find(id=row) or soup.find(class_=row)
            data.append(element.text.strip() if element else '')
        return data
ROWS = [
    'mls_num', 'num_pictures', 'list_price', 'price_perANDoriginal_list_price', 'status', 'cdom', 'list_date',
    'dom', 'address', 'area', 'city', 'county', 'restrictions', 'subdivision', 'taxes', 'zoning1', 'has_hoa',
    'hoa_transfer', 'hoa_amenities', 'pre_market', 'school_dist', 'elem', 'jr_high', 'sr_high', 'total_sqfoot.text',
    'total_bedrooms.text', 'total_bath_full.text', 'total_bath_three_fourth.text', 'total_bath_half.text', 'total_family.text',
    'total_den.text', 'total_formal_living_room.text', 'total_kitchen_k.text', 'total_kitchen_b.text', 'total_kitchen_f.text',
    'total_kitchen_s.text', 'total_laundry.text', 'total_fireplace.text', 'htype', 'style', 'year_built', 'const_status',
    'effect_yr_built', 'acres', 'deck_patio', 'frontage', 'garage', 'side', 'carport', 'back', 'prkg_sp', 'irregular',
    'fin_bsmt', 'roof', 'bsmt', 'heating', 'garage_park', 'air_cond', 'driveway', 'floor', 'water', 'window_cov', 'water_shares',
    'has_pool', 'has_spa', 'community_pool', 'pool_feat', 'master_level', 'possession', 'senior_comm', 'exterior', 'animals',
    'has_solar', 'landscape', 'lot_facts', 'inclusions', 'terms', 'storage', 'utilities', 'zoning2', 'remarks', 'exterior_feat',
    'interior_feat', 'amenities', 'access_feat', 'agt_remarks', 'show_inst', 'owner', 'owner_type', 'contact', 'contact_type', 'l_agent',
    'l_office', 'l_broker', 'bac', 'dual_var', 'list_type', 'comm_type', 'wthdrwn_dt', 'off_mkt_dt', 'exp_dt',
]
cookie = ''
host = 'www.utahrealestate.com'
user_agent = ''
myScraper = Scrappy(cookie, host, user_agent)
while myScraper.page <= 358:
    print(f"Finished scraping URLs from page: {myScraper.page - 1}")
    soup = myScraper.request_next_page()
    myScraper.append_urls(soup)
with open('urls.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for url in myScraper.urls:
        csv_writer.writerow([url])
print('Finished printing URLs to CSV')
urls = []
with open('urls.csv', newline='') as csvfile:
    urlreader = csv.reader(csvfile)
    for row in urlreader:
        urls.append(row[0])
with open('mls_scrape.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(ROWS)
    for i, url in enumerate(urls):
        data = myScraper.scrape_report(url)
        csv_writer.writerow(data)
        if i % 10 == 0:
            print(i)
print('Finished scraping data and saving to CSV')