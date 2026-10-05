import math
import turtle
GRAVITATIONAL_CONSTANT = 6.67428e-11
ASTRONOMICAL_UNIT = 149.6e6 * 1000
SCALE_FACTOR = 250 / 384400000
class CelestialBody(turtle.Turtle):
    def __init__(self, name, mass, position, velocity, color):
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
            raise ValueError("Cannot attract itself")
        dx = other.px - self.px
        dy = other.py - self.py
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            raise ValueError("Collision between objects")
        force = (GRAVITATIONAL_CONSTANT * self.mass * other.mass) / (distance ** 2)
        angle = math.atan2(dy, dx)
        force_x = math.cos(angle) * force
        force_y = math.sin(angle) * force
        return force_x, force_y
def display_info(step, bodies):
    print('Step:', step)
    for body in bodies:
        print(f"{body.name}: Position=({body.px / ASTRONOMICAL_UNIT:.2f}, {body.py / ASTRONOMICAL_UNIT:.2f}), Velocity=({body.vx:.3f}, {body.vy:.3f})")
    print()
def simulate(bodies):
    timestep = 600
    step = 1
    while True:
        display_info(step, bodies)
        step += 1
        forces = {}
        for body in bodies:
            total_force_x, total_force_y = 0.0, 0.0
            for other in bodies:
                if body is other:
                    continue
                force_x, force_y = body.attraction(other)
                total_force_x += force_x
                total_force_y += force_y
            forces[body] = (total_force_x, total_force_y)
        for body in bodies:
            force_x, force_y = forces[body]
            acceleration_x = force_x / body.mass
            acceleration_y = force_y / body.mass
            body.vx += acceleration_x * timestep
            body.vy += acceleration_y * timestep
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px * SCALE_FACTOR, body.py * SCALE_FACTOR)
            body.dot(3)
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.setworldcoordinates(-400, -300, 400, 300)
    earth = CelestialBody('Earth', 5.972e24, (0, 0), (0, 0), 'blue')
    moon = CelestialBody('Moon', 7.34767309e22, (384400000, 0), (0, 1022), 'gray')
    simulate([earth, moon])
if __name__ == '__main__':
    main()