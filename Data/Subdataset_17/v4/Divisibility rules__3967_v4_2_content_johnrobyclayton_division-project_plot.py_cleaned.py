import math
from turtle import *
G = 6.67428e-11
AU = 149.6e6 * 1000
SCALE = 250 / 384400000
class Body(Turtle):
    def __init__(self, name, mass, px, py, vx, vy, color):
        super().__init__()
        self.name = name
        self.mass = mass
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.penup()
        self.hideturtle()
        self.pencolor(color)
        self.ax = 0.0
        self.ay = 0.0
    def attraction(self, other):
        if self is other:
            raise ValueError(f"Attraction of object {self.name} to itself requested")
        dx = other.px - self.px
        dy = other.py - self.py
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            raise ValueError(f"Collision between objects {self.name} and {other.name}")
        force = G * self.mass * other.mass / distance**2
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * force
        fy = math.sin(theta) * force
        return fx, fy
def update_info(step, bodies):
    print(f'Step {step}')
    for body in bodies:
        print(f'{body.name:<8}  Pos.={body.px / AU:>6.2f} {body.py / AU:>6.2f} Vel.={body.vx:>10.3f} {body.vy:>10.3f}')
    print()
def loop(bodies):
    timestep = 600
    step = 1
    while True:
        update_info(step, bodies)
        step += 1
        forces = {}
        for body in bodies:
            total_fx, total_fy = 0.0, 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy
            forces[body] = (total_fx, total_fy)
        for body in bodies:
            fx, fy = forces[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px * SCALE, body.py * SCALE)
            body.dot(3)
def create_bodies():
    bodies = [
        Body('rock', 10**25, 384400000, 0, 0, -1200, 'green'),
        Body('rock2', 10**25, -384400000, 0, 0, 1200, 'green'),
        Body('rock3', 10**25, 0, 384400000, 1200, 0, 'green'),
        Body('rock3a', 10**25, 0, 484400000, 3700, 0, 'green'),
        Body('rock4', 10**25, 0, -384400000, -1200, 0, 'green'),
        Body('rock4a', 10**22, 0, -484400000, -3700, 0, 'green'),
        Body('rock40', 10**27, 0, 0, 0, 0, 'green'),
        Body('rock41', 10**22, 0, -100000000, -2500, 0, 'green')
    ]
    return bodies
def main():
    bodies = create_bodies()
    loop(bodies)
if __name__ == '__main__':
    main()