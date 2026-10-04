def f(x):
    return abs(x) ** 0.5 + 5 * x ** 3
def ask():
    while True:
        try:
            numbers = input('\nEnter 11 numbers: ').strip().split()
            if len(numbers) != 11:
                print("Please enter exactly 11 numbers.")
                continue
            return [float(y) for y in numbers]
        except ValueError:
            print("Please enter valid numbers.")
if __name__ == '__main__':
    numbers = ask()
    numbers.reverse()
    for x in numbers:
        result = f(x)
        if result > 400:
            print(f' {x}: TOO LARGE!', end='')
        else:
            print(f' {x}: {result}', end='')
    print('')