
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_score(auth, api):
    tennis_ref = 'http:
    score_url = urlopen(tennis_ref)
    tennis_score = BeautifulSoup(score_url, 'html.parser')
    game_section = tennis_score.findAll("div", class_="ind")
    tournament = tennis_score.find("div", class_="sec row")
    words = tournament.text
    length = len(re.findall(r'([A-Z]\w+-*\w*)', words))
    tourna = re.findall(r'([A-Z]\w+-*\w*)', words)
    tournament_tag = ''
    i = 0
    while(i < length):
        tournament_tag = tournament_tag + tourna[i]
        i = i + 1
    round_section = tennis_score.findAll("div", class_="ind sub bold")
    fullround = ""
    for line in round_section:
        if line.text != "FULL TOURNAMENT RESULTS":
            fullround = line.text
    matches = []
    for line in game_section:
        print(line)
        print(line.text.find("Final"))
        if (line.text.find("Final") >= 0):
            print("check!")
            print(line)
            word = line.text.split("Final")
            matches = matches + word
    print(matches)
    count_match(matches, auth, api, tournament_tag, fullround)
def count_match(matches, auth, api, tournament_tag, fullround):
    count = 0
    for i in range(len(matches)):
        if matches[i] != "":
            count = count + 1
    final_score(matches, count, auth, api, tournament_tag, fullround)
def final_score(matches, count, auth, api, tournament_tag, fullround):
    for i in range(len(matches)):
        if matches[i] != "" and matches[i] != "FULL TOURNAMENT RESULTS" and matches[i] != "TENNIS HOME PAGE":
            score = re.sub(r'([a-z])(\d{1})', r'\1 \2', matches[i])
            player = re.findall(r'([A-Z]\w+-*\w*)', score)
            round = re.findall(r'^[^:]+', fullround)
            if(len(player)>1):
                print(round[0] + " of the