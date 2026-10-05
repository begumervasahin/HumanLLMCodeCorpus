import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def scrape_injuries():
    url = 'https:
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    injury_section = soup.find('div', {'class': 'injuries-table-container'})
    injury_headings = injury_section.find_all('h3')
    injury_tables = injury_section.find_all('table', {'class': 'injurytable'})
    injuries = []
    for table in injury_tables:
        rows = table.find('tbody').find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            injury_type = columns[0].get('class')[0]
            player_name = columns[1].text
            injuries.append({'injury_type': injury_type, 'player_name': player_name})
    browser.quit()
    return injuries
injuries_data = scrape_injuries()
for injury in injuries_data:
    print(injury)
    print('----------------------------------------------')