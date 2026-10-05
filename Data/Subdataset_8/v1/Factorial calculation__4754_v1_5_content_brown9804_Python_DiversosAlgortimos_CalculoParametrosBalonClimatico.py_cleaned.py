def velocity(t):
    vel = -0.48 * (t ** 3) + 36 * (t ** 2) - 760 * t + 4100
    return vel
def altitude(t):
    alt = -0.12 * t ** 4 + 12 * t ** 3 - 380 * t ** 2 + 4100 * t + 220
    return alt
def velocity_conversion(t):
    v = t / 3600
    return v
def process(initial_time, final_time, increment):
    max_altitude = 0
    max_altitude_time = 0
    for hour in range(initial_time, final_time + 1, increment):
        vel = velocity(hour)
        alt = altitude(hour)
        vel_conv = velocity_conversion(vel)
        if alt > max_altitude:
            max_altitude = alt
            max_altitude_time = hour
        print("{0:2}h   {1:8.2f}m       {2:3.2f}m/s".format(hour, alt, vel_conv))
    print("The maximum altitude was reached at", max_altitude_time, "hours.")
    print("The maximum altitude reached was", max_altitude, "meters.")
initial_time = int(input("Enter the initial time to calculate velocity and altitude for the weather balloon: "))
final_time = int(input("Enter the final time: "))
increment = int(input("Enter the increment in hours: "))
if 0 <= initial_time < 48 and initial_time < final_time <= 48:
    process(initial_time, final_time, increment)
else:
    print("Error: Initial time should be greater than or equal to 0 and less than 48.")
    print("Final time should be greater than initial time and less than or equal to 48.")