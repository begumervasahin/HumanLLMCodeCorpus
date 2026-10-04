from turtle import *
def dragon_curve(steps, length):
    draw_curve_right(steps, length)
def draw_curve_right(steps, length):
    if steps == 0:
        forward(length)
        return
    steps -= 1
    length /= 1.41421
    right(45)
    draw_curve_right(steps, length)
    left(90)
    draw_curve_left(steps, length)
    right(45)
def draw_curve_left(steps, length):
    if steps == 0:
        forward(length)
        return
    steps -= 1
    length /= 1.41421
    left(45)
    draw_curve_right(steps, length)
    right(90)
    draw_curve_left(steps, length)
    left(45)
if __name__ == "__main__":
    speed(0)
    length = 200
    steps = 10
    penup()
    goto(-length / 2, 0)
    pendown()
    dragon_curve(steps, length)
    done()
