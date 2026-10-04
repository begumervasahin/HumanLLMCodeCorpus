import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_score(auth, api):
    tennis_ref = 'http:
    tennis_score = BeautifulSoup(urlopen(tennis_ref), 'html.parser')
    tournament_tag = extract_tournament_tag(tennis_score)
    full_round = extract_full_round(tennis_score)
    matches = extract_matches(tennis_score)
    count_matches(matches, auth, api, tournament_tag, full_round)
def extract_tournament_tag(soup):
    tournament = soup.find("div", class_="sec row")
    return ''.join(re.findall(r'([A-Z]\w+-*\w*)', tournament.text))
def extract_full_round(soup):
    round_section = soup.findAll("div", class_="ind sub bold")
    return next((line.text for line in round_section if line.text != "FULL TOURNAMENT RESULTS"), "")
def extract_matches(soup):
    game_section = soup.findAll("div", class_="ind")
    return [line.text.split("Final")[0] for line in game_section if "Final" in line.text]
def count_matches(matches, auth, api, tournament_tag, full_round):
    match_count = sum(1 for match in matches if match)
    final_score(matches, match_count, auth, api, tournament_tag, full_round)
def final_score(matches, count, auth, api, tournament_tag, full_round):
    for match in matches:
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            score = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            players = re.findall(r'([A-Z]\w+-*\w*)', score)
            round_name = re.findall(r'^[^:]+', full_round)
            if len(players) > 1:
                print(f"{round_name[0]} of the {tournament_tag}")
                print(f"Match: {players[0]} vs {players[1]}")
                print(f"Score: {score}")
