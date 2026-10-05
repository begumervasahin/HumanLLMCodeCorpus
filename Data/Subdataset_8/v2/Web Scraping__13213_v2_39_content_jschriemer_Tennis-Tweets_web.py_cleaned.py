import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_tennis_scores():
    tennis_url = 'http:
    with urlopen(tennis_url) as response:
        soup = BeautifulSoup(response, 'html.parser')
    game_sections = soup.find_all("div", class_="ind")
    tournament_section = soup.find("div", class_="sec row")
    tournament_info = tournament_section.text
    tournament_name = ' '.join(re.findall(r'([A-Z]\w+-*\w*)', tournament_info))
    round_sections = soup.find_all("div", class_="ind sub bold")
    for section in round_sections:
        if section.text != "FULL TOURNAMENT RESULTS":
            round_info = section.text
            break
    matches = []
    for section in game_sections:
        if "Final" in section.text:
            match_info = section.text.split("Final")
            matches.extend(match_info)
    count_matches(matches, tournament_name, round_info)
def count_matches(matches, tournament_name, round_info):
    match_count = sum(1 for match in matches if match.strip())
    print(f"Tournament Round: {round_info} of the Tournament: {tournament_name}")
    for match in matches:
        if match.strip() and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            process_match(match, round_info)
def process_match(match, round_info):
    score = re.sub(r'([a-z])(\d{1})', r'\1 \2', match.strip())
    players = re.findall(r'([A-Z]\w+-*\w*)', score)
    if len(players) >= 2:
        player1, player2 = players[:2]
        print(f"Match: {player1} vs {player2}")
        print(f"Score: {score.strip()}\n")
if __name__ == "__main__":
    get_tennis_scores()