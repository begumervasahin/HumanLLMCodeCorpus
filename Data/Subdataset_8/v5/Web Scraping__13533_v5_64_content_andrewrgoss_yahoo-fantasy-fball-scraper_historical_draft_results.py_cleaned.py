
import argparse
import re
import time
from io import StringIO
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def init_config():
    start_time = time.time()
    args = parse_arguments()
    return start_time, args
def parse_arguments():
    parser = argparse.ArgumentParser(description='Parse command line arguments')
    parser.add_argument('--yahoo_email', type=str, required=True, help='Yahoo email address for account login.')
    parser.add_argument('--yahoo_pw', type=str, required=True, help='Password for Yahoo account login.')
    parser.add_argument('--yahoo_league_name', type=str, required=True, help='Name of Yahoo fantasy football league.')
    parser.add_argument('--yahoo_league_year', type=str, required=True, help='Historical league year for draft results.')
    return parser.parse_args()
def yahoo_account_login(user_email, user_pw, browser):
    browser.get('https:
    email_input = browser.find_element_by_id('login-username')
    email_input.send_keys(user_email)
    login_button = browser.find_element_by_id("login-signin")
    login_button.click()
    pw_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-passwd")))
    pw_input.send_keys(user_pw)
    submit_button = browser.find_element_by_id("login-signin")
    submit_button.click()
    return browser
def main():
    start_time, args = init_config()
    print('Program started\n**************START**************\n')
    browser = webdriver.Safari()
    browser = yahoo_account_login(args.yahoo_email, args.yahoo_pw, browser)
    browser.get("https:
    history_link = browser.find_elements_by_xpath("
    for link in history_link:
        if link.get_attribute('textContent') == 'History':
            link.click()
    draft_links = browser.find_elements_by_xpath(
        f'
    for link in draft_links:
        if args.yahoo_league_name in link.get_attribute('outerText'):
            draft_url = link.get_attribute('href') + '/draftresults?drafttab=picks&sort=cost&order_by=desc'
            browser.get(draft_url)
            tables = browser.find_elements_by_class_name("Table")
            for table in tables:
                table_data = table.get_attribute('innerText')
                if table_data[0:4] == 'Pick':
                    df = pd.read_csv(StringIO(table_data), delimiter='\t', lineterminator='\n')
                    df['Pick'] = df['Pick'].astype(int)
                    df.insert(0, 'Year', args.yahoo_league_year)
                    df.rename(columns={'Team': 'Owner'}, inplace=True)
                    df['Player'] = df['Player'].str.replace(' \\ue03e', '', regex=True)
                    df.insert(3, 'Team', [re.search(r'\(([^\)]+)\)', str(x)).group(1).split(' ')[0] for x in df['Player']])
                    df.insert(4, 'Position', [re.search(r'\(([^\)]+)\)', str(x)).group(1).split(' ')[2] for x in df['Player']])
                    df['Player'] = [re.sub(r'[(].*?[)]', '', str(x)).rstrip() for x in df['Player']]
                    output_file = f'yahoo_{args.yahoo_league_name}_{args.yahoo_league_year}_draft_results.csv'
                    print('Writing to file...' + output_file)
                    df.to_csv(output_file, index=False)
    end_time = time.time()
    print('Program finished\n\n**************DONE**************\n' + 'Time elapsed: ' + str(end_time - start_time) + '\n')
if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        raise err