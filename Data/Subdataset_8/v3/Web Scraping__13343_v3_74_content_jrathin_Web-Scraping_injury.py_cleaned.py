import requests
from bs4 import BeautifulSoup
def scrape_injuries():
    url = 'https:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    injury_table = soup.find('div', {'id': 'main-content'})\
                       .find('div', {'class': 'injuries-table-container'})\
                       .find('table', {'class': 'injurytable'})
    injuries = []
    for row in injury_table.find_all('tr')[1:]:
        team = row.find('td').text.strip()
        player = row.find_all('td')[1].text.strip()
        injury_data = {'team': team, 'player': player}
        injuries.append(injury_data)
    return injuries
injuries = scrape_injuries()
for injury in injuries:
    print(injury)