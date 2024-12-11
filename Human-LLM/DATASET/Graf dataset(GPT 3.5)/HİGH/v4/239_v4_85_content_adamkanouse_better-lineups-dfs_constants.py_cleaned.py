
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
    'NBA': [['PG', 1, 3], ['SG', 1, 3], ['SF', 1, 3], ['PF', 1, 3], ['C', 1, 2]],
    'CBB': [['PG', 0, 5], ['SG', 0, 5], ['SF', 0, 3], ['PF', 0, 3], ['C', 0, 2]],
    'WNBA': [['PG', 1, 3], ['SG', 1, 3], ['SF', 1, 4], ['PF', 1, 4]],
    'NFL': fonk1(),
    'CFB': fonk2(),
    'MLB': [['SP', 2, 2], ['C', 1, 1], ['1B', 1, 1], ['2B', 1, 1], ['3B', 1, 1], ['SS', 1, 1], ['OF', 3, 3]],
}
b10 = {
    'NBA': [['PG', 2, 2], ['SG', 2, 2], ['SF', 2, 2], ['PF', 2, 2], ['C', 1, 1]],
    'NFL': fonk1(),
    'CFB': fonk2(),
    'MLB': [['P', 1, 1], ['1B', 1, 2], ['2B', 1, 2], ['3B', 1, 2], ['SS', 1, 2], ['OF', 3, 4]],
    'WNBA': [['G', 3, 3], ['F', 4, 4]],
    'NASCAR': [['D', 5, 5]],
    'PGA': [['G', 6, 6]],
}
b11 = {
    b1: {'NBA': b6, 'CBB': b7, 'WNBA': b8},
    b2: {'NBA': b6, 'CBB': b7, 'WNBA': b8},
}
b12 = {
    'wr': [['QB', 1, 1], ['WR', 1, 1]],
    'te': [['QB', 1, 1], ['TE', 1, 1]],
    'rb': [['QB', 1, 1], ['rb', 1, 1]],
}
b13 = {
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