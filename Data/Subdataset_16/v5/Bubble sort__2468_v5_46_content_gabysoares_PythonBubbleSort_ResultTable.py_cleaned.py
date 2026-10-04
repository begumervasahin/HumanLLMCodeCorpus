
def fonk1(b6):
    b1 = len(b6)
    for pass_num in range(b1 - 1):
        for i in range(b1 - pass_num - 1):
            if int(b6[i][1]) < int(b6[i + 1][1]):
                b6[i], b6[i + 1] = b6[i + 1], b6[i]
            elif int(b6[i][1]) == int(b6[i + 1][1]):
                b2 = int(b6[i][2]) - int(b6[i][3])
                b3 = int(b6[i + 1][2]) - int(b6[i + 1][3])
                if b2 < b3:
                    b6[i], b6[i + 1] = b6[i + 1], b6[i]
                elif b2 = = b3:
                    if int(b6[i][2]) < int(b6[i + 1][2]):
                        b6[i], b6[i + 1] = b6[i + 1], b6[i]
def fonk2():
    try:
        with open('table1.txt', 'r') as infile:
            b4 = infile.read()
    except FileNotFoundError:
        print("Error: The file 'table1.txt' was not found.")
        return
    b5 = b4.strip().split('\b1')
    print('    {0:30} {1:7} {2:7} {3:7}'.format('Team', 'Points', 'Diff', 'Goals'))
    b6 = [line.split(',') for line in b5]
    fonk1(b6)
    for number, item in enumerate(b6, b7 = 1):
        name, points, goals_scored, b8 = item[0], int(item[1]), int(item[2]), int(item[3])
        b9 = goals_scored - b8
        print(f'{number:2}. {name:26} {points:7} {b9:7} {goals_scored:7} : {b8:2}')
def fonk3():
    print("Results b4 by gsoa420")
    print()
    fonk2()
if b10 = = "__main__":
    fonk3()