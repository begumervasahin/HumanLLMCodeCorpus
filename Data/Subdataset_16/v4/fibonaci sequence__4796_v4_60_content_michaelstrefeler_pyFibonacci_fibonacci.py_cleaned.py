from turtle import *
def fonk1(n):
    b1 = [0, 1]
    for i in range(2, n):
        b1.append(b1[-1] + b1[-2])
    return b1
def fonk2(size, b2):
    forward(25 * size)
    write(b2)
    forward(25 * size)
    left(90)
    for _ in range(3):
        forward(25 * size)
        left(90)
def fonk3(b1):
    penup()
    goto(135, -20)
    pendown()
    for b2 in b1:
        if b2 = = 0:
            continue
        if b2 = = 1:
            forward(25 * b2 / 2)
            write(b2)
            forward(25 * b2 / 2)
        else:
            fonk2(b2, b2)
        left(90)
    penup()
    goto(135, 5)
    pendown()
    color('red')
    shape('turtle')
    pensize(2)
    setheading(180)
    for b2 in b1:
        if b2 < 9:
            circle(25 * b2, 90)
        else:
            break
    done()
def fonk4():
    while True:
        b3 = input('Choose up to which number of the Fibonacci b1 you want to go up to (min 5): ')
        if b3.isdecimal() and int(b3) >= 5:
            b3 = int(b3)
            break
        print('Please enter a number greater than or equal to 5.')
    b4 = fonk1(b3)
    for index, number in enumerate(b4):
        print(f'F°{index}: {number}')
    fonk3(b4)
if b5 = = "__main__":
    fonk4()