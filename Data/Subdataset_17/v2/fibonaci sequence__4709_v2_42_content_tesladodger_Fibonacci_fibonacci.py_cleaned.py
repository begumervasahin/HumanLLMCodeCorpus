import sys
import os
from datetime import datetime
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
def ntimes(n):
    try:
        n = int(n)
    except ValueError:
        print('\n\nYou must introduce an integer\n\n')
        return False
    if n <= 0:
        print('\n\nYou must introduce a positive integer\n\n')
        return False
    clear_screen()
    num, next_num = 1, 1
    print(num)
    for _ in range(n - 1):
        print(next_num)
        num, next_num = next_num, num + next_num
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    ntimes_choice = input('==> ').strip().lower()
    return ntimes_choice == 's'
def upton(maxnum):
    try:
        maxnum = int(maxnum)
    except ValueError:
        print('\n\nYou must introduce an integer\n\n')
        return
    if maxnum < 1:
        print('\n\nYou must insert a value greater or equal to 1\n\n')
        return
    clear_screen()
    num, next_num = 1, 1
    itera = 0
    print(num)
    while next_num <= maxnum:
        print(next_num)
        num, next_num = next_num, num + next_num
        itera += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    upton_choice = input('==> ').strip().lower()
    if upton_choice == 's':
        clear_screen()
        if num == maxnum:
            print(f"The number {maxnum} is in the Fibonacci sequence")
        print(f"Number of iterations:       {itera}")
        print(f"Your number:                {maxnum}")
        print(f"Next number in the sequence:{next_num}")
        print(f"Difference to that number:   {next_num - maxnum}\n\n")
def file_saver(n):
    name = input('Name of the file: ').strip().replace(" ", "") + '.txt'
    with open(name, "w") as file:
        file.write(f"Number of iterations: {n}\n")
        num, next_num = 1, 1
        for _ in range(int(n)):
            file.write(f"{num}\n")
            num, next_num = next_num, num + next_num
    return name
def greeting_message():
    hour = datetime.now().hour
    if hour >= 20:
        return 'night!'
    elif hour >= 12:
        return 'afternoon!'
    elif hour >= 5:
        return 'day!'
    else:
        return 'night!'
def main():
    clear_screen()
    print(' __________________________')
    print('|                          |')
    print('|** Fibonacci calculator **|')
    print('|__________________________|\n\n')
    while True:
        print('1 - Calculate n number of times')
        print('2 - Calculate up to a certain number')
        print('T - Terminate')
        choice = input('==> ').strip().upper()
        if choice == '1':
            n = input('Number of times: ').strip()
            save_file = ntimes(n)
            if save_file:
                name = file_saver(n)
                clear_screen()
                print(f'\nFile saved as: {name}\n\n')
        elif choice == '2':
            maxnum = input('Calculate to the number: ').strip()
            upton(maxnum)
        elif choice == 'T':
            greeting = greeting_message()
            print(f'\nThank you, have a good {greeting}')
            break
        else:
            clear_screen()
            print('\nInvalid option\n')
if __name__ == "__main__":
    main()