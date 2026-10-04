from turtle import *
def fonk1(a2, a1):
    fonk2(a2, a1)
def fonk2(a2, a1):
    a2 -= 1
    a1 /= 1.41421
    if a2 > 0:
        right(45)
        fonk2(a2, a1)
        left(90)
        fonk3(a2, a1)
        right(45)
    else:
        right(45)
        forward(a1)
        left(90)
        forward(a1)
        right(45)
def fonk3(a2, a1):
    a2 -= 1
    a1 /= 1.41421
    if a2 > 0:
        left(45)
        fonk2(a2, a1)
        right(90)
        fonk3(a2, a1)
        left(45)
    else:
        left(45)
        forward(a1)
        right(90)
        forward(a1)
        left(45)
speed(0)
bgcolor('white')
color('blue')
pensize(2)
a1 = 200
a2 = 10
penup()
goto(-a1
pendown()
fonk1(a2, a1)
done()