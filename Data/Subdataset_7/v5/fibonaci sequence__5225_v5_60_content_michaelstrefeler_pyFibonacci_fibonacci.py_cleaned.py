from turtle import *
def fonk1():
    b1 = input('Choose the number of Fibonacci sequence elements (min 5): ')
    while not b1.isdecimal() or int(b1) < 5:
        b1 = input('Please enter a number greater than or equal to 5: ')
    return int(b1)
def fonk2(b6):
    b2 = [0, 1]
    while len(b2) < b6:
        b3 = b2[-1] + b2[-2]
        b2.append(b3)
    return b2
def fonk3(sequence):
    for index, number in enumerate(sequence):
        print(f'Fibonacci {index}: {number}')
def fonk4(sequence):
    penup()
    goto(135.00, -20.00)
    pendown()
    b4 = True
    for b5 in sequence:
        if b5 = = 0:
            continue
        elif b5 = = 1:
            if b4:
                forward(12.5)
                write(b5)
                forward(12.5)
                for _ in range(3):
                    left(90)
                    forward(25)
                b4 = False
            else:
                for _ in range(2):
                    forward(25)
                forward(12.5)
                write(b5)
                forward(12.5)
                for _ in range(3):
                    left(90)
                    forward(25)
        else:
            for _ in range(2):
                forward(12.5 * b5)
                left(90)
            forward(12.5)
            write(b5)
            forward(12.5)
            left(90)
def fonk5(sequence):
    penup()
    goto(135.00, 5.00)
    pendown()
    color('red')
    shape('turtle')
    pensize(2)
    setheading(180)
    for i in range(len(sequence)):
        if i < 9:
            circle(12.5 * sequence[i], 90)
        else:
            break
def fonk6():
    b6 = fonk1()
    b2 = fonk2(b6)
    fonk3(b2)
    fonk4(b2)
    fonk5(b2)
    done()
if b7 = = "__main__":
    fonk6()