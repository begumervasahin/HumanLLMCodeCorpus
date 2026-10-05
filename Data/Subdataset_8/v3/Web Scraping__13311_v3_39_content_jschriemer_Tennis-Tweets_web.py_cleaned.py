import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fetch_tennis_scores(url):
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')
    game_sections = soup.find_all("div", class_="ind")
    tournament_section = soup.find("div", class_="sec row")
    tournament_name = extract_tournament_info(tournament_section)
    round_info = extract_round_info(soup)
    matches = extract_matches(game_sections)
    print_matches(matches, tournament_name, round_info)
def extract_tournament_info(tournament_section):
    tournament_info = tournament_section.text
    return ' '.join(re.findall(r'([A-Z]\w+-*\w*)', tournament_info))
def extract_round_info(soup):
    round_sections = soup.find_all("div", class_="ind sub bold")
    for section in round_sections:
        if section.text != "FULL TOURNAMENT RESULTS":
            return section.text
def extract_matches(game_sections):
    matches = []
    for section in game_sections:
        if "Final" in section.text:
            match_info = section.text.split("Final")
            matches.extend(match_info)
    return matches
def print_matches(matches, tournament_name, round_info):
    print(f"Tournament Round: {round_info} of the Tournament: {tournament_name}")
    for match in matches:
        match = match.strip()
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            process_match(match)
def process_match(match):
    score = re.sub(r'([a-z])(\d{1})', r'\1 \2', match.strip())
    players = re.findall(r'([A-Z]\w+-*\w*)', score)
    if len(players) >= 2:
        player1, player2 = players[:2]
        print(f"Match: {player1} vs {player2}")
        print(f"Score: {score.strip()}\n")
if __name__ == "__main__":
    tennis_url = 'http:
    fetch_tennis_scores(tennis_url)