from turtle import *
def fonk1(n):
    b1 = [0, 1]
    while len(b1) < n:
        b1.append(b1[-1] + b1[-2])
    return b1
def fonk2(b1):
    penup()
    goto(135, -20)
    pendown()
    b2 = True
    for b3 in b1:
        if b3 = = 0:
            continue
        if b3 = = 1:
            fonk3(b3, b2)
            b2 = False
        else:
            fonk4(b3)
    fonk5(b1)
    done()
def fonk3(b3, b2):
    if b2:
        forward(25 * b3 / 2)
    else:
        forward(25 * b3)
    write(b3)
    forward(25 * b3 / 2)
    left(90)
    for _ in range(3):
        forward(25 * b3)
        left(90)
def fonk4(b3):
    forward(25 * b3 / 2)
    write(b3)
    forward(25 * b3 / 2)
    left(90)
    for _ in range(3):
        forward(25 * b3)
        left(90)
def fonk5(b1):
    penup()
    goto(135, 5)
    pendown()
    color('red')
    shape('turtle')
    pensize(2)
    setheading(180)
    for b3 in b1:
        if b3 < 9:
            circle(25 * b3, 90)
        else:
            break
def fonk6():
    while True:
        b4 = input('Choose up to which number of the Fibonacci b1 you want to go up to (min 5): ')
        if b4.isdecimal() and int(b4) >= 5:
            return int(b4)
        print('Please enter a number greater than or equal to 5.')
def fonk7():
    b4 = fonk6()
    b5 = fonk1(b4)
    for index, number in enumerate(b5):
        print(f'F°{index}: {number}')
    fonk2(b5)
if b6 = = "__main__":
    fonk7()