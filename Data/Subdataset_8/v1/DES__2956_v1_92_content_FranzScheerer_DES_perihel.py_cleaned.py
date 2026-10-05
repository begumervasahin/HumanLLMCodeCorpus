import math
def main():
    print("Die Periheldrehung eines schnellen Planeten")
    e = 0.1
    vy = 1.0 * (1.0 + e)
    vx = 0.0
    c = 100.0
    dt = 0.00001
    t_max = 30
    gamma = 1.0 / math.sqrt(1.0 - (vx * vx + vy * vy) / (c * c))
    px = vx * gamma
    py = vy * gamma
    x = (-1) * (1.0 - e)
    y = 0.0
    t = 0.0
    s0 = px * x + py * y
    y0 = y
    t0 = t
    while t < t_max:
        t += dt
        gamma = 1.0 / math.sqrt(1.0 - (vx * vx + vy * vy) / (c * c))
        r = math.sqrt(x * x + y * y)
        r3 = r * r * r
        px -= gamma * (x / r3) * dt
        py -= gamma * (y / r3) * dt
        vx = px / gamma
        vy = py / gamma
        x += vx * dt
        y += vy * dt
        omega = math.sqrt(vx * vx + vy * vy) / r
        if y0 * y < 0.0:
            print("y = 0 ", t)
            print("r = 0 ", math.sqrt(x * x + y * y))
            t0 = t
        if s0 * (px * x + py * y) < 0.0:
            print("s = 0 ", t, "relative Drehung ", omega * (t - t0) / t)
        s0 = px * x + py * y
        y0 = y
if __name__ == "__main__":
    main()