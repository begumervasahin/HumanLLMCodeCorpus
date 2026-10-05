import os
import sys
import datetime
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\nYou must enter an integer.\n')
def n_times_fibonacci(n, clear):
    try:
        n = int(n)
    except ValueError:
        print('\nYou must enter an integer.\n')
        return
    if n <= 0:
        print('\nYou must enter a positive integer.\n')
        return
    os.system(clear)
    num = 1
    next_num = 1
    print(num)
    for _ in range(n - 1):
        print(next_num)
        num, next_num = next_num, num + next_num
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    ntimes_choice = input('==> ')
    return ntimes_choice.lower() == 's'
def fibonacci_up_to(maxnum, clear):
    try:
        maxnum = int(maxnum)
    except ValueError:
        print('\nYou must enter an integer.\n')
        return
    if maxnum < 1:
        print('\nYou must enter a value greater than or equal to 1.\n')
        return
    os.system(clear)
    num = 1
    next_num = 1
    iterations = 0
    print(num)
    while next_num <= maxnum:
        print(next_num)
        num, next_num = next_num, num + next_num
        iterations += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    upton_choice = input('==> ')
    if upton_choice.lower() == 's':
        os.system(clear)
        if next_num == maxnum:
            print(f"The number {maxnum} is in the Fibonacci sequence.")
        print(f"Number of iterations:       {iterations}")
        print(f"Your number:                {maxnum}")
        print(f"Next number in the sequence: {next_num}")
        print(f"Difference to that number:   {next_num - maxnum}\n\n")
def save_to_file(n):
    name = input('Name of the file: ').replace(" ", "") + '.txt'
    with open(name, "w") as file:
        conc = f"Number of iterations: {n}\n"
        file.write(conc)
        num = 1
        next_num = 1
        for _ in range(n):
            file.write(f"{num}\n")
            num, next_num = next_num, num + next_num
    return name
def get_time_of_day():
    hour = datetime.datetime.now().hour
    if hour >= 20:
        return 'night!'
    elif hour >= 12:
        return 'afternoon!'
    elif hour >= 5:
        return 'day!'
    else:
        return 'night!'
platform = sys.platform
clear = 'cls' if platform == 'win32' else 'clear'
os.system(clear)
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\n\n')
while True:
    print('1 - Calculate Fibonacci sequence n times')
    print('2 - Calculate Fibonacci sequence up to a certain number')
    print('T - Terminate')
    choice = input('==> ').upper()
    if choice == '1':
        n = get_integer_input('Number of times: ')
        if n > 0 and n_times_fibonacci(n, clear):
            name = save_to_file(n)
            os.system(clear)
            print(f'\nFile saved as: {name}\n\n')
    elif choice == '2':
        maxnum = get_integer_input('Calculate up to the number: ')
        if maxnum >= 1:
            fibonacci_up_to(maxnum, clear)
    elif choice == 'T':
        greeting = get_time_of_day()
        print(f'\nThank you, have a good {greeting}')
        break
    else:
        os.system(clear)
        print('\nInvalid option\n')