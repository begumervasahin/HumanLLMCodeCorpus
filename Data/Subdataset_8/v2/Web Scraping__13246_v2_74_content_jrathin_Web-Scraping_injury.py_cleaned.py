import requests
from bs4 import BeautifulSoup
def injury_scrape():
    url = 'https:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    injury_table = soup.find('div', {'id': 'main-content'})\
                       .find('div', {'class': 'injuries-table-container'})\
                       .find('table', {'class': 'injurytable'})
    injury_list = []
    for row in injury_table.find_all('tr')[1:]:
        columns = row.find_all('td')
        team = columns[0].text.strip()
        player = columns[1].text.strip()
        injury_data = {'team': team, 'player': player}
        injury_list.append(injury_data)
    return injury_list
injuries = injury_scrape()
for injury in injuries:
    print(injury)