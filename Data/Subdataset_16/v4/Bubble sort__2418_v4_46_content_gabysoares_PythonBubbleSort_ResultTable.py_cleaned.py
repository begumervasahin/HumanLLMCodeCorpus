
def fonk1(b5):
    for pass_num in range(len(b5) - 1, 0, -1):
        for i in range(pass_num):
            if int(b5[i][1]) < int(b5[i + 1][1]):
                b5[i], b5[i + 1] = b5[i + 1], b5[i]
            elif b5[i][1] == b5[i + 1][1]:
                b1 = int(b5[i][2]) - int(b5[i][3])
                b2 = int(b5[i + 1][2]) - int(b5[i + 1][3])
                if b1 < b2:
                    b5[i], b5[i + 1] = b5[i + 1], b5[i]
                elif b1 = = b2:
                    if int(b5[i][2]) < int(b5[i + 1][2]):
                        b5[i], b5[i + 1] = b5[i + 1], b5[i]
def fonk2():
    try:
        with open('table1.txt', 'r') as infile:
            b3 = infile.read()
    except FileNotFoundError:
        print("Error: The file 'table1.txt' was not found.")
        return
    b4 = b3.strip().split('\n')
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    b5 = []
    for line in b4:
        b5.append(line.split(','))
    fonk1(b5)
    for number, item in enumerate(b5, b6 = 1):
        name, points, goals_scored, b7 = item[0], int(item[1]), int(item[2]), int(item[3])
        b8 = goals_scored - b7
        print(f'{number:2}. {name:26}  {points:7}  {b8:5}  {goals_scored:5} : {b7:2}')
def fonk3():
    print("Results b3 by gsoa420")
    print()
    fonk2()
if b9 = = "__main__":
    fonk3()