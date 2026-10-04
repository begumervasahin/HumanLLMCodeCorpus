def print_A():
    for row in range(6):
        for col in range(11):
            if (row + col == 5) or (col - row == 5) or (row == 3 and row + col in [7, 9]):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def print_M():
    for row in range(6):
        for col in range(11):
            if (col == 0) or (col - row == 0) or (row + col == 10) or (col == 10):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def print_I():
    for row in range(7):
        for col in range(11):
            if (col == 5):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def print_T():
    for row in range(6):
        for col in range(11):
            if (col != 5 and row == 0) or (col == 5):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def print_V():
    for row in range(6):
        for col in range(11):
            if (row + col == 10) or (row - col == 0):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def main():
    print_A()
    print('\n')
    print_M()
    print('\n')
    print_I()
    print('\n')
    print_T()
    print('\n')
    print_V()
if __name__ == "__main__":
    main()