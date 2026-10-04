import time
def run_function():
    word1 = input('First Sequence: ').lower().strip().replace(' ', '')
    word2 = input('Second Sequence: ').lower().strip().replace(' ', '')
    speed = input('How fast would you like to fill out the table? (manual, slow, med, fast, superspeed): ').lower().strip().replace(' ', '')
    if speed == 'manual':
        print("Press 'Enter' to continue")
        input()
    table = build_lcs_table(word1, word2, speed)
    if word1[-1] == word2[-1]:
        display_table(table, word1, word2, speed, 'back', 2)
    else:
        display_table(table, word1, word2, speed, 'back', 3)
    lcs = extract_lcs(table, word1, word2)
    display_table(table, word1, word2, 'slow', 'final', 6, lcs)
def build_lcs_table(word1, word2, speed):
    x = len(word1)
    y = len(word2)
    table = [[' '] * (x + 1) for _ in range(y + 1)]
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                table[j][i] = 0
                display_table(table, word1, word2, speed, 'fill', 0)
            elif word1[i - 1] == word2[j - 1]:
                table[j][i] = table[j - 1][i - 1] + 1
                display_table(table, word1, word2, speed, 'fill', 1)
            else:
                table[j][i] = max(table[j - 1][i], table[j][i - 1])
                display_table(table, word1, word2, speed, 'fill', 2)
    return table
def extract_lcs(table, word1, word2):
    j = len(word1)
    i = len(word2)
    lcs = ''
    while i > 0 and j > 0:
        if table[i][j] == table[i - 1][j]:
            table[i][j] = 'X'
            i -= 1
            display_table(table, word1, word2, 'slow', 'back', 3, lcs)
        elif table[i][j] == table[i][j - 1]:
            table[i][j] = 'X'
            j -= 1
            display_table(table, word1, word2, 'slow', 'back', 4, lcs)
        else:
            lcs = word1[j - 1] + lcs
            table[i][j] = 'X'
            i -= 1
            j -= 1
            display_table(table, word1, word2, 'slow', 'back', 5, lcs)
    table[i][j] = 'X'
    display_table(table, word1, word2, 'slow', 'back', 6, lcs)
    return lcs
def display_table(table, word1, word2, speed, fill, turn, lcs=''):
    control_speed(speed)
    print('\n' * 50)
    if fill == 'fill':
        print('Filling out table:')
    elif fill == 'back':
        print('Backtracking through table:')
    elif fill == 'final':
        print('Final Table:')
    steps_description = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in LCS. Moving up.",
        "Word 1 letter isn't in LCS. Moving to left.",
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(steps_description[turn])
    print()
    print('     ', end='')
    for char in word1:
        print(char, end=' ')
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
    print('Longest Common Subsequence: ' + str(lcs))
    if speed == 'manual':
        print()
        print("Press 'Enter' to continue")
        input()
def control_speed(speed):
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
    run_function()