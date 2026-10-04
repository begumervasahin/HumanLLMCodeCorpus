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
        right(45)
        forward(length)
        left(90)
        forward(length)
        right(45)
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
        left(45)
        forward(length)
        right(90)
        forward(length)
        left(45)