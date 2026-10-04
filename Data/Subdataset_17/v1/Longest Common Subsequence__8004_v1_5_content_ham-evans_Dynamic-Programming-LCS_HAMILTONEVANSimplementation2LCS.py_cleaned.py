import time
def runFunction():
    word1 = input('First Sequence: ').lower().strip().replace(' ', '')
    word2 = input('Second Sequence: ').lower().strip().replace(' ', '')
    speed = input('How fast would you like to fill out the table? (manual, slow, med, fast, superspeed): ').lower().strip().replace(' ', '')
    if speed == 'manual':
        print("Press 'Enter' to continue")
        input()
    table = dynamWoohoo(word1, word2, speed)
    if word1[-1] == word2[-1]:
        printTable(table, word1, word2, speed, 'back', 2)
    else:
        printTable(table, word1, word2, speed, 'back', 3)
    LCS = whatIsLCS(table, word1, word2)
    printTable(table, word1, word2, 'slow', 'final', 6, LCS)
def dynamWoohoo(word1, word2, speed):
    x = len(word1)
    y = len(word2)
    store = [[' '] * (x + 1) for _ in range(y + 1)]
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                store[j][i] = 0
                printTable(store, word1, word2, speed, 'fill', 0)
            elif word1[i - 1] == word2[j - 1]:
                store[j][i] = store[j - 1][i - 1] + 1
                printTable(store, word1, word2, speed, 'fill', 1)
            else:
                store[j][i] = max(store[j - 1][i], store[j][i - 1])
                printTable(store, word1, word2, speed, 'fill', 2)
    return store
def whatIsLCS(store, word1, word2):
    j = len(word1)
    i = len(word2)
    LCS = ''
    while i > 0 and j > 0:
        if store[i][j] == store[i - 1][j]:
            store[i][j] = 'X'
            i -= 1
            printTable(store, word1, word2, 'slow', 'back', 3, LCS)
        elif store[i][j] == store[i][j - 1]:
            store[i][j] = 'X'
            j -= 1
            printTable(store, word1, word2, 'slow', 'back', 4, LCS)
        else:
            LCS = word1[j - 1] + LCS
            store[i][j] = 'X'
            i -= 1
            j -= 1
            printTable(store, word1, word2, 'slow', 'back', 5, LCS)
    store[i][j] = 'X'
    printTable(store, word1, word2, 'slow', 'back', 6, LCS)
    return LCS
def printTable(table, word1, word2, speed, fill, turn, LCS=''):
    howFast(speed)
    print('\n' * 50)
    if fill == 'fill':
        print('Filling out table:')
    elif fill == 'back':
        print('Backtracking through table:')
    elif fill == 'final':
        print('Final Table:')
    whatsHappening = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in LCS. Moving up.",
        "Word 1 letter isn't in LCS. Moving to left.",
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(whatsHappening[turn])
    print()
    print('     ', end='')
    for z in range(len(word1)):
        print(word1[z], end=' ')
    print('\n')
    for i in range(len(word2) + 1):
        if i != 0:
            print(word2[i - 1], end='  ')
        else:
            print('   ', end='')
        for j in range(len(word1) + 1):
            print(table[i][j], end=' ')
        print()
    print()
    print('Longest Common Subsequence: ' + str(LCS))
    if speed == 'manual':
        print()
        print("Press 'Enter' to continue")
        input()
def howFast(speed):
    if speed == 'manual':
        input()
    elif speed == 'slow':
        time.sleep(1)
    elif speed == 'med':
        time.sleep(0.4)
    elif speed == 'fast':
        time.sleep(0.25)
    elif speed == 'superspeed':
        time.sleep(0.1)
if __name__ == "__main__":
    runFunction()