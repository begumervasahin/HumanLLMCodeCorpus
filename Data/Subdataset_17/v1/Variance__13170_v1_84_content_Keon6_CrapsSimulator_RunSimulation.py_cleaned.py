from CrapsSimulator import CrapsSimulator
def run_simulation_for_roll_counts(c):
    simulation = CrapsSimulator(numb_players=1, bet_type=2, roll_count_limit=100)
    roll_count_limits = [1000, 5000, 10000]
    for roll_count_limit in roll_count_limits:
        print(f"----- Roll {roll_count_limit} times -----")
        profit_pdp, profit_pf, profit_dpf = 0, 0, 0
        simulation.reset_total_roll_count()
        simulation.set_roll_count_limit(roll_count_limit)
        while simulation.total_roll_count < roll_count_limit:
            if c == 0:
                pdp = (0, 1000, 0)
                pf = (1000, 0, 0)
                dpf = (0, 1000, 0)
            elif c == 1:
                pdp = (493, 507, 0)
                pf = (568, 0, 432)
                dpf = (0, 575, 425)
            elif c == 2:
                pdp = (496, 504, 0)
                pf = (550, 0, 450)
                dpf = (0, 554, 446)
            else:
                pdp, pf, dpf = (), (), ()
            profit_pdp += simulation.play(p=pdp[0], dp=pdp[1], f=pdp[2])[0]
            profit_pf += simulation.play(p=pf[0], dp=pf[1], f=pf[2])[0]
            profit_dpf += simulation.play(p=dpf[0], dp=dpf[1], f=dpf[2])[0]
        print("Total Profit - Pass/Don't Pass", profit_pdp)
        print("Total Profit - Pass + Field", profit_pf)
        print("Total Profit - Don't Pass + Field", profit_dpf)
def main():
    for c in range(3):
        run_simulation_for_roll_counts(c)
if __name__ == "__main__":
    main()