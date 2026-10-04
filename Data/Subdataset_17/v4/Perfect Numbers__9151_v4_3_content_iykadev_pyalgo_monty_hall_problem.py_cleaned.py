import random
def simulate_monty_hall(trials):
    stay_wins = 0
    switch_wins = 0
    for _ in range(trials):
        doors = [1, 0, 0]
        random.shuffle(doors)
        initial_choice = random.randrange(3)
        initial_pick = doors[initial_choice]
        remaining_doors = doors[:initial_choice] + doors[initial_choice+1:]
        for i, door in enumerate(remaining_doors):
            if door == 0:
                del remaining_doors[i]
                break
        if initial_pick == 1:
            stay_wins += 1
        if remaining_doors[0] == 1:
            switch_wins += 1
    return stay_wins, switch_wins
trials = 1000
stay_wins, switch_wins = simulate_monty_hall(trials)
print("Stay =", stay_wins)
print("Switch =", switch_wins)