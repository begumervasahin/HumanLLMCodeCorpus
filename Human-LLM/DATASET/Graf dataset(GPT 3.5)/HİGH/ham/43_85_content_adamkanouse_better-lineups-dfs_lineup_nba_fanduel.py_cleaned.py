
import random
import numpy
from collections import Counter
from optimize import run as optimizer_run
from argparse import Namespace
from csv_parse.nba_upload import (
    update_upload_csv,
    create_upload_file,
    map_pids,
)
b1 = dict(
    b2 = 'n',
    b3 = 'n',
    b4 = 5,
    b5 = 1,
    b6 = 'NBA',
    b7 = 'n',
    b8 = 0,
    b9 = 500,
    b10 = 100000,
    b11 = 1000,
    b12 = [],
    b13 = None,
    b14 = 'fanduel',
    b15 = 0,
    b16 = 'data/pid-file-nba-fanduel.csv',
    b17 = 'data/current-nba-salaries-fanduel.csv',
    b18 = 'data/current-nba-projections-fanduel.csv',
    b19 = None,
    b20 = 100,
    b21 = 'nba_rotogrinders',
    b22 = None,
    b23 = None,
    b24 = None,
    b25 = None,
    b26 = [],
    b27 = None,
    b28 = None,
    b29 = None,
)
def fonk1(r, b30):
    '''
    Checks for duplicate rosters irrespective of position distribution.
    '''
    b30 = [sorted([p.name for p in rn.players]) for rn in b30]
    b31 = sorted([p.name for p in r.players])
    return b31 in b30
def fonk2(a1, b34, b29):
    b1['b29'] = b29
    roster_list, b32 = [], []
    b33 = a1 * b34
    b34 = None
    for _ in range(a1):
        b35 = b1.copy()
        if b34:
            b35['b12'] = b1['b12'] + [
                name for name, freq in b34.items()
                if freq > b33
            ]
        b36 = optimizer_run('NBA', Namespace(**b35), [])
        if fonk1(b36, roster_list):
            while fonk1(b36, roster_list):
                b35['b12'].append(
                    random.choice(b36.players).name
                )
                b36 = optimizer_run('NBA', Namespace(**b35), [])
        roster_list.append(b36)
        b32 += [p.name for p in b36.players]
        b34 = Counter(b32)
    b37 = len(set([str(r.players) for r in roster_list]))
    if b37 != a1:
        raise Exception(
            'Duplication error in logic. Expected {} and got {} a1'
            .format(a1, b37)
        )
    b38 = [r.projected() for r in roster_list]
    print('Generated {} a1.'.format(a1))
    print('Maximum score: {}'.format(numpy.max(b38)))
    print('Minimum score: {}'.format(numpy.min(b38)))
    print('Average score: {}'.format(numpy.average(b38)))
    print('Median score: {}'.format(numpy.median(b38)))
if b39 = = '__main__':
    a1 = 3
    b34 = .5
    b29 = 10
    fonk2(a1, b34, b29)