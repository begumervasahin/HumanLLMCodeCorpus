import math
import turtle
a1 = 6.67428e-11
b1 = 149.6e6 * 1000
b2 = 250 / 384400000
class class1(turtle.Turtle):
    def fonk1(self, b3, b4, position, velocity, color):
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
            raise ValueError("Cannot attract itself")
        b7 = other.px - self.px
        b8 = other.b5 - self.b5
        b9 = math.sqrt(b7 ** 2 + b8 ** 2)
        if b9 = = 0:
            raise ValueError("Collision between objects")
        b10 = (a1 * self.b4 * other.b4) / (b9 ** 2)
        b11 = math.atan2(b8, b7)
        b12 = math.cos(b11) * b10
        b13 = math.sin(b11) * b10
        return b12, b13
def fonk3(a3, bodies):
    print('Step:', a3)
    for body in bodies:
        print(f"{body.b3}: b14 = ({body.px / b1:.2f}, {body.b5 / b1:.2f}), Velocity=({body.vx:.3f}, {body.b6:.3f})")
    print()
def fonk4(bodies):
    a2 = 600
    a3 = 1
    while True:
        fonk3(a3, bodies)
        a3 += 1
        b15 = {}
        for body in bodies:
            total_force_x, b16 = 0.0, 0.0
            for other in bodies:
                if body is other:
                    continue
                b12, b13 = body.fonk2(other)
                total_force_x += b12
                b16 += b13
            b15[body] = (total_force_x, b16)
        for body in bodies:
            b12, b13 = b15[body]
            b17 = b12 / body.b4
            b18 = b13 / body.b4
            body.vx += b17 * a2
            body.b6 += b18 * a2
            body.px += body.vx * a2
            body.b5 += body.b6 * a2
            body.goto(body.px * b2, body.b5 * b2)
            body.dot(3)
def fonk5():
    b19 = turtle.Screen()
    b19.setup(b20 = 800, height=600)
    b19.setworldcoordinates(-400, -300, 400, 300)
    b21 = class1('Earth', 5.972e24, (0, 0), (0, 0), 'blue')
    b22 = class1('Moon', 7.34767309e22, (384400000, 0), (0, 1022), 'gray')
    fonk4([b21, b22])
if b23 = = '__main__':
    fonk5()