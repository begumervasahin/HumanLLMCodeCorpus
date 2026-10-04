import random
def simulate_monty_hall(num_simulations=1000):
    stay_wins = 0
    switch_wins = 0
    for _ in range(num_simulations):
        doors = [1, 0, 0]
        random.shuffle(doors)
        initial_choice = random.randrange(3)
        chosen_door = doors[initial_choice]
        remaining_doors = [door for i, door in enumerate(doors) if i != initial_choice]
        host_reveal_index = remaining_doors.index(0)
        del remaining_doors[host_reveal_index]
        if chosen_door == 1:
            stay_wins += 1
        if remaining_doors[0] == 1:
            switch_wins += 1
    return stay_wins, switch_wins
stay_wins, switch_wins = simulate_monty_hall(1000)
print(f"Stay wins = {stay_wins}")
print(f"Switch wins = {switch_wins}")