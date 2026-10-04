from CrapsSimulator import CrapsSimulator
def get_betting_strategy(c):
    if c == 0:
        return (0, 1000, 0), (1000, 0, 0), (0, 1000, 0)
    elif c == 1:
        return (493, 507, 0), (568, 0, 432), (0, 575, 425)
    elif c == 2:
        return (496, 504, 0), (550, 0, 450), (0, 554, 446)
    else:
        return (), (), ()
def simulate_betting_strategy(simulation, roll_count_limit, strategy):
    profit = 0
    simulation.reset_total_roll_count()
    simulation.set_roll_count_limit(roll_count_limit)
    while simulation.total_roll_count < roll_count_limit:
        profit += simulation.play(p=strategy[0], dp=strategy[1], f=strategy[2])[0]
    return profit
def run_simulation_for_roll_counts(c):
    simulation = CrapsSimulator(numb_players=1, bet_type=2, roll_count_limit=100)
    roll_count_limits = [1000, 5000, 10000]
    for roll_count_limit in roll_count_limits:
        print(f"----- Roll {roll_count_limit} times -----")
        pdp_strategy, pf_strategy, dpf_strategy = get_betting_strategy(c)
        profit_pdp = simulate_betting_strategy(simulation, roll_count_limit, pdp_strategy)
        profit_pf = simulate_betting_strategy(simulation, roll_count_limit, pf_strategy)
        profit_dpf = simulate_betting_strategy(simulation, roll_count_limit, dpf_strategy)
        print(f"Total Profit - Pass/Don't Pass: {profit_pdp}")
        print(f"Total Profit - Pass + Field: {profit_pf}")
        print(f"Total Profit - Don't Pass + Field: {profit_dpf}")
def main():
    for c in range(3):
        run_simulation_for_roll_counts(c)
if __name__ == "__main__":
    main()