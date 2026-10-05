import math
import turtle
G = 6.67428e-11
AU = 149.6e6 * 1000
SCALE = 250 / 384400000
class Body(turtle.Turtle):
    name = 'Body'
    mass = None
    ax = ay = 0.0
    vx = vy = 0.0
    px = py = 0.0
    def attraction(self, other):
        if self is other:
            raise ValueError("Attraction of an object to itself is not allowed")
        dx = other.px - self.px
        dy = other.py - self.py
        d = math.sqrt(dx ** 2 + dy ** 2)
        if d == 0:
            raise ValueError("Collision between objects")
        f = G * self.mass * other.mass / (d ** 2)
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy
def update_info(step, bodies):
    print('Step:', step)
    for body in bodies:
        print(f"{body.name}: Position=({body.px / AU:.2f}, {body.py / AU:.2f}), Velocity=({body.vx:.3f}, {body.vy:.3f})")
    print()
def loop(bodies):
    timestep = 600
    for body in bodies:
        body.penup()
        body.hideturtle()
    step = 1
    while True:
        update_info(step, bodies)
        step += 1
        force = {}
        for body in bodies:
            total_fx = total_fy = 0.0
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
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.setworldcoordinates(-400, -300, 400, 300)
    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.972e24
    earth.px = 0
    earth.py = 0
    earth.vx = 0
    earth.vy = 0
    earth.pencolor('blue')
    moon = Body()
    moon.name = 'Moon'
    moon.mass = 7.34767309e22
    moon.px = 384400000
    moon.py = 0
    moon.vx = 0
    moon.vy = 1022
    moon.pencolor('gray')
    loop([earth, moon])
if __name__ == '__main__':
    main()