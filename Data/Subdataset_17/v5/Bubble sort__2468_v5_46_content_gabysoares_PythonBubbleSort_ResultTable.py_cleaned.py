
def bubble_sort(results):
    n = len(results)
    for pass_num in range(n - 1):
        for i in range(n - pass_num - 1):
            if int(results[i][1]) < int(results[i + 1][1]):
                results[i], results[i + 1] = results[i + 1], results[i]
            elif int(results[i][1]) == int(results[i + 1][1]):
                goal_diff_i = int(results[i][2]) - int(results[i][3])
                goal_diff_next = int(results[i + 1][2]) - int(results[i + 1][3])
                if goal_diff_i < goal_diff_next:
                    results[i], results[i + 1] = results[i + 1], results[i]
                elif goal_diff_i == goal_diff_next:
                    if int(results[i][2]) < int(results[i + 1][2]):
                        results[i], results[i + 1] = results[i + 1], results[i]
def result_table():
    try:
        with open('table1.txt', 'r') as infile:
            table = infile.read()
    except FileNotFoundError:
        print("Error: The file 'table1.txt' was not found.")
        return
    table_list = table.strip().split('\n')
    print('    {0:30} {1:7} {2:7} {3:7}'.format('Team', 'Points', 'Diff', 'Goals'))
    results = [line.split(',') for line in table_list]
    bubble_sort(results)
    for number, item in enumerate(results, start=1):
        name, points, goals_scored, goals_against = item[0], int(item[1]), int(item[2]), int(item[3])
        goal_diff = goals_scored - goals_against
        print(f'{number:2}. {name:26} {points:7} {goal_diff:7} {goals_scored:7} : {goals_against:2}')
def main():
    print("Results table by gsoa420")
    print()
    result_table()
if __name__ == "__main__":
    main()