from time import sleep
def run_function():
    word1 = input('First Sequence: ').lower().strip().replace(' ', '')
    word2 = input('Second Sequence: ').lower().strip().replace(' ', '')
    speed = input('How fast would you like to fill out the table? (manual, slow, med, fast, superspeed): ').lower().strip().replace(' ', '')
    if speed == 'manual':
        print("Press 'Enter' to continue")
        input()
    table = fill_table(word1, word2, speed)
    print_table(table, word1, word2, speed, 'back', 2 if word1[-1] == word2[-1] else 3)
    lcs = find_lcs(table, word1, word2)
    print_table(table, word1, word2, 'slow', 'final', 6, lcs)
def fill_table(word1, word2, speed):
    x, y = len(word1), len(word2)
    table = [[' '] * (x + 1) for _ in range(y + 1)]
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                table[j][i] = 0
                print_table(table, word1, word2, speed, 'fill', 0)
            elif word1[i - 1] == word2[j - 1]:
                table[j][i] = table[j - 1][i - 1] + 1
                print_table(table, word1, word2, speed, 'fill', 1)
            else:
                table[j][i] = max(table[j - 1][i], table[j][i - 1])
                print_table(table, word1, word2, speed, 'fill', 2)
    return table
def find_lcs(table, word1, word2):
    i, j = len(word2), len(word1)
    lcs = ''
    while i > 0 and j > 0:
        if table[i][j] == table[i - 1][j]:
            table[i][j] = 'X'
            i -= 1
            print_table(table, word1, word2, 'slow', 'back', 3, lcs)
        elif table[i][j] == table[j][j - 1]:
            table[i][j] = 'X'
            j -= 1
            print_table(table, word1, word2, 'slow', 'back', 4, lcs)
        else:
            lcs = word1[j - 1] + lcs
            table[i][j] = 'X'
            i -= 1
            j -= 1
            print_table(table, word1, word2, 'slow', 'back', 5, lcs)
    table[i][j] = 'X'
    print_table(table, word1, word2, 'slow', 'back', 6, lcs)
    return lcs
def print_table(table, word1, word2, speed, mode, step, lcs=''):
    control_speed(speed)
    print('\n' * 50)
    if mode == 'fill':
        print('Filling out table:')
    elif mode == 'back':
        print('Backtracking through table:')
    elif mode == 'final':
        print('Final Table:')
    steps = [
        'Base Case.',
        'Letters are the same! Increasing index',
        'Letters are different. Taking max of left and above.',
        "Word 2 letter isn't in LCS. Moving up.",
        "Word 1 letter isn't in LCS. Moving to left.",
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(steps[step])
    print()
    print('     ', end='')
    for char in word1:
        print(f'{char} ', end='')
    print('\n')
    for i in range(len(word2) + 1):
        if i != 0:
            print(f'{word2[i - 1]}  ', end='')
        else:
            print('   ', end='')
        for j in range(len(word1) + 1):
            print(f'{table[i][j]} ', end='')
        print()
    print()
    print(f'Longest Common Subsequence: {lcs}')
    if speed == 'manual':
        print("\nPress 'Enter' to continue")
        input()
def control_speed(speed):
    speed_dict = {
        'manual': input,
        'slow': lambda: sleep(1),
        'med': lambda: sleep(0.4),
        'fast': lambda: sleep(0.25),
        'superspeed': lambda: sleep(0.1)
    }
    speed_dict.get(speed, lambda: None)()
if __name__ == "__main__":
    run_function()