def fonk1(p, b1 = None, relax=True):
    if p.fppg < 3 or p.injury_indicator + p.injury_details != '':
        return False
    if b1 is not None and b1 not in p.b1:
        return False
    return True
def fonk2(p, b1 = None, relax=True):
    if p.fppg < 1.0 or p.injury_indicator + p.injury_details != '':
        return False
    if p.played < 2:
        return False
    if b1 is not None and b1 not in p.b1:
        return False
    return True
def fonk3(p, b1 = None, relax=True):
    if p.fppg < 1 or p.injury_indicator + p.injury_details != '':
        return False
    if p.b2 in ['SP', 'RP', 'P'] and p.probable_pitcher != 'Yes':
        return False
    if p.b2 = = ['SP', 'RP', 'P'] and not relax and p.played < 10:
        return False
    if p.b2 != ['SP', 'RP', 'P'] and not relax and (p.played < 35 or p.batting_order in ['', 0]):
        return False
    if b1 is not None and b1 not in p.b1:
        return False
    return True
b3 = {
        'FanDuel': {'MLB': {'salary': 35000,
                       'composition': {'P':1, 'C':1, '1B':1, '2B':1, '3B':1, 'SS':1, 'OF':3},
                       'filter': filter_mlb
                      },
                    'NFL': {'salary': 60000,
                       'composition': {'QB': 1, 'RB': 2, 'WR': 3, 'TE':1, 'K':1, 'D':1},
                       'filter': filter_nfl
                      },
                     'NHL': {'salary': 55000,
                       'composition': {'LW': 2, 'RW': 2, 'C': 2, 'D': 2, 'G': 1},
                       'filter': filter_nhl
                      },
               },
        'DraftKings': {'MLB': {'salary': 50000,
                         'composition': {'SP':2, 'C':1, '1B':1, '2B':1, '3B':1, 'SS':1, 'OF':3},
                         'filter': filter_mlb
                      },
                       'NFL': {'salary': 60000,
                         'composition': {'QB': 1, 'RB': 2, 'WR': 3, 'TE':1, 'K':1, 'D':1},
                         'filter': filter_nfl
                      },
                       'NHL': {'salary': 55000,
                         'composition': {'LW': 2, 'RW': 2, 'C': 2, 'D': 2, 'G': 1},
                         'filter': filter_nhl
                      },
               }
         }