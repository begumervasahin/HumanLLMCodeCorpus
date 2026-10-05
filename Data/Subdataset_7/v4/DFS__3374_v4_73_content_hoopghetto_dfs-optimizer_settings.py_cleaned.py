
def fonk1(player, b1 = None, relax=True):
    a1 = 3
    if player.fppg < a1 or player.injury_indicator + player.injury_details:
        return False
    if b1 is not None and b1 not in player.b1:
        return False
    return True
def fonk2(player, b1 = None, relax=True):
    a1 = 1.0
    a2 = 2
    if player.fppg < a1 or player.injury_indicator + player.injury_details:
        return False
    if player.played < a2:
        return False
    if b1 is not None and b1 not in player.b1:
        return False
    return True
def fonk3(player, b1 = None, relax=True):
    a1 = 1
    a3 = 10
    a4 = 35
    a5 = 1
    if player.fppg < a1 or player.injury_indicator + player.injury_details:
        return False
    if player.b2 in ['SP', 'RP', 'P'] and player.probable_pitcher != 'Yes':
        return False
    if player.b2 = = ['SP', 'RP', 'P'] and not relax and player.played < a3:
        return False
    if player.b2 != ['SP', 'RP', 'P'] and not relax and (player.played < a4 or player.batting_order in ['', 0]):
        return False
    if b1 is not None and b1 not in player.b1:
        return False
    return True
b3 = {
    'FanDuel': {
        'MLB': {
            'salary': 35000,
            'composition': {'P': 1, 'C': 1, '1B': 1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3},
            'filter': filter_mlb
        },
        'NFL': {
            'salary': 60000,
            'composition': {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'K': 1, 'D': 1},
            'filter': filter_nfl
        },
        'NHL': {
            'salary': 55000,
            'composition': {'LW': 2, 'RW': 2, 'C': 2, 'D': 2, 'G': 1},
            'filter': filter_nhl
        },
    },
    'DraftKings': {
        'MLB': {
            'salary': 50000,
            'composition': {'SP': 2, 'C': 1, '1B': 1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3},
            'filter': filter_mlb
        },
        'NFL': {
            'salary': 60000,
            'composition': {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'K': 1, 'D': 1},
            'filter': filter_nfl
        },
        'NHL': {
            'salary': 55000,
            'composition': {'LW': 2, 'RW': 2, 'C': 2, 'D': 2, 'G': 1},
            'filter': filter_nhl
        },
    }
}