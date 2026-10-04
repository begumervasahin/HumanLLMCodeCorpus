import math
from turtle import *
a1 = 6.67428e-11
b1 = 149.6e6 * 1000
b2 = 250 / 384400000
class class1(Turtle):
    def fonk1(self, b3, b4, b5, b6, b7, b8, color):
        super().fonk1()
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.penup()
        self.hideturtle()
        self.pencolor(color)
        self.a2 = 0.0
        self.a3 = 0.0
    def fonk2(self, other):
        if self is other:
            raise ValueError(f"Attraction of object {self.b3} to itself requested")
        b9 = other.b5 - self.b5
        b10 = other.b6 - self.b6
        b11 = math.sqrt(b9**2 + b10**2)
        if b11 = = 0:
            raise ValueError(f"Collision between objects {self.b3} and {other.b3}")
        b12 = a1 * self.b4 * other.b4 / b11**2
        b13 = math.atan2(b10, b9)
        b14 = math.cos(b13) * b12
        b15 = math.sin(b13) * b12
        return b14, b15
def fonk3(a5, b18):
    print(f'Step {a5}')
    for body in b18:
        print(f'{body.b3:<8}  Pos.={body.b5 / b1:>6.2f} {body.b6 / b1:>6.2f} Vel.={body.b7:>10.3f} {body.b8:>10.3f}')
    print()
def fonk4(b18):
    a4 = 600
    a5 = 1
    while True:
        fonk3(a5, b18)
        a5 += 1
        b16 = {}
        for body in b18:
            total_fx, b17 = 0.0, 0.0
            for other in b18:
                if body is other:
                    continue
                b14, b15 = body.fonk2(other)
                total_fx += b14
                b17 += b15
            b16[body] = (total_fx, b17)
        for body in b18:
            b14, b15 = b16[body]
            body.b7 += b14 / body.b4 * a4
            body.b8 += b15 / body.b4 * a4
            body.b5 += body.b7 * a4
            body.b6 += body.b8 * a4
            body.goto(body.b5 * b2, body.b6 * b2)
            body.dot(3)
def fonk5():
    b18 = [
        class1('rock', 10**25, 384400000, 0, 0, -1200, 'green'),
        class1('rock2', 10**25, -384400000, 0, 0, 1200, 'green'),
        class1('rock3', 10**25, 0, 384400000, 1200, 0, 'green'),
        class1('rock3a', 10**25, 0, 484400000, 3700, 0, 'green'),
        class1('rock4', 10**25, 0, -384400000, -1200, 0, 'green'),
        class1('rock4a', 10**22, 0, -484400000, -3700, 0, 'green'),
        class1('rock40', 10**27, 0, 0, 0, 0, 'green'),
        class1('rock41', 10**22, 0, -100000000, -2500, 0, 'green')
    ]
    return b18
def fonk6():
    b18 = fonk5()
    fonk4(b18)
if b19 = = '__main__':
    fonk6()