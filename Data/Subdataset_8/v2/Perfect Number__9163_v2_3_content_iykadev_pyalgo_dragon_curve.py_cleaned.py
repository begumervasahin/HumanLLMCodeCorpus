from turtle import *
def draw_dragon_curve(step, length):
    draw_dragon_curve_right(step, length)
def draw_dragon_curve_right(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        right(45)
        draw_dragon_curve_right(step, length)
        left(90)
        draw_dragon_curve_left(step, length)
        right(45)
    else:
        right(45)
        forward(length)
        left(90)
        forward(length)
        right(45)
def draw_dragon_curve_left(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        left(45)
        draw_dragon_curve_right(step, length)
        right(90)
        draw_dragon_curve_left(step, length)
        left(45)
    else:
        left(45)
        forward(length)
        right(90)
        forward(length)
        left(45)
speed(0)
penup()
goto(-200, 0)
pendown()
draw_dragon_curve(12, 300)
done()