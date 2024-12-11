import math
from turtle import *
a1 = 6.67428e-11
b1 = 149.6e6 * 1000
b2 = 250 / 384400000
class class1(Turtle):
    def fonk1(self, b3 = '', b4=None, position=(0.0, 0.0), velocity=(0.0, 0.0), color='black'):
        super().fonk1()
        self.b3 = b3
        self.b4 = b4
        self.px, self.b5 = position
        self.vx, self.b6 = velocity
        self.color(color)
        self.penup()
        self.hideturtle()
    def fonk2(self, other):
        if self is other:
            raise ValueError("Attraction of object %r to itself requested" % self.b3)
        sx, b7 = self.px, self.b5
        ox, b8 = other.px, other.b5
        dx, b9 = ox - sx, b8 - b7
        b10 = math.sqrt(dx ** 2 + b9 ** 2)
        if b10 = = 0:
            raise ValueError("Collision between objects %r and %r" % (self.b3, other.b3))
        b11 = a1 * self.b4 * other.b4 / (b10 ** 2)
        b12 = math.atan2(b9, dx)
        fx, b13 = math.cos(b12) * b11, math.sin(b12) * b11
        return fx, b13
def fonk3(a3, bodies):
    print('Step:', a3)
    for body in bodies:
        b14 = body.px / b1
        b15 = body.b5 / b1
        vel_x, b16 = body.vx, body.b6
        print(b11"{body.b3:<8}  Pos.={b14:>6.2f} {b15:>6.2f} Vel.={vel_x:>10.3f} {b16:>10.3f}")
    print()
def fonk4(bodies):
    a2 = 600
    for body in bodies:
        body.penup()
        body.hideturtle()
    a3 = 1
    while True:
        fonk3(a3, bodies)
        a3 += 1
        b17 = {}
        for body in bodies:
            total_fx, b18 = 0.0, 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, b13 = body.fonk2(other)
                total_fx += fx
                b18 += b13
            b17[body] = (total_fx, b18)
        for body in bodies:
            fx, b13 = b17[body]
            body.vx += fx / body.b4 * a2
            body.b6 += b13 / body.b4 * a2
            body.px += body.vx * a2
            body.b5 += body.b6 * a2
            body.goto(body.px * b2, body.b5 * b2)
            body.dot(3)
def fonk5():
    b19 = class1(b3='b19', b4=10 ** 25, position=(384400000, 0), velocity=(0, -1200), color='green')
    b20 = class1(b3='b19', b4=10 ** 25, position=(-384400000, 0), velocity=(0, 1200), color='green')
    fonk4([b19, b20])
if b21 = = '__main__':
    fonk5()