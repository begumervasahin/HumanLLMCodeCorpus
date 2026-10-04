
def fonk1(b3):
    for pass_num in range(len(b3) - 1, 0, -1):
        for i in range(pass_num):
            if int(b3[i][1]) < int(b3[i + 1][1]):
                b3[i], b3[i + 1] = b3[i + 1], b3[i]
            elif int(b3[i][1]) == int(b3[i + 1][1]):
                if (int(b3[i][2]) - int(b3[i][3])) < (int(b3[i + 1][2]) - int(b3[i + 1][3])):
                    b3[i], b3[i + 1] = b3[i + 1], b3[i]
                elif (int(b3[i][2]) - int(b3[i][3])) == (int(b3[i + 1][2]) - int(b3[i + 1][3])):
                    if int(b3[i][2]) < int(b3[i + 1][2]):
                        b3[i], b3[i + 1] = b3[i + 1], b3[i]
def fonk2():
    try:
        with open('table1.txt', "r") as infile:
            b1 = infile.read()
    except FileNotFoundError:
        print("Error: 'table1.txt' file not found.")
        return
    b2 = b1.strip().split('\n')
    print('    {0:30} {1:7} {2:5} {3:7}'.format('Team', 'Points', 'Diff', 'Goals'))
    b3 = [line.split(',') for line in b2]
    fonk1(b3)
    for number, item in enumerate(b3, b4 = 1):
        b5 = item[0]
        b6 = item[1]
        b7 = item[2]
        b8 = item[3]
        b9 = int(b7) - int(b8)
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(number, b5, b6, b9, b7, b8))
def fonk3():
    print("Results b1 by gsoa420")
    print()
    fonk2()
if b10 = = "__main__":
    fonk3()