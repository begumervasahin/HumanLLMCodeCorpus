
b1 = 'b1'
b2 = 'b2'
b3 = {
    'NBA': {b1: 50000, b2: 60000},
    'CBB': {b1: 50000, b2: 60000},
    'WNBA': {b1: 50000, b2: 40000},
    'NFL': {b1: 50000, b2: 60000},
    'CFB': {b1: 50000, b2: 60000},
    'MLB': {b1: 50000, b2: 35000},
    'PGA': {b2: 60000},
    'NASCAR': {b2: 50000},
}
b4 = {
    b1: {'NFL': 9, 'CFB': 8, 'NBA': 8, 'CBB': 8, 'WNBA': 6, 'MLB': 10},
    b2: {'NBA': 9, 'CBB': 9, 'NFL': 9, 'CFB': 9, 'MLB': 9, 'WNBA': 7, 'NASCAR': 5, 'PGA': 6},
}
def fonk1(b5 = 2, wr_min=3, te_min=1, te_upper=2):
    return [
        ['QB', 1, 1],
        ['RB', b5, 3],
        ['WR', wr_min, 4],
        ['TE', te_min, te_upper],
        ['DST', 1, 1]
    ]
def fonk2(b5 = 2, wr_min=3):
    return [
        ['QB', 1, 2],
        ['RB', b5, 3],
        ['WR', wr_min, 4],
    ]
b6 = [['G', 3, 4], ['F', 3, 4], ['C', 1, 2]]
b7 = [['G', 3, 5], ['F', 3, 5]]
b8 = [['G', 2, 3], ['F', 3, 4]]
b9 = {
    'Panthers': 'Carolina Panthers', 'Buccaneers': 'Tampa Bay Buccaneers', 'Dolphins': 'Miami Dolphins',
    'Bears': 'Chicago Bears', 'Raiders': 'Oakland Raiders', 'Patriots': 'New England Patriots',
    'Vikings': 'Minnesota Vikings', 'Eagles': 'Philadelphia Eagles', '49ers': 'San Francisco 49ers',
    'Bengals': 'Cincinnati Bengals', 'Bills': 'Buffalo Bills', 'Broncos': 'Denver Broncos',
    'Browns': 'Cleveland Browns', 'Cardinals': 'Arizona Cardinals', 'Chargers': 'San Diego Chargers',
    'Chiefs': 'Kansas City Chiefs', 'Colts': 'Indianapolis Colts', 'Cowboys': 'Dallas Cowboys',
    'Falcons': 'Atlanta Falcons', 'Giants': 'New York Giants', 'Jaguars': 'Jacksonville Jaguars',
    'Jets': 'New York Jets', 'Lions': 'Detroit Lions', 'Packers': 'Green Bay Packers', 'Rams': 'Los Angeles Rams',
    'Ravens': 'Baltimore Ravens', 'Redskins': 'Washington Redskins', 'Saints': 'New Orleans Saints',
    'Seahawks': 'Seattle Seahawks', 'Steelers': 'Pittsburgh Steelers', 'Texans': 'Houston Texans',
    'Titans': 'Tennessee Titans'
}
print("b1:", b1)
print("b2:", b2)
print("b3:", b3)
print("b4:", b4)
print("b6:", b6)
print("b7:", b7)
print("b8:", b8)
print("DUO_TYPE:", DUO_TYPE)
print("b9:", b9)