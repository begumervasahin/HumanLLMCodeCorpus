from bs4 import BeautifulSoup
import requests
import csv
import classes
import re
b1 = [
    'mls_num', 'num_pictures', 'list_price', 'price_perANDoriginal_list_price', 'status', 'cdom', 'list_date',
    'dom', 'address', 'area', 'city', 'county', 'restrictions', 'subdivision', 'taxes', 'zoning1', 'has_hoa',
    'hoa_transfer', 'hoa_amenities', 'pre_market', 'school_dist', 'elem', 'jr_high', 'sr_high', 'total_sqfoot.text',
    'total_bedrooms.text', 'total_bath_full.text', 'total_bath_three_fourth.text', 'total_bath_half.text', 'total_family.text',
    'total_den.text', 'total_formal_living_room.text','total_kitchen_k.text', 'total_kitchen_b.text', 'total_kitchen_f.text',
    'total_kitchen_s.text', 'total_laundry.text', 'total_fireplace.text', 'htype', 'style', 'year_built', 'const_status',
    'effect_yr_built', 'acres', 'deck_patio', 'frontage', 'garage', 'side', 'carport', 'back', 'prkg_sp', 'irregular',
    'fin_bsmt', 'roof', 'bsmt', 'heating', 'garage_park', 'air_cond', 'driveway', 'floor', 'water', 'window_cov', 'water_shares',
    'has_pool', 'has_spa', 'community_pool', 'pool_feat', 'master_level', 'possession', 'senior_comm', 'exterior', 'animals',
    'has_solar', 'landscape', 'lot_facts', 'inclusions', 'terms', 'storage', 'utilities', 'zoning2', 'remarks', 'exterior_feat',
    'interior_feat', 'amenities', 'access_feat', 'agt_remarks', 'show_inst', 'owner', 'owner_type', 'contact', 'contact_type', 'l_agent',
    'l_office', 'l_broker', 'bac', 'dual_var', 'list_type', 'comm_type', 'wthdrwn_dt', 'off_mkt_dt', 'exp_dt',
]
b2 = ''
b3 = 'www.utahrealestate.com'
b4 = ''
b5 = classes.scrappy(b2,b3,b4)
while b5.page <= 358:
    print("finished scraping b9 from page: " + b5.page)
    b6 = b5.request_next_page()
    b5.append_urls(b6)
b7 = open('b9.csv', 'w')
b8 = csv.writer(b7)
b9 = b5.b9
for url in b9:
    b8.writerow(url)
print(f'finished printing b9 to CSV')
b9 = []
with open('b9.csv', b10 = '') as csvfile:
    b11 = csv.reader(csvfile, delimiter=' ')
    for row in b11:
        b9.append(', '.join(row))
b7.close()
b7 = open('mls_scrape.csv', 'w')
b8 = b8(b7)
b8.writerow(b1)
a1 = 0
for url in b9:
    b12 = b5.scrape_report(url)
    b8.writerow(b12)
    if a1%b13 = = 0:
        print(a1)
    a1 += 1
b7.close()