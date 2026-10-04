
from time import sleep
def runFunction ():
    b1 = str(input ('First Sequence: ')).lower().strip().replace(' ', '')
    b2 = str(input ('Second Sequence: ')).lower().strip().replace(' ', '')
    b3 = str(input ('How fast would you like to b11 out the b4? (manual, slow, med, fast, superspeed): ')).lower().strip().replace(' ', '')
    if (b3 = = 'manual'):
        print("Press 'Enter' to continue")
        input()
    b4 = dynamWoohoo(b1, b2, b3)
    if (b1[-1] == b2[-1]):
        printTable (b4, b1, b2, b3, 'back', 2)
    else:
        printTable (b4, b1, b2, b3, 'back', 3)
    b5 = whatIsLCS (b4, b1, b2)
    printTable (b4, b1, b2, 'slow', 'final', 6, b5)
def dynamWoohoo (b1, b2, b3):
    b6 = len(b1)
    b7 = len(b2)
    b8 = [[' '] * (b6+1) for b9 in range(b7+2)]
    for b9 in range (b6+1):
        for b10 in range (b7+1):
            if (b9 = = 0 or b10 == 0):
                b8[b10][b9] = 0
                printTable(b8, b1, b2, b3, 'b11', 0)
            elif (b1[b9-1] == b2[b10-1]):
                b8[b10][b9] = b8[b10-1][b9-1]+1
                printTable(b8, b1, b2, b3, 'b11', 1)
            else:
                b8[b10][b9] = max(b8[b10-1][b9], b8[b10][b9-1])
                printTable(b8, b1, b2, b3, 'b11', 2)
    return b8
def whatIsLCS (b8, b1, b2):
    b10 = len(b1)
    b9 = len(b2)
    b5 = ''
    while (b9>0 and b10>0):
        if (b8[b9][b10] == b8[b9-1][b10]):
            b8[b9][b10] = 'X'
            b9-=1
            printTable(b8, b1, b2, 'slow', 'back', 3, b5)
        elif (b8[b9][b10] == b8[b9][b10-1]):
            b8[b9][b10] = 'X'
            b10-=1
            printTable(b8, b1, b2, 'slow', 'back', 4, b5)
        else:
            b5 = b1[b10-1] + b5
            b8[b9][b10] = 'X'
            b9-=1
            b10-=1
            printTable(b8, b1, b2, 'slow', 'back', 5, b5)
    b8[b9][b10] = 'X'
    printTable(b8, b1, b2, 'slow', 'back', 6, b5)
    return b5
def printTable (b4, b1, b2, b3, b11, turn, b5 = ''):
    howFast (b3)
    print (50*'\n')
    if (b11 = = 'b11'):
        print('Filling out b4:')
    elif (b11 = = 'back'):
        print('Backtracking through b4:')
    elif(b11 = = 'final'):
        print('Final Table:')
    b12 = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in b5. Moving up.",
        "Word 1 letter isn't in b5. Moving to left.",
        'Letters are the same! Adding to b5.',
        'Table Complete!'
    ]
    print(b12[turn])
    print ()
    print('     ', b13 = '')
    for z in range(len(b1)):
        print (b1[z], b13 = '')
        print(' ', b13 = '')
    print('\n')
    for b9 in range(len(b2) + 1):
        if (b9!=0):
            print(b2[b9-1], b13 = '  ')
        else:
            print('   ', b13 = '')
        for b10 in range(len(b1) + 1):
            print (b4[b9][b10], b13 = ' ')
        print()
    print ()
    print('Longest Common Subsequence: ' + str(b5))
    if (b3 = = 'manual'):
        print()
        print("Press 'Enter' to continue")
def howFast (b3):
    if (b3 = = 'manual'):
        input()
    elif (b3 = = 'slow'):
        sleep (1)
    elif (b3 = = 'med'):
        sleep (0.4)
    elif (b3 = = 'fast'):
        sleep(0.25)
runFunction ()