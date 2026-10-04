from random import randrange
from time import process_time
def fonk1(a4, a5):
    a1 = -1
    while a1 < a4 or a1 > a5:
        a1 = int(input(f"Enter a number between {a4} and {a5}: "))
    return a1
def fonk2():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def fonk3(b10):
    print(f'Computer says: {b10}')
def fonk4(b8, b9):
    return (b9 + b8)
def fonk5():
    b1 = ''
    while b1 not in 'lsc':
        b1 = input(fonk2())[0]
    return b1
def fonk6(b1, b10, a4, a5):
    if b1 = = 'l':
        return [b10, a5]
    elif b1 = = 's':
        return [a4, b10]
    elif b1 = = 'c':
        return [a4, a5]
def fonk7(b10, a2):
    print(f'Done! Your number is {b10}. Guessed in {a2} attempts!')
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
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']} seconds\n")
def fonk10(a6):
    return int((a6 * (a6 + 1)) / 2)
def fonk11():
    return [randrange(10) for _ in range(3)]
def fonk12(b4 = "Enter a number: "):
    return int(input(b4))
def fonk13():
    return [fonk12() for _ in range(3)]
def fonk14(b5, rand_numbers):
    return b5 = = rand_numbers
def fonk15():
    return [f"{x:03d}" for x in range(1000)]
def fonk16(b14, three_random_numbers):
    a2 = 1
    for idx in range(len(b14)):
        if [int(digit) for digit in b14[idx]] == three_random_numbers:
            break
        a2 += 1
    return a2
def fonk17(three_random_numbers):
    a3 = 5000
    a2 = 1
    while fonk11() != three_random_numbers and a2 < a3:
        a2 += 1
    return a2
if b6 = = "__main__":
    a4 = 1
    a5 = 100
    b7 = fonk1(a4, a5)
    a2 = 0
    b8 = a4
    b9 = a5
    b10 = fonk4(b8, b9)
    while True:
        fonk3(b10)
        b1 = fonk5()
        if b1 = = 'c':
            a2 += 1
            fonk7(b10, a2)
            break
        b8, b9 = fonk6(b1, b10, b8, b9)
        b10 = fonk4(b8, b9)
        a2 += 1
    a6 = 1000000
    b11 = fonk8(sum_up, a6)
    fonk9(b11)
    b12 = fonk11()
    b13 = fonk13()
    if fonk14(b13, b12):
        print("You win!")
    else:
        print("Try again!")
    b14 = fonk15()
    a2 = fonk16(b14, b12)
    print(f"Worst case a2: {a2}")
    a2 = fonk17(b12)
    print(f"Random case a2: {a2}")