class Player:
    def __init__(self, fppg, injury_indicator, injury_details, gametime, played, position, probable_pitcher, batting_order):
        self.fppg = fppg
        self.injury_indicator = injury_indicator
        self.injury_details = injury_details
        self.gametime = gametime
        self.played = played
        self.position = position
        self.probable_pitcher = probable_pitcher
        self.batting_order = batting_order
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
    min_played_threshold = 10 if player.position in ['SP', 'RP', 'P'] else 35
    min_batting_order = 1
    if player.fppg < min_fppg_threshold or player.injury_indicator + player.injury_details:
        return False
    if player.position in ['SP', 'RP', 'P'] and player.probable_pitcher != 'Yes':
        return False
    if player.position == ['SP', 'RP', 'P'] and not relax and player.played < min_played_threshold:
        return False
    if player.position != ['SP', 'RP', 'P'] and not relax and (player.played < min_played_threshold or player.batting_order < min_batting_order):
        return False
    if gametime is not None and gametime not in player.gametime:
        return False
    return True
def create_team(config, site, sport):
    salary = config[site][sport]['salary']
    composition = config[site][sport]['composition']
    filter_func = config[site][sport]['filter']
    eligible_players = [player for player in all_players if filter_func(player)]
    team = {}
    remaining_salary = salary
    for position, num_players in composition.items():
        position_players = [player for player in eligible_players if player.position == position]
        position_players.sort(key=lambda x: x.fppg, reverse=True)
        selected_players = position_players[:num_players]
        team[position] = selected_players
        remaining_salary -= sum(player.fppg for player in selected_players)
    return team
all_players = [
    Player(5, '', '', ['Sunday'], 10, 'QB', '', ''),
    Player(4, '', '', ['Sunday'], 12, 'RB', '', ''),
    Player(6, '', '', ['Sunday'], 9, 'RB', '', ''),
]
config = {
    'FanDuel': {
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
        'MLB': {
            'salary': 35000,
            'composition': {'P': 1, 'C': 1, '1B': 1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3},
            'filter': filter_mlb
        }
    },
    'DraftKings': {
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
        'MLB': {
            'salary': 50000,
            'composition': {'SP': 2, 'C': 1, '1B': 1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3},
            'filter': filter_mlb
        }
    }
}
team_fanduel_nfl = create_team(config, 'FanDuel', 'NFL')
team_draftkings_mlb = create_team(config, 'DraftKings', 'MLB')
