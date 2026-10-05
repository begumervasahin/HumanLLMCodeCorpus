import math
from turtle import *
GRAVITATIONAL_CONSTANT = 6.67428e-11
ASTRONOMICAL_UNIT = 149.6e6 * 1000
SCALE = 250 / 384400000
class Body(Turtle):
    def __init__(self, name='', mass=None, position=(0.0, 0.0), velocity=(0.0, 0.0), color='black'):
        super().__init__()
        self.name = name
        self.mass = mass
        self.px, self.py = position
        self.vx, self.vy = velocity
        self.color(color)
        self.penup()
        self.hideturtle()
    def attraction(self, other):
        if self is other:
            raise ValueError("Attraction of object %r to itself requested" % self.name)
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx, dy = ox - sx, oy - sy
        d = math.sqrt(dx ** 2 + dy ** 2)
        if d == 0:
            raise ValueError("Collision between objects %r and %r" % (self.name, other.name))
        f = GRAVITATIONAL_CONSTANT * self.mass * other.mass / (d ** 2)
        theta = math.atan2(dy, dx)
        fx, fy = math.cos(theta) * f, math.sin(theta) * f
        return fx, fy
def display_info(step, bodies):
    print('Step:', step)
    for body in bodies:
        pos_x = body.px / ASTRONOMICAL_UNIT
        pos_y = body.py / ASTRONOMICAL_UNIT
        vel_x, vel_y = body.vx, body.vy
        print(f"{body.name:<8}  Pos.={pos_x:>6.2f} {pos_y:>6.2f} Vel.={vel_x:>10.3f} {vel_y:>10.3f}")
    print()
def simulate(bodies):
    timestep = 600
    for body in bodies:
        body.penup()
        body.hideturtle()
    step = 1
    while True:
        display_info(step, bodies)
        step += 1
        force = {}
        for body in bodies:
            total_fx, total_fy = 0.0, 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy
            force[body] = (total_fx, total_fy)
        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px * SCALE, body.py * SCALE)
            body.dot(3)
def main():
    rock = Body(name='rock', mass=10 ** 25, position=(384400000, 0), velocity=(0, -1200), color='green')
    rock2 = Body(name='rock', mass=10 ** 25, position=(-384400000, 0), velocity=(0, 1200), color='green')
    simulate([rock, rock2])
if __name__ == '__main__':
    main()