def get_positive_integer():
    while True:
        try:
            n = int(input('Enter a positive integer: '))
            if n > 0:
                return n
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
def print_fibonacci_sequence(n_max):
    f1, f2 = 1, 2
    for n in range(1, n_max + 1):
        print(f'{n:4d}: {f1}')
        f1, f2 = f2, f1 + f2
def main():
    n_max = get_positive_integer()
    print_fibonacci_sequence(n_max)
if __name__ == '__main__':
    main()