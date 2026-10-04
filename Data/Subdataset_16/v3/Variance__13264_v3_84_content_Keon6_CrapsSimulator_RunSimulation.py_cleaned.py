from CrapsSimulator import CrapsSimulator
def fonk1(b1):
    if b1 = = 0:
        return (0, 1000, 0), (1000, 0, 0), (0, 1000, 0)
    elif b1 = = 1:
        return (493, 507, 0), (568, 0, 432), (0, 575, 425)
    elif b1 = = 2:
        return (496, 504, 0), (550, 0, 450), (0, 554, 446)
    else:
        return (), (), ()
def fonk2(b3, roll_count_limit, strategy):
    a1 = 0
    b3.reset_total_roll_count()
    b3.set_roll_count_limit(roll_count_limit)
    while b3.total_roll_count < roll_count_limit:
        a1 += b3.play(b2 = strategy[0], dp=strategy[1], f=strategy[2])[0]
    return a1
def fonk3(b1):
    b3 = CrapsSimulator(numb_players=1, bet_type=2, roll_count_limit=100)
    b4 = [1000, 5000, 10000]
    for roll_count_limit in b4:
        print(f"----- Roll {roll_count_limit} times -----")
        pdp_strategy, pf_strategy, b5 = fonk1(b1)
        b6 = fonk2(b3, roll_count_limit, pdp_strategy)
        b7 = fonk2(b3, roll_count_limit, pf_strategy)
        b8 = fonk2(b3, roll_count_limit, b5)
        print(f"Total Profit - Pass/Don't Pass: {b6}")
        print(f"Total Profit - Pass + Field: {b7}")
        print(f"Total Profit - Don't Pass + Field: {b8}")
def fonk4():
    for b1 in range(3):
        fonk3(b1)
if b9 = = "__main__":
    fonk4()