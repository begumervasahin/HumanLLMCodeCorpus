def calculate_velocity(time):
    velocity = -0.48 * (time ** 3) + 36 * (time ** 2) - 760 * time + 4100
    return velocity
def calculate_altitude(time):
    altitude = -0.12 * time ** 4 + 12 * time ** 3 - 380 * time ** 2 + 4100 * time + 220
    return altitude
def convert_velocity(velocity_mph):
    velocity_mps = velocity_mph / 3600
    return velocity_mps
def process(initial_time, final_time, increment):
    max_altitude = 0
    hour_of_max_altitude = 0
    for hour in range(initial_time, final_time + 1, increment):
        velocity = calculate_velocity(hour)
        altitude = calculate_altitude(hour)
        velocity_converted = convert_velocity(velocity)
        if altitude > max_altitude:
            max_altitude = altitude
            hour_of_max_altitude = hour
        print("{0:2}h   {1:8.2f}m       {2:3.2f}m/s".format(hour, altitude, velocity_converted))
    print("The maximum altitude was reached at", hour_of_max_altitude, "hours.")
    print("The maximum altitude reached was", max_altitude, "meters.")
initial_time = int(input("Enter the initial time to calculate velocity and altitude for the weather balloon: "))
final_time = int(input("Enter the final time: "))
increment = int(input("Enter the increment in hours: "))
if 0 <= initial_time < 48 and initial_time < final_time <= 48:
    process(initial_time, final_time, increment)
else:
    print("Error: Initial time should be greater than or equal to 0 and less than 48.")
    print("Final time should be greater than initial time and less than or equal to 48.")