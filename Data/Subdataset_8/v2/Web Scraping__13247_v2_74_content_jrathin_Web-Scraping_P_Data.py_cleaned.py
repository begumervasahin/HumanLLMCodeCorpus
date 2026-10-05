import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def scrape_player_info():
    browser = webdriver.Chrome('chromedriver.exe')
    main_url = 'http:
    subpage_tag = 'gerbun.htm'
    browser.get(main_url + subpage_tag)
    main_page_html = browser.page_source
    main_page_soup = BeautifulSoup(main_page_html, "html.parser")
    main_div = main_page_soup.find_all("div", {"id": "main"})
    team_headings = main_div[0].find_all('h5')
    player_list = []
    for team_heading in team_headings:
        team_name = team_heading.text
        team_url = main_url + team_heading.find("a").get("href")
        browser.get(team_url)
        team_page_html = browser.page_source
        team_page_soup = BeautifulSoup(team_page_html, "html.parser")
        team_main_div = team_page_soup.find_all("div", {"id": "main"})
        team_tables = team_main_div[0].find_all('table')
        player_rows = team_tables[0].find('tbody').find_all('tr')
        for player_row in player_rows[1:]:
            player_info = []
            player_columns = player_row.find_all('td')
            try:
                if player_columns[1].text:
                    player_info.append(player_columns[1].text)
                    player_info.append(player_columns[2].text)
                    player_info.append(player_columns[3].text)
                    player_info.append(team_name)
                    player_list.append(player_info)
            except:
                break
    browser.quit()
    return player_list
player_list = scrape_player_info()
for player_info in player_list:
    print(player_info)