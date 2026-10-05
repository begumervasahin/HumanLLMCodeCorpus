from constantes import *
import random as r
def update_win_history(player_grid, official_draw, win_history, gains):
    correct_numbers = count_correct_numbers(player_grid, official_draw)
    bonus_number_matched = player_grid[NB_BOULES_NORMALES] == official_draw[NB_BOULES_NORMALES]
    if correct_numbers == 5 and bonus_number_matched:
        win_history[0][1] += 1
        gains += win_history[0][0]
    elif correct_numbers == 5:
        win_history[1][1] += 1
        gains += win_history[1][0]
    elif correct_numbers == 4 and bonus_number_matched:
        win_history[2][1] += 1
        gains += win_history[2][0]
    elif correct_numbers == 4:
        win_history[3][1] += 1
        gains += win_history[3][0]
    elif correct_numbers == 3 and bonus_number_matched:
        win_history[4][1] += 1
        gains += win_history[4][0]
    elif correct_numbers == 3:
        win_history[5][1] += 1
        gains += win_history[5][0]
    elif correct_numbers == 2 and bonus_number_matched:
        win_history[6][1] += 1
        gains += win_history[6][0]
    elif correct_numbers == 2:
        win_history[7][1] += 1
        gains += win_history[7][0]
    elif correct_numbers == 1 and bonus_number_matched:
        win_history[8][1] += 1
        gains += win_history[8][0]
    elif bonus_number_matched:
        win_history[8][1] += 1
        gains += win_history[8][0]
    return win_history, gains
def count_correct_numbers(player_grid, official_draw):
    correct_numbers = 0
    for g in range(NB_BOULES_NORMALES):
        for t in range(NB_BOULES_NORMALES):
            if player_grid[g] == official_draw[t]:
                correct_numbers += 1
    return correct_numbers
def create_win_history():
    return [
        [JACKPOT, 0],
        [100000, 0],
        [1000, 0],
        [500, 0],
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [MISE, 0],
    ]
def update_ball_history(official_draw, ball_history):
    for i in range(NB_BOULES_NORMALES):
        ball_history[0][official_draw[i] - 1][1] += 1
    ball_history[1][official_draw[NB_BOULES_NORMALES] - 1][1] += 1
    return ball_history
def create_ball_history():
    return [
        [[i, 0] for i in range(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL + 1)],
        [[i, 0] for i in range(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP + 1)]
    ]
def sort_ball_history(ball_history):
    sorted_ball_history = [
        sorted(ball_history[0], key=lambda x: x[1], reverse=True),
        sorted(ball_history[1], key=lambda x: x[1], reverse=True)
    ]
    return sorted_ball_history
def create_hot_cold_grids(sorted_ball_history):
    hot_grid = [item[0] for item in sorted_ball_history[0][:NB_BOULES_NORMALES]]
    hot_grid.append(sorted_ball_history[1][0][0])
    cold_grid = [item[0] for item in sorted_ball_history[0][-NB_BOULES_NORMALES:][::-1]]
    cold_grid.append(sorted_ball_history[1][-1][0])
    return hot_grid, cold_grid
def create_random_grid():
    random_grid = []
    while len(random_grid) < NB_BOULES_NORMALES:
        temp_number = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        if temp_number not in random_grid:
            random_grid.append(temp_number)
    random_grid.append(r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP))
    return random_grid