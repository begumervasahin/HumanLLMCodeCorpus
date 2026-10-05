from turtle import *
def dragon(step, length):
    dragon_curve(step, length)
def dragon_curve(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        right(45)
        dragon_curve(step, length)
        left(90)
        dragon_curve_reverse(step, length)
        right(45)
    else:
        right(45)
        forward(length)
        left(90)
        forward(length)
        right(45)
def dragon_curve_reverse(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        left(45)
        dragon_curve(step, length)
        right(90)
        dragon_curve_reverse(step, length)
        left(45)
    else:
        left(45)
        forward(length)
        right(90)
        forward(length)
        left(45)