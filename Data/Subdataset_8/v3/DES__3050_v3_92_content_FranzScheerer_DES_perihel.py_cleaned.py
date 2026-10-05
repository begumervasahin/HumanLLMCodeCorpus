import math
def perihelion_rotation():
    print("Die Periheldrehung eines schnellen Planeten")
    eccentricity = 0.1
    vy = 1.0 * (1.0 + eccentricity)
    vx = 0.0
    speed_of_light = 100.0
    time_step = 0.00001
    max_time = 30
    gamma = 1.0 / math.sqrt(1.0 - (vx * vx + vy * vy) / (speed_of_light * speed_of_light))
    px = vx * gamma
    py = vy * gamma
    x = (-1) * (1.0 - eccentricity)
    y = 0.0
    t = 0.0
    s0 = px * x + py * y
    y0 = y
    t0 = t
    while t < max_time:
        t += time_step
        gamma = 1.0 / math.sqrt(1.0 - (vx * vx + vy * vy) / (speed_of_light * speed_of_light))
        r = math.sqrt(x * x + y * y)
        r3 = r * r * r
        px -= gamma * (x / r3) * time_step
        py -= gamma * (y / r3) * time_step
        vx = px / gamma
        vy = py / gamma
        x += vx * time_step
        y += vy * time_step
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
    perihelion_rotation()