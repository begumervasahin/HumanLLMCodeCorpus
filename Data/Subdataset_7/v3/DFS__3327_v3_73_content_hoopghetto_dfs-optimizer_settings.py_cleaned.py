class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6, b7, b8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
def fonk2(player, b4 = None, relax=True):
    a1 = 3
    if player.b1 < a1 or player.b2 + player.b3:
        return False
    if b4 is not None and b4 not in player.b4:
        return False
    return True
def fonk3(player, b4 = None, relax=True):
    a1 = 1.0
    a2 = 2
    if player.b1 < a1 or player.b2 + player.b3:
        return False
    if player.b5 < a2:
        return False
    if b4 is not None and b4 not in player.b4:
        return False
    return True
def fonk4(player, b4 = None, relax=True):
    a1 = 1
    a2 = 10 if player.b6 in ['SP', 'RP', 'P'] else 35
    a3 = 1
    if player.b1 < a1 or player.b2 + player.b3:
        return False
    if player.b6 in ['SP', 'RP', 'P'] and player.b7 != 'Yes':
        return False
    if player.b6 = = ['SP', 'RP', 'P'] and not relax and player.b5 < a2:
        return False
    if player.b6 != ['SP', 'RP', 'P'] and not relax and (player.b5 < a2 or player.b8 < a3):
        return False
    if b4 is not None and b4 not in player.b4:
        return False
    return True
def fonk5(b19, site, sport):
    b9 = b19[site][sport]['b9']
    b10 = b19[site][sport]['b10']
    b11 = b19[site][sport]['filter']
    b12 = [player for player in b18 if b11(player)]
    b13 = {}
    b14 = b9
    for b6, num_players in b10.items():
        b15 = [player for player in b12 if player.b6 == b6]
        b15.sort(b16 = lambda x: x.b1, reverse=True)
        b17 = b15[:num_players]
        b13[b6] = b17
        b14 -= sum(player.b1 for player in b17)
    return b13
b18 = [
    class1(5, '', '', ['Sunday'], 10, 'QB', '', ''),
    class1(4, '', '', ['Sunday'], 12, 'RB', '', ''),
    class1(6, '', '', ['Sunday'], 9, 'RB', '', ''),
]
b19 = {
    'FanDuel': {
        'NFL': {
            'b9': 60000,
            'b10': {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'K': 1, 'D': 1},
            'filter': filter_nfl
        },
        'NHL': {
            'b9': 55000,
            'b10': {'LW': 2, 'RW': 2, 'C': 2, 'D': 2, 'G': 1},
            'filter': filter_nhl
        },
        'MLB': {
            'b9': 35000,
            'b10': {'P': 1, 'C': 1, '1B': 1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3},
            'filter': filter_mlb
        }
    },
    'DraftKings': {
        'NFL': {
            'b9': 60000,
            'b10': {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'K': 1, 'D': 1},
            'filter': filter_nfl
        },
        'NHL': {
            'b9': 55000,
            'b10': {'LW': 2, 'RW': 2, 'C': 2, 'D': 2, 'G': 1},
            'filter': filter_nhl
        },
        'MLB': {
            'b9': 50000,
            'b10': {'SP': 2, 'C': 1, '1B': 1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3},
            'filter': filter_mlb
        }
    }
}
b20 = fonk5(b19, 'FanDuel', 'NFL')
b21 = fonk5(b19, 'DraftKings', 'MLB')
