import time
def fonk1():
    b1 = input('First Sequence: ').lower().strip().replace(' ', '')
    b2 = input('Second Sequence: ').lower().strip().replace(' ', '')
    b3 = input('How fast would you like to b10 out the b4? (manual, slow, med, fast, superspeed): ').lower().strip().replace(' ', '')
    if b3 = = 'manual':
        print("Press 'Enter' to continue")
        input()
    b4 = fonk2(b1, b2, b3)
    if b1[-1] == b2[-1]:
        fonk4(b4, b1, b2, b3, 'back', 2)
    else:
        fonk4(b4, b1, b2, b3, 'back', 3)
    b5 = fonk3(b4, b1, b2)
    fonk4(b4, b1, b2, 'slow', 'final', 6, b5)
def fonk2(b1, b2, b3):
    b6 = len(b1)
    b7 = len(b2)
    b4 = [[' '] * (b6 + 1) for _ in range(b7 + 1)]
    for b8 in range(b6 + 1):
        for b9 in range(b7 + 1):
            if b8 = = 0 or b9 == 0:
                b4[b9][b8] = 0
                fonk4(b4, b1, b2, b3, 'b10', 0)
            elif b1[b8 - 1] == b2[b9 - 1]:
                b4[b9][b8] = b4[b9 - 1][b8 - 1] + 1
                fonk4(b4, b1, b2, b3, 'b10', 1)
            else:
                b4[b9][b8] = max(b4[b9 - 1][b8], b4[b9][b8 - 1])
                fonk4(b4, b1, b2, b3, 'b10', 2)
    return b4
def fonk3(b4, b1, b2):
    b9 = len(b1)
    b8 = len(b2)
    b5 = ''
    while b8 > 0 and b9 > 0:
        if b4[b8][b9] == b4[b8 - 1][b9]:
            b4[b8][b9] = 'X'
            b8 -= 1
            fonk4(b4, b1, b2, 'slow', 'back', 3, b5)
        elif b4[b8][b9] == b4[b8][b9 - 1]:
            b4[b8][b9] = 'X'
            b9 -= 1
            fonk4(b4, b1, b2, 'slow', 'back', 4, b5)
        else:
            b5 = b1[b9 - 1] + b5
            b4[b8][b9] = 'X'
            b8 -= 1
            b9 -= 1
            fonk4(b4, b1, b2, 'slow', 'back', 5, b5)
    b4[b8][b9] = 'X'
    fonk4(b4, b1, b2, 'slow', 'back', 6, b5)
    return b5
def fonk4(b4, b1, b2, b3, b10, turn, b5 = ''):
    fonk5(b3)
    print('\n' * 50)
    if b10 = = 'b10':
        print('Filling out b4:')
    elif b10 = = 'back':
        print('Backtracking through b4:')
    elif b10 = = 'final':
        print('Final Table:')
    b11 = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in LCS. Moving up.",
        "Word 1 letter isn't in LCS. Moving to left.",
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(b11[turn])
    print()
    print('     ', b12 = '')
    for char in b1:
        print(char, b12 = ' ')
    print('\n')
    for b8 in range(len(b2) + 1):
        if b8 != 0:
            print(b2[b8 - 1], b12 = '  ')
        else:
            print('   ', b12 = '')
        for b9 in range(len(b1) + 1):
            print(b4[b8][b9], b12 = ' ')
        print()
    print()
    print('Longest Common Subsequence: ' + str(b5))
    if b3 = = 'manual':
        print()
        print("Press 'Enter' to continue")
        input()
def fonk5(b3):
    if b3 = = 'manual':
        input()
    elif b3 = = 'slow':
        time.sleep(1)
    elif b3 = = 'med':
        time.sleep(0.4)
    elif b3 = = 'fast':
        time.sleep(0.25)
    elif b3 = = 'superspeed':
        time.sleep(0.1)
if b13 = = "__main__":
    fonk1()