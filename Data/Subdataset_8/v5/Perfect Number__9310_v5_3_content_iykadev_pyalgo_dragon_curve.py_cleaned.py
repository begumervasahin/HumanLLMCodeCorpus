from turtle import *
def draw_dragon_curve(step, length):
    _draw_dragon_curve(step, length)
def _draw_dragon_curve(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        _turn_right(45)
        _draw_dragon_curve(step, length)
        _turn_left(90)
        _draw_dragon_curve_reverse(step, length)
        _turn_right(45)
    else:
        _turn_right(45)
        _move_forward(length)
        _turn_left(90)
        _move_forward(length)
        _turn_right(45)
def _draw_dragon_curve_reverse(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        _turn_left(45)
        _draw_dragon_curve(step, length)
        _turn_right(90)
        _draw_dragon_curve_reverse(step, length)
        _turn_left(45)
    else:
        _turn_left(45)
        _move_forward(length)
        _turn_right(90)
        _move_forward(length)
        _turn_left(45)
def _turn_left(angle):
    left(angle)
def _turn_right(angle):
    right(angle)
def _move_forward(distance):
    forward(distance)