import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_tennis_scores(auth, api):
    tennis_ref = 'http:
    score_url = urlopen(tennis_ref)
    tennis_score = BeautifulSoup(score_url, 'html.parser')
    tournament = tennis_score.find("div", class_="sec row").text
    tournament_tag = re.findall(r'([A-Z]\w+-*\w*)', tournament)
    round_section = tennis_score.findAll("div", class_="ind sub bold")
    full_round = ""
    for line in round_section:
        if line.text != "FULL TOURNAMENT RESULTS":
            full_round = line.text
    game_section = tennis_score.findAll("div", class_="ind")
    matches = []
    for line in game_section:
        if line.text.find("Final") >= 0:
            word = line.text.split("Final")
            matches.extend(word)
    count_matches(matches, auth, api, tournament_tag, full_round)
def count_matches(matches, auth, api, tournament_tag, full_round):
    count = sum(1 for match in matches if match)
    final_score(matches, count, auth, api, tournament_tag, full_round)
def final_score(matches, count, auth, api, tournament_tag, full_round):
    for match in matches:
        if match and match != "FULL TOURNAMENT RESULTS" and match != "TENNIS HOME PAGE":
            score = re.sub(r'([a-z])(\d{1})', r'\1 \2', match)
            players = re.findall(r'([A-Z]\w+-*\w*)', score)
            round_info = re.findall(r'^[^:]+', full_round)
            if len(players) > 1:
                print(f"{round_info[0]} of the...")