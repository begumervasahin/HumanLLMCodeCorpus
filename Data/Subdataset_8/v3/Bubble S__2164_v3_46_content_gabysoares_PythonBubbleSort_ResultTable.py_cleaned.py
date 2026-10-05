def bubble_sort_results(results):
    '''
    Sorts a list of team results based on points, goal difference, and goals scored.
    '''
    for pass_num in range(len(results) - 1, 0, -1):
        for i in range(pass_num):
            points_i, diff_i, goals_i, _ = map(int, results[i][1:])
            points_j, diff_j, goals_j, _ = map(int, results[i + 1][1:])
            if points_i < points_j or (points_i == points_j and diff_i < diff_j) or \
                    (points_i == points_j and diff_i == diff_j and goals_i < goals_j):
                results[i], results[i + 1] = results[i + 1], results[i]
def read_table_from_file(file_name):
    '''
    Reads the team results from a file and returns them as a list of lists.
    '''
    with open(file_name, "r") as infile:
        table = infile.read()
    table_list = table.split('\n')
    return [info.split(',') for info in table_list]
def display_results_table(results):
    '''
    Prints the results table with team name, points, goal difference, and goals scored.
    '''
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    for number, (name, points, goals_scored, goals_against) in enumerate(results, start=1):
        diff_goals = int(goals_scored) - int(goals_against)
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(number, name, int(points), diff_goals, int(goals_scored), int(goals_against)))
def main():
    print("Results table by gsoa420")
    print()
    results = read_table_from_file('table1.txt')
    bubble_sort_results(results)
    display_results_table(results)
if __name__ == "__main__":
    main()