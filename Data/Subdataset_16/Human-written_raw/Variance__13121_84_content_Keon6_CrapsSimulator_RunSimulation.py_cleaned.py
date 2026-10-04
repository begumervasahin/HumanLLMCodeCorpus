from CrapsSimulator import CrapsSimulator
def fonk1(b3):
    b1 = CrapsSimulator(numb_players=1, bet_type=2, roll_count_limit=100)
    b2 = [1000, 5000, 10000]
    print(f"
    for roll_count_limit in b2:
        print(f"----- Roll {roll_count_limit} times -----")
        a1 = 0
        a2 = 0
        a3 = 0
        b1.reset_total_roll_count()
        b1.set_roll_count_limit(roll_count_limit)
        while b1.total_roll_count < roll_count_limit:
            if b3 = = 0:
                b4 = (0, 1000, 0)
                b5 = (1000, 0, 0)
                b6 = (0, 1000, 0)
            elif b3 = = 1:
                b4 = (493, 507, 0)
                b5 = (568, 0, 432)
                b6 = (0, 575, 425)
            elif b3 = = 2:
                b4 = (496, 504, 0)
                b5 = (550, 0, 450)
                b6 = (0, 554, 446)
            else:
                b4 = ()
                b5 = ()
                b6 = ()
            a1 += b1.play(b7 = b4[0], dp=b4[1], f=b4[2])[0]
            a2 += b1.play(b7 = b5[0], dp=b5[1], f=b5[2])[0]
            a3 += b1.play(b7 = b6[0], dp=b6[1], f=b6[2])[0]
        print("Total Profit - Pass/Don't Pass", a1)
        print("Total Profit - Pass + Field", a2)
        print("Total Profit - Don't Pass + Field", a3)
def fonk2():
    for b3 in range(3):
        print(fonk1(b3))
fonk2()