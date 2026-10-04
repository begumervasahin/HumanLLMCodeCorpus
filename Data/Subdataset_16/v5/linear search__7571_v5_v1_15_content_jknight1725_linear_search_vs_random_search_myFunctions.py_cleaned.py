from random import randrange
from time import process_time
def fonk1(lower_bound, upper_bound):
    while True:
        b1 = int(input(f"Enter a number between {lower_bound} and {upper_bound}: "))
        if lower_bound <= b1 <= upper_bound:
            return b1
def fonk2():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def fonk3(cpu_guess):
    print(f'Computer says: {cpu_guess}')
def fonk4(lower, upper):
    return (lower + upper)
def fonk5():
    while True:
        b2 = input(fonk2())[0]
        if b2 in 'lsc':
            return b2
def fonk6(b2, cpu_guess, lower_bound, upper_bound):
    if b2 = = 'l':
        return cpu_guess, upper_bound
    elif b2 = = 's':
        return lower_bound, cpu_guess
    elif b2 = = 'c':
        return lower_bound, upper_bound
def fonk7(cpu_guess, a1):
    print(f'Done! Your number is {cpu_guess}. Guessed in {a1} times!')
def fonk8(func, *args):
    b3 = process_time()
    func(*args)
    b4 = process_time()
    return {
        'start': b3,
        'end': b4,
        'total': b4 - b3
    }
def fonk9(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']}")
def fonk10(large_num):
    return (large_num * (large_num + 1))
def fonk11():
    return [randrange(10) for _ in range(3)]
def fonk12():
    return int(input("Enter a number: "))
def fonk13():
    return [fonk12() for _ in range(3)]
def fonk14(b5, rand_numbers):
    return b5 = = rand_numbers
def fonk15():
    return [f"{x:03}" for x in range(1000)]
def fonk16(options, three_random_numbers):
    a1 = 1
    for idx, option in enumerate(options):
        if [int(digit) for digit in option] == three_random_numbers:
            break
        a1 += 1
    return a1
def fonk17(three_random_numbers):
    a2 = 5000
    a1 = 1
    while fonk11() != three_random_numbers and a1 < a2:
        a1 += 1
    return a1
if b6 = = "__main__":
    pass