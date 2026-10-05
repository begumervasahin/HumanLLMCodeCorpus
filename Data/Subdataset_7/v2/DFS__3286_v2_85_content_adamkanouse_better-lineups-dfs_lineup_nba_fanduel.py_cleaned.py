import random
import numpy as np
from collections import Counter
from optimize import run as optimizer_run
from argparse import Namespace
from csv_parse.nba_upload import update_upload_csv, create_upload_file, map_pids
b1 = {
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
    'a3': None,
}
def fonk1(b7, roster_list):
    b2 = sorted([p.name for p in b7.players])
    return any(sorted([p.name for p in r.players]) == b2 for r in roster_list)
def fonk2(a1, a2, a3):
    b1['a3'] = a3
    roster_list, b3 = [], []
    b4 = a1 * a2
    b5 = None
    for _ in range(a1):
        b6 = b1.copy()
        if b5:
            b6['banned'] = [name for name, freq in b5.items() if freq > b4]
        b7 = optimizer_run('NBA', Namespace(**b6), [])
        if fonk1(b7, roster_list):
            while fonk1(b7, roster_list):
                b6['banned'].append(random.choice(b7.players).name)
                b7 = optimizer_run('NBA', Namespace(**b6), [])
        roster_list.append(b7)
        b3 += [p.name for p in b7.players]
        b5 = Counter(b3)
    b8 = len(set([str(r.players) for r in roster_list]))
    if b8 != a1:
        raise Exception('Duplication error in logic. Expected {} and got {} a1'.format(a1, b8))
    b9 = [r.projected() for r in roster_list]
    print('Generated {} a1.'.format(a1))
    print('Maximum score: {}'.format(np.max(b9)))
    print('Minimum score: {}'.format(np.min(b9)))
    print('Average score: {}'.format(np.average(b9)))
    print('Median score: {}'.format(np.median(b9)))
if b10 = = '__main__':
    a1 = 3
    a2 = 0.5
    a3 = 10
    fonk2(a1, a2, a3)