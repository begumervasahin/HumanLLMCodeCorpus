from random import randrange
from time import process_time
def fonk1(a5, a6):
    a1 = -1
    while a1 < a5 or a1 > a6:
        a1 = int(input(f"Enter a number between {a5} and {a6}: "))
    return a1
def fonk2():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def fonk3(b13):
    print(f'Computer says: {b13}')
def fonk4(b11, b12):
    return (b12 + b11)
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
    print(f'Done! Your number is {b13}. Guessed in {a3} attempts!')
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
def fonk10(a7):
    return int((a7 * (a7 + 1)) / 2)
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
    return b7 = = rand_numbers
def fonk15():
    b8 = []
    for b4 in range(0, 1000):
        while len(str(b4)) < 3:
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
if b9 = = "__main__":
    a5 = 1
    a6 = 100
    b10 = fonk1(a5, a6)
    a3 = 0
    b11 = a5
    b12 = a6
    b13 = fonk4(b11, b12)
    while True:
        fonk3(b13)
        b1 = fonk5()
        if b1 = = 'c':
            a3 += 1
            fonk7(b13, a3)
            break
        b11, b12 = fonk6(b1, b13, b11, b12)
        b13 = fonk4(b11, b12)
        a3 += 1
    a7 = 1000000
    b14 = fonk8(sum_up, a7)
    fonk9(b14)
    b15 = fonk11()
    b16 = fonk13()
    if fonk14(b16, b15):
        print("You win!")
    else:
        print("Try again!")
    b8 = fonk15()
    a3 = fonk16(b8, b15)
    print(f"Worst case a3: {a3}")
    a3 = fonk17(b15)
    print(f"Random case a3: {a3}")