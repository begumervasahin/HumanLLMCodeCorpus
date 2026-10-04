from random import randrange
from time import process_time
def fonk1(a3, a4):
    while True:
        try:
            b1 = int(input(f"Enter a number between {a3} and {a4}: "))
            if a3 <= b1 <= a4:
                return b1
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")
def fonk2():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
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
def fonk8(b2, cpu_guess, a3, a4):
    if b2 = = 'l':
        return [cpu_guess, a4]
    elif b2 = = 's':
        return [a3, cpu_guess]
    elif b2 = = 'c':
        return [a3, a4]
def fonk9(b3, b10):
    return b3 = = b10
def fonk10(func, *args):
    b4 = process_time()
    b5 = func(*args)
    b6 = process_time()
    b7 = b6 - b4
    b8 = {
        'start': b4,
        'end': b6,
        'total': b7
    }
    return b5, b8
def fonk11(b11, three_random_numbers):
    for idx, option in enumerate(b11):
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
if b9 = = "__main__":
    a3 = 0
    a4 = 9
    b3 = fonk3()
    b10 = fonk14()
    print("Random Numbers: ", b10)
    print("User Numbers: ", b3)
    if fonk9(b3, b10):
        print("Congratulations! You guessed the correct numbers!")
    else:
        print("Try again!")
    b11 = fonk15()
    b5, b8 = fonk10(worst_case_algorithm, b11, b10)
    print(f"Worst Case Algorithm Result: {b5}")
    fonk6(b8)
    b5, b8 = fonk10(random_case_algorithm, b10)
    print(f"Random Case Algorithm Result: {b5}")
    fonk6(b8)