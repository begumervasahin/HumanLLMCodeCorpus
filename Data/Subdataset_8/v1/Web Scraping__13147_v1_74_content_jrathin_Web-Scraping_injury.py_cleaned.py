import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def injuryScrap():
    url = 'https:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    injury_table = soup.find('div', {'id': 'main-content'}).find('div', {'class': 'injuries-table-container'}).find('table', {'class': 'injurytable'})
    injury_list = []
    for row in injury_table.find_all('tr')[1:]:
        columns = row.find_all('td')
        team = columns[0].text.strip()
        player = columns[1].text.strip()
        injury_list.append({'team': team, 'player': player})
    return injury_list
injuries = injuryScrap()
for injury in injuries:
    print(injury)