import argparse
from io import StringIO
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
def init_config():
    start = time.time()
    arg_list = get_arg_list()
    return start, arg_list
def get_arg_list():
    parser = argparse.ArgumentParser(description='Parses command line arguments')
    parser.add_argument('--yahoo_email', type=str, required=True, help='Yahoo email address for account login.')
    parser.add_argument('--yahoo_pw', type=str, required=True, help='Password for Yahoo account login.')
    parser.add_argument('--yahoo_league_name', type=str, required=True, help='Name associated with Yahoo fantasy football league.')
    parser.add_argument('--yahoo_league_year', type=str, required=True, help='Historical league year to extract auction draft results from.')
    return parser.parse_args()
def yahoo_account_login(user_email, user_pw, browser):
    browser.get('https:
    email_elem = browser.find_element_by_id('login-username')
    email_elem.send_keys(user_email)
    login_btn = browser.find_element_by_id("login-signin")
    login_btn.click()
    pw_elem = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "login-passwd"))
    )
    pw_elem.send_keys(user_pw)
    submit_btn = browser.find_element_by_id("login-signin")
    submit_btn.click()
    return browser
def main():
    start, args = init_config()
    print('Program started\n**************START**************\n')
    browser = webdriver.Safari()
    browser = yahoo_account_login(args.yahoo_email, args.yahoo_pw, browser)
    browser.get("https:
    elements = browser.find_elements_by_xpath("
    for element in elements:
        if element.get_attribute('textContent') == 'History':
            element.click()
    elements = browser.find_elements_by_xpath(
        '
    for element in elements:
        if args.yahoo_league_name in element.get_attribute('outerText'):
            browser.get(element.get_attribute('href') + '/draftresults?drafttab=picks&sort=cost&order_by=desc')
            tables = browser.find_elements_by_class_name("Table")
            for table in tables:
                table_data = table.get_attribute('innerText')
                if table_data[0:4] == 'Pick':
                    df = pd.read_csv(StringIO(table_data), delimiter='\t', lineterminator='\n')
                    df['Pick'] = df['Pick'].astype(int)
                    df.insert(0, 'Year', args.yahoo_league_year)
                    df.rename(columns={'Team': 'Owner'}, inplace=True)
                    df['Player'] = df['Player'].str.replace(' \\ue03e', '', regex=True)
                    df.insert(3, 'Team',
                              [re.search(r'\(([^\)]+)\)', str(x)).group(1).split(' ')[0] for x in df['Player']])
                    df.insert(4, 'Position',
                              [re.search(r'\(([^\)]+)\)', str(x)).group(1).split(' ')[2] for x in df['Player']])
                    df['Player'] = [re.sub(r'[(].*?[)]', '', str(x)).rstrip() for x in df['Player']]
                    print('Writing to file...yahoo_{0}_{1}_draft_results.csv'.format(args.yahoo_league_name,
         args.yahoo_league_year))
                    df.to_csv('yahoo_{0}_{1}_draft_results.csv'.format(args.yahoo_league_name,
                                                                       args.yahoo_league_year), index=False)
    end = time.time()
    print('Program finished\n\n**************DONE**************\n' + 'Time elapsed: ' + str(end - start) + '\n')
if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        raise err