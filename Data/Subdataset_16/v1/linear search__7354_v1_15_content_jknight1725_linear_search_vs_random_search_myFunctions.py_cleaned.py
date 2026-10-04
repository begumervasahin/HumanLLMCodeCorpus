import random
from time import process_time
def fonk1(a5, a6):
    a1 = -1
    while a1 < a5 or a1 > a6:
        a1 = int(input(f"Enter a b11 between {a5} and {a6}: "))
    return a1
def fonk2():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def fonk3(b13):
    print(f'Computer says: {b13}')
def fonk4(lower, upper):
    return (upper + lower)
def fonk5():
    b1 = '0'
    while b1 not in 'lsc':
        b1 = input(fonk2())[0]
    return b1
def fonk6(b1, b13, a5, a6):
    if b1 = = 'l':
        return [b13, a6]
    elif b1 = = 's':
        return [a5, b13]
    elif b1 = = 'c':
        return [a5, a6]
    else:
        return "Error\n"
def fonk7(b13, a3):
    print(f'Done! Your b11 is {b13}. Guessed in {a3} times!')
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
    b4 = random.randrange(10)
    b5 = random.randrange(10)
    b6 = random.randrange(10)
    return [b4, b5, b6]
def fonk12():
    return int(input("Enter a b11: "))
def fonk13():
    b4 = fonk12()
    b5 = fonk12()
    b6 = fonk12()
    return [b4, b5, b6]
def fonk14(b7, rand_numbers):
    return b7 = = rand_numbers
def fonk15():
    b8 = []
    for b4 in range(0, 1000):
        b9 = str(b4).zfill(3)
        b8.append(b9)
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
    while fonk11() != three_random_numbers and a3 < a4:
        a3 += 1
    return a3
if b10 = = "__main__":
    a5 = 1
    a6 = 100
    b11 = fonk1(a5, a6)
    a3 = 0
    b12 = False
    while not b12:
        b13 = fonk4(a5, a6)
        fonk3(b13)
        b1 = fonk5()
        a5, a6 = fonk6(b1, b13, a5, a6)
        a3 += 1
        if b1 = = 'c':
            b12 = True
            fonk7(b13, a3)
    b14 = fonk8(sum_up, 1000000)
    fonk9(b14)
    b15 = fonk11()
    b16 = fonk13()
    if fonk14(b16, b15):
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, better luck next time.")
    b8 = fonk15()
    a3 = fonk16(b8, b15)
    print(f'Worst case algorithm guessed in {a3} tries.')
    a3 = fonk17(b15)
    print(f'Random case algorithm guessed in {a3} tries.')