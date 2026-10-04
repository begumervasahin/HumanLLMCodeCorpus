
def bubble_sort(results):
    for pass_num in range(len(results) - 1, 0, -1):
        for i in range(pass_num):
            current_team, next_team = results[i], results[i + 1]
            current_points, next_points = int(current_team[1]), int(next_team[1])
            current_goal_diff = int(current_team[2]) - int(current_team[3])
            next_goal_diff = int(next_team[2]) - int(next_team[3])
            current_goals_scored, next_goals_scored = int(current_team[2]), int(next_team[2])
            if current_points < next_points or \
               (current_points == next_points and current_goal_diff < next_goal_diff) or \
               (current_points == next_points and current_goal_diff == next_goal_diff and current_goals_scored < next_goals_scored):
                results[i], results[i + 1] = results[i + 1], results[i]
def result_table():
    try:
        with open('table1.txt', "r") as infile:
            table = infile.read()
    except FileNotFoundError:
        print("Error: 'table1.txt' file not found.")
        return
    table_list = table.strip().split('\n')
    results = [line.split(',') for line in table_list]
    bubble_sort(results)
    print('{:<2} {:<30} {:<7} {:<5} {:<7}'.format('', 'Team', 'Points', 'Diff', 'Goals'))
    for number, item in enumerate(results, start=1):
        name, points, goals_scored, goals_against = item[0], item[1], item[2], item[3]
        diff_goals = int(goals_scored) - int(goals_against)
        print('{:<2} {:<30} {:<7} {:<5} {:<7} : {:<2}'.format(
            f"{number}.", name, points, diff_goals, goals_scored, goals_against))
def main():
    print("Results table by gsoa420\n")
    result_table()
if __name__ == "__main__":
    main()