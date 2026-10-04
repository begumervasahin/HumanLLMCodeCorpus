from CrapsSimulator import CrapsSimulator
def fonk1(c):
    b1 = CrapsSimulator(numb_players=1, bet_type=2, roll_count_limit=100)
    b2 = [1000, 5000, 10000]
    b3 = [
        {'pdp': (0, 1000, 0), 'pf': (1000, 0, 0), 'dpf': (0, 1000, 0)},
        {'pdp': (493, 507, 0), 'pf': (568, 0, 432), 'dpf': (0, 575, 425)},
        {'pdp': (496, 504, 0), 'pf': (550, 0, 450), 'dpf': (0, 554, 446)}
    ]
    for roll_count_limit in b2:
        print(f"----- Roll {roll_count_limit} times -----")
        profit_pdp, profit_pf, b4 = 0, 0, 0
        b1.reset_total_roll_count()
        b1.set_roll_count_limit(roll_count_limit)
        b5 = b3[c] if c in range(3) else {'pdp': (), 'pf': (), 'dpf': ()}
        while b1.total_roll_count < roll_count_limit:
            profit_pdp += b1.play(b6 = b5['pdp'][0], dp=b5['pdp'][1], f=b5['pdp'][2])[0]
            profit_pf += b1.play(b6 = b5['pf'][0], dp=b5['pf'][1], f=b5['pf'][2])[0]
            b4 += b1.play(b6 = b5['dpf'][0], dp=b5['dpf'][1], f=b5['dpf'][2])[0]
        print("Total Profit - Pass/Don't Pass:", profit_pdp)
        print("Total Profit - Pass + Field:", profit_pf)
        print("Total Profit - Don't Pass + Field:", b4)
def fonk2():
    for c in range(3):
        fonk1(c)
if b7 = = "__main__":
    fonk2()