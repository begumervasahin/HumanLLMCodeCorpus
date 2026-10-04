from turtle import *
def fonk1(step, length):
    fonk2(step, length)
def fonk2(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        right(45)
        fonk2(step, length)
        left(90)
        fonk3(step, length)
        right(45)
    else:
        fonk4(length, b1 = 'right')
def fonk3(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        left(45)
        fonk2(step, length)
        right(90)
        fonk3(step, length)
        left(45)
    else:
        fonk4(length, b1 = 'left')
def fonk4(length, b1):
    if b1 = = 'right':
        right(45)
        forward(length)
        left(90)
        forward(length)
        right(45)
    elif b1 = = 'left':
        left(45)
        forward(length)
        right(90)
        forward(length)
        left(45)
def fonk5():
    speed(0)
    bgcolor('white')
    color('blue')
    pensize(2)
def fonk6():
    a1 = 200
    a2 = 10
    fonk5()
    penup()
    goto(-a1
    pendown()
    fonk1(a2, a1)
    done()
if b2 = = "__main__":
    fonk6()