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
            if b2:
                fonk3(b3)
                b2 = False
            else:
                fonk3(b3)
        elif b3 = = 21:
            fonk4(b3)
            break
        else:
            fonk5(b3)
    fonk8(b1)
    done()
def fonk3(b3):
    forward(25 * b3 / 2)
    write(b3)
    forward(25 * b3 / 2)
    left(90)
    forward(25 * b3)
    left(90)
    forward(25 * b3)
    left(90)
    forward(25 * b3)
    left(90)
def fonk4(b3):
    forward(25 * b3)
    left(90)
    forward(25 * b3)
    left(90)
    forward(25 * b3 / 2)
    write(b3)
    forward(25 * b3 / 2)
    left(90)
def fonk5(b3):
    if b3 in [2, 13]:
        fonk6(b3, "left")
    elif b3 = = 3:
        fonk6(b3, "bottom")
    elif b3 = = 5:
        fonk6(b3, "top")
    else:
        fonk7(b3)
def fonk6(b3, b4):
    forward(25 * b3)
    left(90)
    forward(25 * b3)
    left(90)
    if b4 = = "left":
        forward(25 * b3)
        left(90)
        forward(25 * b3 / 2)
    elif b4 = = "bottom":
        forward(25 * b3 / 2)
        left(90)
        forward(25 * b3)
    elif b4 = = "top":
        forward(25 * b3 / 2)
    write(b3)
    forward(25 * b3 / 2)
    left(90)
def fonk7(b3):
    forward(25 * b3 / 2)
    write(b3)
    forward(25 * b3 / 2)
    left(90)
    forward(25 * b3)
    left(90)
    forward(25 * b3)
    left(90)
    forward(25 * b3)
    left(90)
def fonk8(b1):
    penup()
    goto(135, 5)
    pendown()
    color('red')
    shape('turtle')
    pensize(2)
    setheading(180)
    for i in range(len(b1)):
        if i < 9:
            circle(25 * b1[i], 90)
        else:
            break
def fonk9():
    b5 = input('Choose up to which number of the Fibonacci b1 you want to go up to: ')
    while not b5.isdecimal() or int(b5) < 5:
        b5 = input('Please write a number bigger than 4: ')
    b5 = int(b5)
    b6 = fonk1(b5)
    for index, number in enumerate(b6):
        print(f'F°{index}: {number}')
    fonk2(b6)
if b7 = = "__main__":
    fonk9()