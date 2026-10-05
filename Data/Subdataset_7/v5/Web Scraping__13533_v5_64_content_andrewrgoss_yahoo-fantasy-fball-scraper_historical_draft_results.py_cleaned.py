
import argparse
import re
import time
from io import StringIO
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def fonk1():
    b1 = time.time()
    b2 = fonk2()
    return b1, b2
def fonk2():
    b3 = argparse.ArgumentParser(description='Parse command line arguments')
    b3.add_argument('--yahoo_email', b4 = str, required=True, help='Yahoo email address for account login.')
    b3.add_argument('--yahoo_pw', b4 = str, required=True, help='Password for Yahoo account login.')
    b3.add_argument('--yahoo_league_name', b4 = str, required=True, help='Name of Yahoo fantasy football league.')
    b3.add_argument('--yahoo_league_year', b4 = str, required=True, help='Historical league year for draft results.')
    return b3.parse_args()
def fonk3(user_email, user_pw, b9):
    b9.get('https:
    b5 = b9.find_element_by_id('login-username')
    b5.send_keys(user_email)
    b6 = b9.find_element_by_id("login-signin")
    b6.click()
    b7 = WebDriverWait(b9, 10).until(EC.presence_of_element_located((By.ID, "login-passwd")))
    b7.send_keys(user_pw)
    b8 = b9.find_element_by_id("login-signin")
    b8.click()
    return b9
def fonk4():
    b1, b2 = fonk1()
    print('Program started\n**************START**************\n')
    b9 = webdriver.Safari()
    b9 = fonk3(b2.yahoo_email, b2.yahoo_pw, b9)
    b9.get("https:
    b10 = b9.find_elements_by_xpath("
    for link in b10:
        if link.get_attribute('textContent') == 'History':
            link.click()
    b11 = b9.find_elements_by_xpath(
        f'
    for link in b11:
        if b2.yahoo_league_name in link.get_attribute('outerText'):
            b12 = link.get_attribute('href') + '/draftresults?drafttab=picks&sort=cost&order_by=desc'
            b9.get(b12)
            b13 = b9.find_elements_by_class_name("Table")
            for table in b13:
                b14 = table.get_attribute('innerText')
                if b14[0:4] == 'Pick':
                    b15 = pd.read_csv(StringIO(b14), delimiter='\t', lineterminator='\n')
                    b15['Pick'] = b15['Pick'].astype(int)
                    b15.insert(0, 'Year', b2.yahoo_league_year)
                    b15.rename(b16 = {'Team': 'Owner'}, inplace=True)
                    b15['Player'] = b15['Player'].str.replace(' \\ue03e', '', b17 = True)
                    b15.insert(3, 'Team', [re.search(r'\(([^\)]+)\)', str(x)).group(1).split(' ')[0] for x in b15['Player']])
                    b15.insert(4, 'Position', [re.search(r'\(([^\)]+)\)', str(x)).group(1).split(' ')[2] for x in b15['Player']])
                    b15['Player'] = [re.sub(r'[(].*?[)]', '', str(x)).rstrip() for x in b15['Player']]
                    b18 = f'yahoo_{b2.yahoo_league_name}_{b2.yahoo_league_year}_draft_results.csv'
                    print('Writing to file...' + b18)
                    b15.to_csv(b18, b19 = False)
    b20 = time.time()
    print('Program finished\n\n**************DONE**************\n' + 'Time elapsed: ' + str(b20 - b1) + '\n')
if b21 = = '__main__':
    try:
        fonk4()
    except Exception as err:
        raise err