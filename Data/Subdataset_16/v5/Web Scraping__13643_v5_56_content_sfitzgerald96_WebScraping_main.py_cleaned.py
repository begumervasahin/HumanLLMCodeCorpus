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
    'total_den.text', 'total_formal_living_room.text', 'total_kitchen_k.text', 'total_kitchen_b.text', 'total_kitchen_f.text',
    'total_kitchen_s.text', 'total_laundry.text', 'total_fireplace.text', 'htype', 'style', 'year_built', 'const_status',
    'effect_yr_built', 'acres', 'deck_patio', 'frontage', 'garage', 'side', 'carport', 'back', 'prkg_sp', 'irregular',
    'fin_bsmt', 'roof', 'bsmt', 'heating', 'garage_park', 'air_cond', 'driveway', 'floor', 'water', 'window_cov', 'water_shares',
    'has_pool', 'has_spa', 'community_pool', 'pool_feat', 'master_level', 'possession', 'senior_comm', 'exterior', 'animals',
    'has_solar', 'landscape', 'lot_facts', 'inclusions', 'terms', 'storage', 'utilities', 'zoning2', 'remarks', 'exterior_feat',
    'interior_feat', 'amenities', 'access_feat', 'agt_remarks', 'show_inst', 'owner', 'owner_type', 'contact', 'contact_type', 'l_agent',
    'l_office', 'l_broker', 'bac', 'dual_var', 'list_type', 'comm_type', 'wthdrwn_dt', 'off_mkt_dt', 'exp_dt',
]
def fonk1():
    b2 = ''
    b3 = 'www.utahrealestate.com'
    b4 = ''
    return classes.scrappy(b2, b3, b4)
def fonk2(b14, b5 = 358):
    while b14.page <= b5:
        print(f"Finished scraping URLs from page: {b14.page}")
        b6 = b14.request_next_page()
        b14.append_urls(b6)
def fonk3(b10, b7 = 'b10.csv'):
    with open(b7, 'w', b8 = '') as csv_file:
        b9 = csv.writer(csv_file)
        for url in b10:
            b9.writerow([url])
    print('Finished printing URLs to CSV')
def fonk4(b7 = 'b10.csv'):
    b10 = []
    with open(b7, b8 = '') as csvfile:
        b11 = csv.reader(csvfile)
        for row in b11:
            b10.append(row[0])
    return b10
def fonk5(b10, b14, b7 = 'mls_scrape.csv'):
    with open(b7, 'w', b8 = '') as csv_file:
        b9 = csv.writer(csv_file)
        b9.writerow(b1)
        for i, url in enumerate(b10):
            b12 = b14.scrape_report(url)
            b9.writerow(b12)
            if i % b13 = = 0:
                print(i)
    print('Finished scraping MLS b12 to CSV')
def fonk6():
    b14 = fonk1()
    fonk2(b14)
    b10 = b14.b10
    fonk3(b10)
    b10 = fonk4()
    fonk5(b10, b14)
if b15 = = "__main__":
    fonk6()