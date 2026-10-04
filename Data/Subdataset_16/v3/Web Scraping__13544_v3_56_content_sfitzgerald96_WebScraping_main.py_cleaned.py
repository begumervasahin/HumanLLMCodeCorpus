import csv
import re
import requests
from bs4 import BeautifulSoup
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = []
        self.a1 = 1
    def fonk2(self):
        b5 = {
            'User-Agent': self.b3,
            'Cookie': self.b1
        }
        b6 = f"https:
        b7 = requests.get(b6, b5=b5)
        self.a1 += 1
        return BeautifulSoup(b7.content, 'html.parser')
    def fonk3(self, b9):
        b8 = b9.find_all('a', href=re.compile('/listing/'))
        for listing in b8:
            self.b4.append(f"https:
    def fonk4(self, b6):
        b5 = {
            'User-Agent': self.b3,
            'Cookie': self.b1
        }
        b7 = requests.get(b6, b5=b5)
        b9 = BeautifulSoup(b7.content, 'html.parser')
        b10 = []
        for field in b12:
            b11 = b9.find(id=field) or b9.find(class_=field)
            b10.append(b11.text.strip() if b11 else '')
        return b10
b12 = [
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
    'l_office', 'l_broker', 'bac', 'dual_var', 'list_type', 'comm_type', 'wthdrwn_dt', 'off_mkt_dt', 'exp