import time
def fonk1():
    b1 = fonk2('First Sequence: ')
    b2 = fonk2('Second Sequence: ')
    b3 = fonk2('How fast would you like to b8 out the b4? (manual, slow, med, fast, superspeed): ')
    if b3 = = 'manual':
        fonk3()
    b4 = fonk4(b1, b2, b3)
    fonk6(b1, b2, b3, b4)
    b5 = fonk5(b4, b1, b2)
    fonk7(b4, b1, b2, b5)
def fonk2(prompt):
    return input(prompt).lower().strip().replace(' ', '')
def fonk3():
    print("Press 'Enter' to continue")
    input()
def fonk4(b1, b2, b3):
    x, b6 = len(b1), len(b2)
    b4 = [[' '] * (x + 1) for _ in range(b6 + 1)]
    for b7 in range(x + 1):
        for j in range(b6 + 1):
            if b7 = = 0 or j == 0:
                b4[j][b7] = 0
                fonk8(b4, b1, b2, b3, 'b8', 0)
            elif b1[b7 - 1] == b2[j - 1]:
                b4[j][b7] = b4[j - 1][b7 - 1] + 1
                fonk8(b4, b1, b2, b3, 'b8', 1)
            else:
                b4[j][b7] = max(b4[j - 1][b7], b4[j][b7 - 1])
                fonk8(b4, b1, b2, b3, 'b8', 2)
    return b4
def fonk5(b4, b1, b2):
    j, b7 = len(b1), len(b2)
    b5 = ''
    while b7 > 0 and j > 0:
        if b4[b7][j] == b4[b7 - 1][j]:
            b4[b7][j] = 'X'
            b7 -= 1
            fonk8(b4, b1, b2, 'slow', 'back', 3, b5)
        elif b4[b7][j] == b4[b7][j - 1]:
            b4[b7][j] = 'X'
            j -= 1
            fonk8(b4, b1, b2, 'slow', 'back', 4, b5)
        else:
            b5 = b1[j - 1] + b5
            b4[b7][j] = 'X'
            b7 -= 1
            j -= 1
            fonk8(b4, b1, b2, 'slow', 'back', 5, b5)
    b4[b7][j] = 'X'
    fonk8(b4, b1, b2, 'slow', 'back', 6, b5)
    return b5
def fonk6(b1, b2, b3, b4):
    if b1[-1] == b2[-1]:
        fonk8(b4, b1, b2, b3, 'back', 2)
    else:
        fonk8(b4, b1, b2, b3, 'back', 3)
def fonk7(b4, b1, b2, b5):
    fonk8(b4, b1, b2, 'slow', 'final', 6, b5)
def fonk8(b4, b1, b2, b3, b8, turn, b5 = ''):
    fonk9(b3)
    print('\n' * 50)
    if b8 = = 'b8':
        print('Filling out b4:')
    elif b8 = = 'back':
        print('Backtracking through b4:')
    elif b8 = = 'final':
        print('Final Table:')
    b9 = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in LCS. Moving up.",
        "Word 1 letter isn't in LCS. Moving to left.",
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(b9[turn])
    print()
    print('     ', b10 = '')
    for char in b1:
        print(char, b10 = ' ')
    print('\n')
    for b7 in range(len(b2) + 1):
        if b7 != 0:
            print(b2[b7 - 1], b10 = '  ')
        else:
            print('   ', b10 = '')
        for j in range(len(b1) + 1):
            print(b4[b7][j], b10 = ' ')
        print()
    print()
    print('Longest Common Subsequence: ' + str(b5))
    if b3 = = 'manual':
        fonk3()
def fonk9(b3):
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
if b11 = = "__main__":
    fonk1()