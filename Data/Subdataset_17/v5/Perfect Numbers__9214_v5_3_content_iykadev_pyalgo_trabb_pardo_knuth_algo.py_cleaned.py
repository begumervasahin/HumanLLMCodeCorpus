import math
def f(x):
    return math.sqrt(abs(x)) + 5 * x ** 3
def ask():
    input_numbers = input('\nEnter 11 numbers separated by spaces: ')
    return [float(num) for num in input_numbers.strip().split()[:11]]
def main():
    numbers = ask()
    numbers.reverse()
    for x in numbers:
        result = f(x)
        if result > 400:
            print(f'{x}: TOO LARGE!', end=' ')
        else:
            print(f'{x}: {result}', end=' ')
    print('')
if __name__ == '__main__':
    main()