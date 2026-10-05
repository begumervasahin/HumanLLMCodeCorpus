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
        fonk4(length, 45)
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
        fonk4(length, -45)
def fonk4(length, angle):
    setheading(angle)
    forward(length)
speed(0)
penup()
goto(-200, 0)
pendown()
fonk1(12, 300)
done()