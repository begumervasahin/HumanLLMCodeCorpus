from turtle import *
def fonk1(step, length):
    fonk2(step, length)
def fonk2(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        fonk5(45)
        fonk2(step, length)
        fonk4(90)
        fonk3(step, length)
        fonk5(45)
    else:
        fonk5(45)
        fonk6(length)
        fonk4(90)
        fonk6(length)
        fonk5(45)
def fonk3(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        fonk4(45)
        fonk2(step, length)
        fonk5(90)
        fonk3(step, length)
        fonk4(45)
    else:
        fonk4(45)
        fonk6(length)
        fonk5(90)
        fonk6(length)
        fonk4(45)
def fonk4(angle):
    left(angle)
def fonk5(angle):
    right(angle)
def fonk6(distance):
    forward(distance)