import math
import turtle
a1 = 6.67428e-11
b1 = 149.6e6 * 1000
b2 = 250 / 384400000
class class1(turtle.Turtle):
    b3 = 'class1'
    b4 = None
    b5 = ay = 0.0
    b6 = a5 = 0.0
    b7 = a4 = 0.0
    def fonk1(self, other):
        if self is other:
            raise ValueError("Attraction of an object to itself is not allowed")
        b8 = other.b7 - self.b7
        b9 = other.a4 - self.a4
        b10 = math.sqrt(b8 ** 2 + b9 ** 2)
        if b10 = = 0:
            raise ValueError("Collision between objects")
        b11 = a1 * self.b4 * other.b4 / (b10 ** 2)
        b12 = math.atan2(b9, b8)
        b13 = math.cos(b12) * b11
        b14 = math.sin(b12) * b11
        return b13, b14
def fonk2(a3, bodies):
    print('Step:', a3)
    for body in bodies:
        print(b11"{body.b3}: b15 = ({body.b7 / b1:.2f}, {body.a4 / b1:.2f}), Velocity=({body.b6:.3f}, {body.a5:.3f})")
    print()
def fonk3(bodies):
    a2 = 600
    for body in bodies:
        body.penup()
        body.hideturtle()
    a3 = 1
    while True:
        fonk2(a3, bodies)
        a3 += 1
        b16 = {}
        for body in bodies:
            b17 = total_fy = 0.0
            for other in bodies:
                if body is other:
                    continue
                b13, b14 = body.fonk1(other)
                b17 += b13
                total_fy += b14
            b16[body] = (b17, total_fy)
        for body in bodies:
            b13, b14 = b16[body]
            body.b6 += b13 / body.b4 * a2
            body.a5 += b14 / body.b4 * a2
            body.b7 += body.b6 * a2
            body.a4 += body.a5 * a2
            body.goto(body.b7 * b2, body.a4 * b2)
            body.dot(3)
def fonk4():
    b18 = turtle.Screen()
    b18.setup(b19 = 800, height=600)
    b18.setworldcoordinates(-400, -300, 400, 300)
    b20 = class1()
    b20.b3 = 'Earth'
    b20.b4 = 5.972e24
    b20.b7 = 0
    b20.a4 = 0
    b20.b6 = 0
    b20.a5 = 0
    b20.pencolor('blue')
    b21 = class1()
    b21.b3 = 'Moon'
    b21.b4 = 7.34767309e22
    b21.b7 = 384400000
    b21.a4 = 0
    b21.b6 = 0
    b21.a5 = 1022
    b21.pencolor('gray')
    fonk3([b20, b21])
if b22 = = '__main__':
    fonk4()