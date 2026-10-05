import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def start():
    browser = webdriver.Chrome('chromedriver.exe')
    base_url = 'http:
    tag = 'gerbun.htm'
    url = base_url + tag
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    main_div = soup.find("div", {"id": "main"})
    team_headings = main_div.find_all('h5')
    player_list = []
    for team_heading in team_headings:
        team_name = team_heading.text
        team_url = base_url + team_heading.find("a").get("href")
        browser.get(team_url)
        team_html = browser.page_source
        team_soup = BeautifulSoup(team_html, "html.parser")
        team_main_div = team_soup.find("div", {"id": "main"})
        tables = team_main_div.find_all('table')
        player_table = tables[0].find('tbody')
        player_rows = player_table.find_all('tr')
        for player_row in player_rows[1:]:
            player_data = player_row.find_all('td')
            try:
                if player_data[1].text.strip():
                    player_info = [
                        player_data[1].text.strip(),
                        player_data[2].text.strip(),
                        player_data[3].text.strip(),
                        team_name
                    ]
                    player_list.append(player_info)
            except IndexError:
                break
    browser.quit()
    return player_list