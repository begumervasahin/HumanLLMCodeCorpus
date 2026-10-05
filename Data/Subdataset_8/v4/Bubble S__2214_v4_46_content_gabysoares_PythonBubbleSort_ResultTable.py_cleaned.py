def bubble_sort(results):
    for pass_num in range(len(results) - 1, 0, -1):
        for i in range(0, pass_num):
            if int(results[i][1]) < int(results[i + 1][1]):
                results[i], results[i + 1] = results[i + 1], results[i]
            if results[i][1] == results[i + 1][1]:
                if (int(results[i][2]) - int(results[i][3])) < (int(results[i + 1][2]) - int(results[i + 1][3])):
                    results[i], results[i + 1] = results[i + 1], results[i]
            if (results[i][1] == results[i + 1][1]) and (int(results[i][2]) - int(results[i][3])) == (int(results[i + 1][2]) - int(results[i + 1][3])):
                if results[i][2] < results[i + 1][2]:
                    results[i], results[i + 1] = results[i + 1], results[i]
def read_table(filename):
    with open(filename, "r") as infile:
        table = infile.readlines()
    table_list = [line.strip().split(',') for line in table]
    return table_list
def display_results(results):
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    number = 0
    for item in results:
        name = item[0]
        points = int(item[1])
        goals_scored = int(item[2])
        goals_against = int(item[3])
        diff_goals = goals_scored - goals_against
        number += 1
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(number, name, points, diff_goals, goals_scored, goals_against))
def main():
    print("Results table by gsoa420")
    print()
    results = read_table('table1.txt')
    bubble_sort(results)
    display_results(results)
if __name__ == "__main__":
    main()