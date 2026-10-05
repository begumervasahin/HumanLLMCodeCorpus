import math
import turtle
a1 = 6.67428e-11
b1 = 149.6e6 * 1000
b2 = 250 / 384400000
class class1(turtle.Turtle):
    b3 = 'class1'
    b4 = None
    b5 = ay = 0.0
    b6 = a4 = 0.0
    b7 = py = 0.0
    def fonk1(self, other):
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.b3)
        sx, b8 = self.b7, self.py
        ox, b9 = other.b7, other.py
        b10 = ox - sx
        b11 = b9 - b8
        b12 = math.sqrt(b10 ** 2 + b11 ** 2)
        if b12 = = 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.b3, other.b3))
        b13 = a1 * self.b4 * other.b4 / (b12 ** 2)
        b14 = math.atan2(b11, b10)
        b15 = math.cos(b14) * b13
        b16 = math.sin(b14) * b13
        return b15, b16
def fonk2(a3, bodies):
    print('Step:', a3)
    for body in bodies:
        b17 = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.b3, body.b7 / b1, body.py / b1, body.b6, body.a4)
        print(b17)
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
        b18 = {}
        for body in bodies:
            b19 = total_fy = 0.0
            for other in bodies:
                if body is other:
                    continue
                b15, b16 = body.fonk1(other)
                b19 += b15
                total_fy += b16
            b18[body] = (b19, total_fy)
        for body in bodies:
            b15, b16 = b18[body]
            body.b6 += b15 / body.b4 * a2
            body.a4 += b16 / body.b4 * a2
            body.b7 += body.b6 * a2
            body.py += body.a4 * a2
            body.goto(body.b7 * b2, body.py * b2)
            body.dot(3)
def fonk4():
    b20 = turtle.Screen()
    b20.setup(b21 = 800, height=600)
    b20.setworldcoordinates(-400, -300, 400, 300)
    b22 = class1()
    b22.b3 = 'b22'
    b22.b4 = 10 ** 25
    b22.b7 = 384400000
    b22.a4 = -1200
    b22.pencolor('green')
    b23 = class1()
    b23.b3 = 'b22'
    b23.b4 = 10 ** 25
    b23.b7 = -384400000
    b23.a4 = 1200
    b23.pencolor('green')
    fonk3([b22, b23])
if b24 = = '__main__':
    fonk4()