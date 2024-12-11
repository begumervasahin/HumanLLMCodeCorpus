def fonk1(b8):
    for pass_num in range(len(b8) - 1, 0, -1):
        for i in range(0, pass_num):
            if int(b8[i][1]) < int(b8[i + 1][1]):
                b8[i], b8[i + 1] = b8[i + 1], b8[i]
            if b8[i][1] == b8[i + 1][1]:
                if (int(b8[i][2]) - int(b8[i][3])) < (int(b8[i + 1][2]) - int(b8[i + 1][3])):
                    b8[i], b8[i + 1] = b8[i + 1], b8[i]
            if (b8[i][1] == b8[i + 1][1]) and (int(b8[i][2]) - int(b8[i][3])) == (int(b8[i + 1][2]) - int(b8[i + 1][3])):
                if b8[i][2] < b8[i + 1][2]:
                    b8[i], b8[i + 1] = b8[i + 1], b8[i]
def fonk2(filename):
    with open(filename, "r") as infile:
        b1 = infile.readlines()
    b2 = [line.strip().split(',') for line in b1]
    return b2
def fonk3(b8):
    print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
    a1 = 0
    for item in b8:
        b3 = item[0]
        b4 = int(item[1])
        b5 = int(item[2])
        b6 = int(item[3])
        b7 = b5 - b6
        a1 += 1
        print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(a1, b3, b4, b7, b5, b6))
def fonk4():
    print("Results b1 by gsoa420")
    print()
    b8 = fonk2('table1.txt')
    fonk1(b8)
    fonk3(b8)
if b9 = = "__main__":
    fonk4()