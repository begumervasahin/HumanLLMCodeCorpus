
from Team import Team
def fonk1():
    b1 = [
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
    b2 = [Team([abbreviation, name]) for abbreviation, name in b1]
    return b2
b3 = fonk1()