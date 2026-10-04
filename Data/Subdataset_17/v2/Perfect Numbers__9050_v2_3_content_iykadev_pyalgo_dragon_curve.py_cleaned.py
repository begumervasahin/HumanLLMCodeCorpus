from turtle import *
def dragon_curve(step, length):
    draw_curve_right(step, length)
def draw_curve_right(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        right(45)
        draw_curve_right(step, length)
        left(90)
        draw_curve_left(step, length)
        right(45)
    else:
        right(45)
        forward(length)
        left(90)
        forward(length)
        right(45)
def draw_curve_left(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        left(45)
        draw_curve_right(step, length)
        right(90)
        draw_curve_left(step, length)
        left(45)
    else:
        left(45)
        forward(length)
        right(90)
        forward(length)
        left(45)
speed(0)
bgcolor('white')
color('blue')
pensize(2)
initial_length = 200
iterations = 10
penup()
goto(-initial_length
pendown()
dragon_curve(iterations, initial_length)
done()