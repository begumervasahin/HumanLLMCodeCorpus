from time import sleep
def fonk1():
    b1 = input('First Sequence: ').lower().strip().replace(' ', '')
    b2 = input('Second Sequence: ').lower().strip().replace(' ', '')
    b3 = input('How fast would you like to fill out the b4? (manual, slow, med, fast, superspeed): ').lower().strip().replace(' ', '')
    if b3 = = 'manual':
        print("Press 'Enter' to continue")
        input()
    b4 = fonk2(b1, b2, b3)
    fonk4(b4, b1, b2, b3, 'back', 2 if b1[-1] == b2[-1] else 3)
    b5 = fonk3(b4, b1, b2)
    fonk4(b4, b1, b2, 'slow', 'final', 6, b5)
def fonk2(b1, b2, b3):
    x, b6 = len(b1), len(b2)
    b4 = [[' '] * (x + 1) for _ in range(b6 + 1)]
    for b7 in range(x + 1):
        for b8 in range(b6 + 1):
            if b7 = = 0 or b8 == 0:
                b4[b8][b7] = 0
                fonk4(b4, b1, b2, b3, 'fill', 0)
            elif b1[b7 - 1] == b2[b8 - 1]:
                b4[b8][b7] = b4[b8 - 1][b7 - 1] + 1
                fonk4(b4, b1, b2, b3, 'fill', 1)
            else:
                b4[b8][b7] = max(b4[b8 - 1][b7], b4[b8][b7 - 1])
                fonk4(b4, b1, b2, b3, 'fill', 2)
    return b4
def fonk3(b4, b1, b2):
    b7, b8 = len(b2), len(b1)
    b5 = ''
    while b7 > 0 and b8 > 0:
        if b4[b7][b8] == b4[b7 - 1][b8]:
            b4[b7][b8] = 'X'
            b7 -= 1
            fonk4(b4, b1, b2, 'slow', 'back', 3, b5)
        elif b4[b7][b8] == b4[b8][b8 - 1]:
            b4[b7][b8] = 'X'
            b8 -= 1
            fonk4(b4, b1, b2, 'slow', 'back', 4, b5)
        else:
            b5 = b1[b8 - 1] + b5
            b4[b7][b8] = 'X'
            b7 -= 1
            b8 -= 1
            fonk4(b4, b1, b2, 'slow', 'back', 5, b5)
    b4[b7][b8] = 'X'
    fonk4(b4, b1, b2, 'slow', 'back', 6, b5)
    return b5
def fonk4(b4, b1, b2, b3, b9, step, b5 = ''):
    fonk5(b3)
    print('\n' * 50)
    if b9 = = 'fill':
        print('Filling out b4:')
    elif b9 = = 'back':
        print('Backtracking through b4:')
    elif b9 = = 'final':
        print('Final Table:')
    b10 = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in LCS. Moving up.",
        "Word 1 letter isn't in LCS. Moving to left.",
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(b10[step])
    print()
    print('     ', b11 = '')
    for char in b1:
        print(f'{char} ', b11 = '')
    print('\n')
    for b7 in range(len(b2) + 1):
        if b7 != 0:
            print(f'{b2[b7 - 1]}  ', b11 = '')
        else:
            print('   ', b11 = '')
        for b8 in range(len(b1) + 1):
            print(f'{b4[b7][b8]} ', b11 = '')
        print()
    print()
    print(f'Longest Common Subsequence: {b5}')
    if b3 = = 'manual':
        print("\nPress 'Enter' to continue")
        input()
def fonk5(b3):
    b12 = {
        'manual': input,
        'slow': lambda: sleep(1),
        'med': lambda: sleep(0.4),
        'fast': lambda: sleep(0.25),
        'superspeed': lambda: sleep(0.1)
    }
    b12.get(b3, lambda: None)()
if b13 = = "__main__":
    fonk1()