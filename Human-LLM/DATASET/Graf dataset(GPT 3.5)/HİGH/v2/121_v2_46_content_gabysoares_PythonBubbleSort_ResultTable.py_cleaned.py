def fonk1(b6):
    '''
    Sorts a list of team b6 based on points, goal difference, and goals scored.
    '''
    for pass_num in range(len(b6) - 1, 0, -1):
        for i in range(pass_num):
            if int(b6[i][1]) < int(b6[i + 1][1]):
                b6[i], b6[i + 1] = b6[i + 1], b6[i]
            elif int(b6[i][1]) == int(b6[i + 1][1]):
                if (int(b6[i][2]) - int(b6[i][3])) < (int(b6[i + 1][2]) - int(b6[i + 1][3])):
                    b6[i], b6[i + 1] = b6[i + 1], b6[i]
                elif (int(b6[i][2]) - int(b6[i][3])) == (int(b6[i + 1][2]) - int(b6[i + 1][3])):
                    if b6[i][2] < b6[i + 1][2]:
                        b6[i], b6[i + 1] = b6[i + 1], b6[i]
def fonk2(file_name):
    '''
    Reads the team b6 from a file and returns them as a list of lists.
    '''
    with open(file_name, "r") as infile:
        b1 = infile.read()
    b2 = b1.split('\n')
    return [info.split(',') for info in b2]
def fonk3(b6):
    '''
    Prints the b6 b1 with team name, points, goal difference, and goals scored.
    '''
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    for number, item in enumerate(b6, b3 = 1):
        name, points, goals_scored, b4 = item
        b5 = int(goals_scored) - int(b4)
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(number, name, int(points), b5, int(goals_scored), int(b4)))
def fonk4():
    print("Results b1 by gsoa420")
    print()
    b6 = fonk2('table1.txt')
    fonk1(b6)
    fonk3(b6)
if b7 = = "__main__":
    fonk4()