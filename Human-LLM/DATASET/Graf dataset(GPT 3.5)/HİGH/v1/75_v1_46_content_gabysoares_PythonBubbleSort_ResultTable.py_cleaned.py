def fonk1(b4):
    for pass_num in range(len(b4) - 1, 0, -1):
        for i in range(0, pass_num):
            if int(b4[i][1]) < int(b4[i + 1][1]):
                b4[i], b4[i + 1] = b4[i + 1], b4[i]
            if b4[i][1] == b4[i + 1][1]:
                if (int(b4[i][2]) - int(b4[i][3])) < (int(b4[i + 1][2]) - int(b4[i + 1][3])):
                    b4[i], b4[i + 1] = b4[i + 1], b4[i]
            if (b4[i][1] == b4[i + 1][1]) and (int(b4[i][2]) - int(b4[i][3])) == (int(b4[i + 1][2]) - int(b4[i + 1][3])):
                if b4[i][2] < b4[i + 1][2]:
                    b4[i], b4[i + 1] = b4[i + 1], b4[i]
def fonk2():
    b1 = open('table1.txt', "r")
    b2 = b1.read()
    b1.close()
    b3 = b2.split('\n')
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    b4 = []
    a1 = 0
    for b5 in b3:
        b5 = b5.split(',')
        b4.append(b5)
    fonk1(b4)
    for item in b4:
        b6 = item[0]
        b7 = item[1]
        b8 = item[2]
        b9 = item[3]
        b10 = int(b8) - int(b9)
        a1 += 1
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(int(a1), b6, int(b7), int(b10), int(b8), int(b9)))
def fonk3():
    print("Results b2 by gsoa420")
    print()
    print(fonk2())
if b11 = = "__main__":
    fonk3()