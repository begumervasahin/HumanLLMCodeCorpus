from CrapsSimulator import CrapsSimulator
def fonk1(b4):
    b1 = CrapsSimulator(numb_players=1, bet_type=2, roll_count_limit=100)
    b2 = [1000, 5000, 10000]
    for roll_count_limit in b2:
        print(f"----- Roll {roll_count_limit} times -----")
        profit_pdp, profit_pf, b3 = 0, 0, 0
        b1.reset_total_roll_count()
        b1.set_roll_count_limit(roll_count_limit)
        while b1.total_roll_count < roll_count_limit:
            if b4 = = 0:
                b5 = (0, 1000, 0)
                b6 = (1000, 0, 0)
                b7 = (0, 1000, 0)
            elif b4 = = 1:
                b5 = (493, 507, 0)
                b6 = (568, 0, 432)
                b7 = (0, 575, 425)
            elif b4 = = 2:
                b5 = (496, 504, 0)
                b6 = (550, 0, 450)
                b7 = (0, 554, 446)
            else:
                b5, b6, b7 = (), (), ()
            profit_pdp += b1.play(b8 = b5[0], dp=b5[1], f=b5[2])[0]
            profit_pf += b1.play(b8 = b6[0], dp=b6[1], f=b6[2])[0]
            b3 += b1.play(b8 = b7[0], dp=b7[1], f=b7[2])[0]
        print("Total Profit - Pass/Don't Pass:", profit_pdp)
        print("Total Profit - Pass + Field:", profit_pf)
        print("Total Profit - Don't Pass + Field:", b3)
def fonk2():
    for b4 in range(3):
        fonk1(b4)
if b9 = = "__main__":
    fonk2()