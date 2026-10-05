import argparse
import pandas as pd
import re
import time
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
def init_config():
    start_time = time.time()
    arguments = get_arguments()
    return start_time, arguments
def get_arguments():
    parser = argparse.ArgumentParser(description='Parse command line arguments')
    parser.add_argument('--yahoo_email', type=str, required=True, help='Yahoo email address for account login.')
    parser.add_argument('--yahoo_pw', type=str, required=True, help='Password for Yahoo account login.')
    parser.add_argument('--yahoo_league_name', type=str, required=True, help='Name associated with Yahoo fantasy football league.')
    parser.add_argument('--yahoo_league_year', type=str, required=True, help='Historical league year to extract auction draft results from.')
    return parser.parse_args()
def yahoo_login(email, password, browser):
    browser.get('https:
    email_element = browser.find_element_by_id('login-username')
    email_element.send_keys(email)
    login_button = browser.find_element_by_id("login-signin")
    login_button.click()
    password_element = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "login-passwd"))
    )
    password_element.send_keys(password)
    submit_button = browser.find_element_by_id("login-signin")
    submit_button.click()
    return browser
def main():
    start_time, args = init_config()
    print('Program started\n**************START**************\n')
    browser = webdriver.Safari()
    browser = yahoo_login(args.yahoo_email, args.yahoo_pw, browser)
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
                    output_file = 'yahoo_{0}_{1}_draft_results.csv'.format(args.yahoo_league_name, args.yahoo_league_year)
                    print(f'Writing to file...{output_file}')
                    df.to_csv(output_file, index=False)
    end_time = time.time()
    print('Program finished\n\n**************DONE**************\n' + 'Time elapsed: ' + str(end_time - start_time) + '\n')
if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        raise err