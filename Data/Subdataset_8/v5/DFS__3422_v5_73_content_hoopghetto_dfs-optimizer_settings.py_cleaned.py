
def filter_nfl(player, gametime=None, relax=True):
    min_fppg_threshold = 3
    if player.fppg < min_fppg_threshold or player.injury_indicator + player.injury_details:
        return False
    if gametime is not None and gametime not in player.gametime:
        return False
    return True
def filter_nhl(player, gametime=None, relax=True):
    min_fppg_threshold = 1.0
    min_played_threshold = 2
    if player.fppg < min_fppg_threshold or player.injury_indicator + player.injury_details:
        return False
    if player.played < min_played_threshold:
        return False
    if gametime is not None and gametime not in player.gametime:
        return False
    return True
def filter_mlb(player, gametime=None, relax=True):
    min_fppg_threshold = 1
    min_played_threshold_sp_rp_p = 10
    min_played_threshold_other = 35
    min_batting_order = 1
    if player.fppg < min_fppg_threshold or player.injury_indicator + player.injury_details:
        return False
    if player.position in ['SP', 'RP', 'P'] and player.probable_pitcher != 'Yes':
        return False
    if player.position == ['SP', 'RP', 'P'] and not relax and player.played < min_played_threshold_sp_rp_p:
        return False
    if player.position != ['SP', 'RP', 'P'] and not relax and (player.played < min_played_threshold_other or player.batting_order in ['', 0]):
        return False
    if gametime is not None and gametime not in player.gametime:
        return False
    return True
config = {
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