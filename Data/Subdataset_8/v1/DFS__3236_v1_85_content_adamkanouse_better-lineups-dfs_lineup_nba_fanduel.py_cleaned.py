import random
import numpy as np
from collections import Counter
from optimize import run as optimizer_run
from argparse import Namespace
from csv_parse.nba_upload import update_upload_csv, create_upload_file, map_pids
DEFAULT_ARGS = {
    'duo': 'n',
    's': 'n',
    'w': 5,
    'i': 1,
    'league': 'NBA',
    'limit': 'n',
    'lp': 0,
    'mp': 500,
    'ms': 100000,
    'sp': 1000,
    'banned': [],
    'historical_date': None,
    'game': 'fanduel',
    'po': 0,
    'pids': 'data/pid-file-nba-fanduel.csv',
    'salary_file': 'data/current-nba-salaries-fanduel.csv',
    'projection_file': 'data/current-nba-projections-fanduel.csv',
    'home': None,
    'v_avg': 100,
    'source': 'nba_rotogrinders',
    'historical': None,
    'season': None,
    'dtype': None,
    'flex_position': None,
    'locked': [],
    'teams': None,
    'po_location': None,
    'min_avg': None,
}
def is_duplicate(roster, roster_list):
    roster_players = sorted([p.name for p in roster.players])
    return any(sorted([p.name for p in r.players]) == roster_players for r in roster_list)
def run(lineups, exposure, min_avg):
    DEFAULT_ARGS['min_avg'] = min_avg
    roster_list, player_list = [], []
    max_exposure = lineups * exposure
    exposure_counter = None
    for _ in range(lineups):
        args = DEFAULT_ARGS.copy()
        if exposure_counter:
            args['banned'] = [name for name, freq in exposure_counter.items() if freq > max_exposure]
        roster = optimizer_run('NBA', Namespace(**args), [])
        if is_duplicate(roster, roster_list):
            while is_duplicate(roster, roster_list):
                args['banned'].append(random.choice(roster.players).name)
                roster = optimizer_run('NBA', Namespace(**args), [])
        roster_list.append(roster)
        player_list += [p.name for p in roster.players]
        exposure_counter = Counter(player_list)
    unique_lineups = len(set([str(r.players) for r in roster_list]))
    if unique_lineups != lineups:
        raise Exception('Duplication error in logic. Expected {} and got {} lineups'.format(lineups, unique_lineups))
    scores = [r.projected() for r in roster_list]
    print('Generated {} lineups.'.format(lineups))
    print('Maximum score: {}'.format(np.max(scores)))
    print('Minimum score: {}'.format(np.min(scores)))
    print('Average score: {}'.format(np.average(scores)))
    print('Median score: {}'.format(np.median(scores)))
if __name__ == '__main__':
    lineups = 3
    exposure = 0.5
    min_avg = 10
    run(lineups, exposure, min_avg)