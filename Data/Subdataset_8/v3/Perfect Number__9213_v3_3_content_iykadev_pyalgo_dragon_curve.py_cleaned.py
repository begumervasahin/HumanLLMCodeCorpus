from turtle import *
def draw_dragon_curve(step, length):
    _draw_dragon_curve_right(step, length)
def _draw_dragon_curve_right(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        right(45)
        _draw_dragon_curve_right(step, length)
        left(90)
        _draw_dragon_curve_left(step, length)
        right(45)
    else:
        _draw_line(length, 45)
def _draw_dragon_curve_left(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        left(45)
        _draw_dragon_curve_right(step, length)
        right(90)
        _draw_dragon_curve_left(step, length)
        left(45)
    else:
        _draw_line(length, -45)
def _draw_line(length, angle):
    setheading(angle)
    forward(length)
speed(0)
penup()
goto(-200, 0)
pendown()
draw_dragon_curve(12, 300)
done()