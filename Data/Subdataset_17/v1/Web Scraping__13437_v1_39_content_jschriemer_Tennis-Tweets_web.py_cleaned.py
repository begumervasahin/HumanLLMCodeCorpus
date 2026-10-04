import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_score():
    tennis_ref = 'http:
    score_url = urlopen(tennis_ref)
    tennis_score = BeautifulSoup(score_url, 'html.parser')
    tournament = tennis_score.find("div", class_="sec row")
    tournament_tag = ''.join(re.findall(r'([A-Z]\w+-*\w*)', tournament.text))
    round_section = tennis_score.findAll("div", class_="ind sub bold")
    fullround = next((line.text for line in round_section if line.text != "FULL TOURNAMENT RESULTS"), "")
    game_section = tennis_score.findAll("div", class_="ind")
    matches = [line.text.split("Final")[0] for line in game_section if "Final" in line.text]
    count_match(matches, tournament_tag, fullround)
def count_match(matches, tournament_tag, fullround):
    count = sum(1 for match in matches if match)
    final_score(matches, count, tournament_tag, fullround)
def final_score(matches, count, tournament_tag, fullround):
    for match in matches:
        if match and match not in ["FULL TOURNAMENT RESULTS", "TENNIS HOME PAGE"]:
            score = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            players = re.findall(r'([A-Z]\w+-*\w*)', score)
            round_info = re.findall(r'^[^:]+', fullround)
            if len(players) > 1:
                print(f"{round_info[0]} of the {tournament_tag}: {players[0]} vs {players[1]}")
                print(f"Score: {score}")
get_score()