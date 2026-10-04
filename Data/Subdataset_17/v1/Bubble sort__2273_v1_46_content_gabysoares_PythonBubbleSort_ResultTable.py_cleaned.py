
def bubble_sort(results):
    for pass_num in range(len(results) - 1, 0, -1):
        for i in range(pass_num):
            if int(results[i][1]) < int(results[i + 1][1]):
                results[i], results[i + 1] = results[i + 1], results[i]
            elif int(results[i][1]) == int(results[i + 1][1]):
                if (int(results[i][2]) - int(results[i][3])) < (int(results[i + 1][2]) - int(results[i + 1][3])):
                    results[i], results[i + 1] = results[i + 1], results[i]
                elif (int(results[i][2]) - int(results[i][3])) == (int(results[i + 1][2]) - int(results[i + 1][3])):
                    if int(results[i][2]) < int(results[i + 1][2]):
                        results[i], results[i + 1] = results[i + 1], results[i]
def result_table():
    try:
        with open('table1.txt', "r") as infile:
            table = infile.read()
    except FileNotFoundError:
        print("Error: 'table1.txt' file not found.")
        return
    table_list = table.strip().split('\n')
    print('    {0:30} {1:7} {2:5} {3:7}'.format('Team', 'Points', 'Diff', 'Goals'))
    results = [line.split(',') for line in table_list]
    bubble_sort(results)
    for number, item in enumerate(results, start=1):
        name = item[0]
        points = item[1]
        goals_scored = item[2]
        goals_against = item[3]
        diff_goals = int(goals_scored) - int(goals_against)
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(number, name, points, diff_goals, goals_scored, goals_against))
def main():
    print("Results table by gsoa420")
    print()
    result_table()
if __name__ == "__main__":
    main()