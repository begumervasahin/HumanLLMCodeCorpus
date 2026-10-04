from turtle import *
def fonk1(b1, a1):
    fonk2(b1, a1)
def fonk2(b1, a1):
    if b1 = = 0:
        forward(a1)
        return
    b1 -= 1
    a1 /= 1.41421
    right(45)
    fonk2(b1, a1)
    left(90)
    fonk3(b1, a1)
    right(45)
def fonk3(b1, a1):
    if b1 = = 0:
        forward(a1)
        return
    b1 -= 1
    a1 /= 1.41421
    left(45)
    fonk2(b1, a1)
    right(90)
    fonk3(b1, a1)
    left(45)
if b2 = = "__main__":
    speed(0)
    a1 = 200
    b1 = 10
    penup()
    goto(-a1 / 2, 0)
    pendown()
    fonk1(b1, a1)
    done()
