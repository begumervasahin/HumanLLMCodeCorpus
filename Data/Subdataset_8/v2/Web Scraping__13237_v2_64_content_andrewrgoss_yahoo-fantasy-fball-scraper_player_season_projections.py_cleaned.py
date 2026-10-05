
import argparse
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
def init_config():
    start = time.time()
    arg_list = get_arg_list()
    return start, arg_list
def get_arg_list():
    parser = argparse.ArgumentParser(description='Retrieve Yahoo fantasy football player projections')
    parser.add_argument('--yahoo_email', type=str, required=True, help='Yahoo email address for account login.')
    parser.add_argument('--yahoo_pw', type=str, required=True, help='Password for Yahoo account login.')
    parser.add_argument('--yahoo_league_id', type=str, required=True, help='ID associated with Yahoo fantasy football league.')
    parser.add_argument('--yahoo_league_year', type=str, required=True, help='Current league year for player projections.')
    return parser.parse_args()
def yahoo_account_login(user_email, user_pw, browser):
    browser.get('https:
    email_elem = browser.find_element_by_id('login-username')
    email_elem.send_keys(user_email)
    login_btn = browser.find_element_by_id('login-signin')
    login_btn.click()
    pw_elem = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, 'login-passwd')))
    pw_elem.send_keys(user_pw)
    submit_btn = browser.find_element_by_id('login-signin')
    submit_btn.click()
    return browser
def write_player_record_to_csv(csv_extract, player_details, player_status, player_projections):
    csv_contents = '\n' + ' '.join(player_details[:-3]) + '{0}' + player_details[-3] + '{0}' + player_details[-1] + '{0}' + player_status + '{0}'
    for player_projection in player_projections:
        csv_contents = csv_contents + player_projection + '{0}'
    with open(csv_extract, 'a') as output_file:
        output_file.write(csv_contents.format(',')[:-1])
def main():
    start, args = init_config()
    print('Program started\n**************START**************\n')
    csv_extract = datetime.now().strftime('%Y_%m_%d_') + 'yahoo_player_season_projections.csv'
    with open(csv_extract, 'a') as output_file:
        output_file.write(
            'PLAYER_NAME,TEAM,POSITION,PLAYER_STATUS,GP*,BYE,FANTASY_POINTS,PRESEASON_RANKING,ACTUAL_RANKING,%_ROSTERED,PASSING_YDS,'
            'PASSING_TD,PASSING_INT,RUSHING_ATT,RUSHING_YDS,RUSHING_TD,RECEPTIONS,RECEIVING_YDS,RECEIVING_TD,TARGETS,RET_TD,'
            '2PT_CONVERSIONS,FUMBLES_LOST')
    browser = webdriver.Safari()
    browser = yahoo_account_login(args.yahoo_email, args.yahoo_pw, browser)
    print('Extracting Yahoo! fantasy football player season projections...')
    pagination = 0
    while pagination <= 275:
        browser.get('https:
                    .format(args.yahoo_league_id, args.yahoo_league_year, str(pagination)))
        tables = browser.find_elements_by_class_name('Table')
        table_data = tables[0].get_attribute('innerText')
        table_rows = table_data.splitlines()
        del table_rows[:38]
        i = 0
        player_details = []
        player_status = 'A'
        player_projections = []
        for table_row in table_rows:
            if i == 2:
                player_details = table_row.split(' ')
                print(' '.join(player_details[:-3]))
                i += 1
            elif table_row.lower() in ('ir', 'nfi-r', 'nfi-a', 'o', 'pup', 'pup-p', 'd', 'na', 'p', 'q', 'susp'):
                player_status = table_row
                continue
            elif 'forecast' in table_row.lower():
                continue
            elif i in (0, 1, 3, 4, 5, 25):
                i += 1
                pass
            elif 'note' in table_row.lower():
                write_player_record_to_csv(csv_extract, player_details, player_status, player_projections)
                i = 2
                player_projections = []
                player_status = 'A'
                continue
            else:
                player_projections.append(table_row)
                i += 1
                continue
        write_player_record_to_csv(csv_extract, player_details, player_status, player_projections)
        pagination += 25
    end = time.time()
    print('Program finished\n\n**************DONE**************\n' + 'Time elapsed: ' + str(end - start) + '\n')
if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        raise err