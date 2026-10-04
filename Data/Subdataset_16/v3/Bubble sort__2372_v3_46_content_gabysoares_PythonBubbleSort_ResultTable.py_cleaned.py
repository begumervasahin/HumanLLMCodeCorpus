
def fonk1(b9):
    for pass_num in range(len(b9) - 1, 0, -1):
        for i in range(pass_num):
            current_team, b1 = b9[i], b9[i + 1]
            b6, b2 = int(current_team[1]), int(b1[1])
            b3 = int(current_team[2]) - int(current_team[3])
            b4 = int(b1[2]) - int(b1[3])
            current_goals_scored, b5 = int(current_team[2]), int(b1[2])
            if b6 < b2 or \
               (b6 = = b2 and b3 < b4) or \
               (b6 = = b2 and b3 == b4 and current_goals_scored < b5):
                b9[i], b9[i + 1] = b9[i + 1], b9[i]
def fonk2():
    try:
        with open('table1.txt', "r") as infile:
            b7 = infile.read()
    except FileNotFoundError:
        print("Error: 'table1.txt' file not found.")
        return
    b8 = b7.strip().split('\n')
    b9 = [line.split(',') for line in b8]
    fonk1(b9)
    print('{:<2} {:<30} {:<7} {:<5} {:<7}'.format('', 'Team', 'Points', 'Diff', 'Goals'))
    for number, item in enumerate(b9, b10 = 1):
        name, points, goals_scored, b11 = item[0], item[1], item[2], item[3]
        b12 = int(goals_scored) - int(b11)
        print('{:<2} {:<30} {:<7} {:<5} {:<7} : {:<2}'.format(
            f"{number}.", name, points, b12, goals_scored, b11))
def fonk3():
    print("Results b7 by gsoa420\n")
    fonk2()
if b13 = = "__main__":
    fonk3()