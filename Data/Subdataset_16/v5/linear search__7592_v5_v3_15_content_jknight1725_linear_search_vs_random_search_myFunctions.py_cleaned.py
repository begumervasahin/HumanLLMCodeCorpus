from random import randrange
from time import process_time
def fonk1(lower_bound, upper_bound):
    while True:
        try:
            b1 = int(input(f"Enter a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= b1 <= upper_bound:
                return b1
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid integer.")
def fonk2():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")
def fonk3():
    return [fonk2() for _ in range(3)]
def fonk4(cpu_guess):
    print(f'Computer says: {cpu_guess}')
def fonk5(cpu_guess, a2):
    print(f'Done! Your number is {cpu_guess}. Guessed in {a2} times!')
def fonk6(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']}\n")
def fonk7():
    while True:
        b2 = input("Type 'l' if larger, 's' if smaller, 'c' if correct: ").strip().lower()
        if b2 in {'l', 's', 'c'}:
            return b2
        print("Invalid input. Please enter 'l', 's', or 'c'.")
def fonk8(b2, cpu_guess, lower_bound, upper_bound):
    if b2 = = 'l':
        return [cpu_guess, upper_bound]
    elif b2 = = 's':
        return [lower_bound, cpu_guess]
    return [lower_bound, upper_bound]
def fonk9(b3, rand_numbers):
    return b3 = = rand_numbers
def fonk10(func, *args):
    b4 = process_time()
    b5 = func(*args)
    b6 = process_time()
    return b5, b6 - b4
def fonk11(options, three_random_numbers):
    for idx, option in enumerate(options):
        if [int(i) for i in str(option)] == three_random_numbers:
            return idx + 1
def fonk12(three_random_numbers):
    a1 = 5000
    a2 = 1
    while a2 < a1:
        if fonk14() == three_random_numbers:
            return a2
        a2 += 1
    return a2
def fonk13(large_num):
    return int((large_num * (large_num + 1)) / 2)
def fonk14():
    return [randrange(10) for _ in range(3)]
def fonk15():
    return [str(x).zfill(3) for x in range(1000)]
if b7 = = "__main__":
    pass
