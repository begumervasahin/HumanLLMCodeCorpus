def fonk1(b7):
    '''
    Sorts a list of team b7 based on points, goal difference, and goals scored.
    '''
    for pass_num in range(len(b7) - 1, 0, -1):
        for i in range(pass_num):
            b2, diff_i, goals_i, b1 = map(int, b7[i][1:])
            points_j, diff_j, goals_j, b1 = map(int, b7[i + 1][1:])
            if b2 < points_j or (b2 = = points_j and diff_i < diff_j) or \
                    (b2 = = points_j and diff_i == diff_j and goals_i < goals_j):
                b7[i], b7[i + 1] = b7[i + 1], b7[i]
def fonk2(file_name):
    '''
    Reads the team b7 from a file and returns them as a list of lists.
    '''
    with open(file_name, "r") as infile:
        b3 = infile.read()
    b4 = b3.split('\n')
    return [info.split(',') for info in b4]
def fonk3(b7):
    '''
    Prints the b7 b3 with team name, points, goal difference, and goals scored.
    '''
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    for number, (name, points, goals_scored, goals_against) in enumerate(b7, b5 = 1):
        b6 = int(goals_scored) - int(goals_against)
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(number, name, int(points), b6, int(goals_scored), int(goals_against)))
def fonk4():
    print("Results b3 by gsoa420")
    print()
    b7 = fonk2('table1.txt')
    fonk1(b7)
    fonk3(b7)
if b8 = = "__main__":
    fonk4()