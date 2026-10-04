
from Team import Team
def create_team_list():
    teams_data = [
        ('ATL', 'Atlanta'),
        ('BOS', 'Boston'),
        ('BKN', 'Brooklyn'),
        ('CHA', 'Charlotte'),
        ('CHI', 'Chicago'),
        ('CLE', 'Cleveland'),
        ('DAL', 'Dallas'),
        ('DEN', 'Denver'),
        ('DET', 'Detroit'),
        ('GSW', 'Golden State'),
        ('HOU', 'Houston'),
        ('IND', 'Indiana'),
        ('LAC', 'LA Clippers'),
        ('LAL', 'LA Lakers'),
        ('MEM', 'Memphis'),
        ('MIA', 'Miami'),
        ('MIL', 'Milwaukee'),
        ('MIN', 'Minnesota'),
        ('NOP', 'New Orleans'),
        ('NY', 'New York'),
        ('OKC', 'Oklahoma City'),
        ('ORL', 'Orlando'),
        ('PHI', 'Philadelphia'),
        ('PHO', 'Phoenix'),
        ('POR', 'Portland'),
        ('SAC', 'Sacramento'),
        ('SA', 'San Antonio'),
        ('TOR', 'Toronto'),
        ('UTA', 'Utah'),
        ('WAS', 'Washington')
    ]
    teams = [Team([abbreviation, name]) for abbreviation, name in teams_data]
    return teams
team_list = create_team_list()