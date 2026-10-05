import math
from turtle import *
G = 6.67428e-11
AU = (149.6e6 * 1000)
SCALE =250/384400000
class Body(Turtle):
    name = 'Body'
    mass = None
    ax = ay = 0.0
    vx = vy = 0.0
    px = py = 0.0
    def attraction(self, other):
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)
        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))
        f = G * self.mass * other.mass / (d**2)
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy
def update_info(step, bodies):
    print('Step
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)
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
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)
def main():
    rock = Body()
    rock.name = 'rock'
    rock.mass = 10**25
    rock.px = 384400000
    rock.vy = -1200
    rock.pencolor('green')
    rock2 = Body()
    rock2.name = 'rock'
    rock2.mass = 10**25
    rock2.px = -384400000
    rock2.vy = 1200
    rock2.pencolor('green')
    rock3 = Body()
    rock3.name = 'rock'
    rock3.mass = 10**25
    rock3.py = 384400000
    rock3.vx = 1200
    rock3.pencolor('green')
    rock3a = Body()
    rock3a.name = 'rock'
    rock3a.mass = 10**25
    rock3a.py = 384400000+100000000
    rock3a.vx = 1200+2500
    rock3a.pencolor('green')
    rock4 = Body()
    rock4.name = 'rock'
    rock4.mass = 10**25
    rock4.py = -384400000
    rock4.vx = -1200
    rock4.pencolor('green')
    rock4a = Body()
    rock4a.name = 'rock'
    rock4a.mass = 10**22
    rock4a.py = -384400000-100000000
    rock4a.vx = -1200-2500
    rock4a.pencolor('green')
    rock40 = Body()
    rock40.name = 'rock'
    rock40.mass = 10**27
    rock40.py = 0
    rock40.vx = 0
    rock40.pencolor('green')
    rock41 = Body()
    rock41.name = 'rock'
    rock41.mass = 10**22
    rock41.py = -100000000
    rock41.vx = -2500
    rock41.pencolor('green')
    loop([rock, rock2, rock3, rock3a, rock4, rock4a, rock40, rock41])
if __name__ == '__main__':
    main()