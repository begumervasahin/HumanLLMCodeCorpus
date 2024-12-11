from random import randrange
from time import process_time
def fonk1(lower_bound, upper_bound):
    a1 = -1
    while a1 < lower_bound or a1 > upper_bound:
        a1 = int(input(f"Enter a number between {lower_bound} and {upper_bound}: "))
    return a1
def fonk2():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def fonk3(cpu_guess):
    print(f'Computer says: {cpu_guess}')
def fonk4(lower, upper):
    return (upper + lower)
def fonk5():
    b1 = '0'
    while b1 not in 'lsc':
        b1 = input(fonk2())[0]
    return b1
def fonk6(b1, cpu_guess, lower_bound, upper_bound):
    if b1 = = 'l':
        return [cpu_guess, upper_bound]
    elif b1 = = 's':
        return [lower_bound, cpu_guess]
    elif b1 = = 'c':
        return [lower_bound, upper_bound]
    else:
        return "Error\n"
def fonk7(cpu_guess, a3):
    print(f'Done! Your number is {cpu_guess} . Guessed in {a3} times!')
def fonk8(func, *args):
    b2 = process_time()
    func(*args)
    b3 = process_time()
    return {
        'start': b2,
        'end': b3,
        'total': b3 - b2
    }
def fonk9(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']}\n")
def fonk10(large_num):
    return int((large_num * (large_num + 1)) / 2)
def fonk11():
    b4 = randrange(10)
    b5 = randrange(10)
    b6 = randrange(10)
    return [b4, b5, b6]
def fonk12():
    return int(input("Enter a number: "))
def fonk13():
    b4 = fonk12()
    b5 = fonk12()
    b6 = fonk12()
    return [b4, b5, b6]
def fonk14(b7, rand_numbers):
    return True if b7 = = rand_numbers else False
def fonk15():
    b8 = []
    for b4 in range(0, 1000):
        while (len(str(b4))) < 3:
            b4 = '0' + str(b4)
        b8.append(str(b4))
    return b8
def fonk16(b8, three_random_numbers):
    a2 = 0
    a3 = 1
    while [int(i) for i in str(b8[a2])] != three_random_numbers:
        a2 += 1
        a3 += 1
    return a3
def fonk17(three_random_numbers):
    a4 = 5000
    a3 = 1
    while (fonk11() != three_random_numbers) and a3 < a4:
        a3 += 1
    return a3