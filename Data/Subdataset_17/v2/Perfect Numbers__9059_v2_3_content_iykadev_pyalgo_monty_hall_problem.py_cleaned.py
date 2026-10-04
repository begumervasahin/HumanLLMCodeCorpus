import random
stay_wins = 0
switch_wins = 0
for _ in range(1000):
    doors = [1, 0, 0]
    random.shuffle(doors)
    initial_choice = random.randrange(3)
    chosen_door = doors[initial_choice]
    remaining_doors = doors[:initial_choice] + doors[initial_choice + 1:]
    for i in range(len(remaining_doors)):
        if remaining_doors[i] == 0:
            del remaining_doors[i]
            break
    if chosen_door == 1:
        stay_wins += 1
    if remaining_doors[0] == 1:
        switch_wins += 1
print("Stay wins =", stay_wins)
print("Switch wins =", switch_wins)