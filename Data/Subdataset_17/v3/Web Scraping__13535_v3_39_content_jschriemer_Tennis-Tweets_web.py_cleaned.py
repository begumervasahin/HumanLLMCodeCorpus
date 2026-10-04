import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def fetch_tennis_scores():
    url = 'http:
    response = urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    tournament_name = extract_tournament_name(soup)
    round_name = extract_round_name(soup)
    match_scores = extract_match_scores(soup)
    display_final_scores(match_scores, tournament_name, round_name)
def extract_tournament_name(soup):
    tournament_info = soup.find("div", class_="sec row")
    return ''.join(re.findall(r'([A-Z]\w+-*\w*)', tournament_info.text))
def extract_round_name(soup):
    round_info = soup.findAll("div", class_="ind sub bold")
    return next((line.text for line in round_info if line.text != "FULL TOURNAMENT RESULTS"), "")
def extract_match_scores(soup):
    matches_info = soup.findAll("div", class_="ind")
    return [line.text.split("Final")[0] for line in matches_info if "Final" in line.text]
def display_final_scores(match_scores, tournament_name, round_name):
    for match in match_scores:
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            formatted_score = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            players = re.findall(r'([A-Z]\w+-*\w*)', formatted_score)
            round_details = re.findall(r'^[^:]+', round_name)
            if len(players) > 1:
                print(f"{round_details[0]} of the {tournament_name}: {players[0]} vs {players[1]}")
                print(f"Score: {formatted_score}")
fetch_tennis_scores()