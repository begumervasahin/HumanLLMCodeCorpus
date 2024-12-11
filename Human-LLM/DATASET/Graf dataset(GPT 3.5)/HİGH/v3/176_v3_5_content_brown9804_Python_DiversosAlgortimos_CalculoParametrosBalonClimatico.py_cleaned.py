def fonk1(time):
    b1 = -0.48 * (time ** 3) + 36 * (time ** 2) - 760 * time + 4100
    return b1
def fonk2(time):
    b2 = -0.12 * time ** 4 + 12 * time ** 3 - 380 * time ** 2 + 4100 * time + 220
    return b2
def fonk3(velocity_mph):
    b3 = velocity_mph / 3600
    return b3
def fonk4(b7, b8, b9):
    a1 = 0
    a2 = 0
    for hour in range(b7, b8 + 1, b9):
        b4 = fonk1(hour)
        b5 = fonk2(hour)
        b6 = fonk3(b4)
        if b5 > a1:
            a1 = b5
            a2 = hour
        print("{0:2}h   {1:8.2f}m       {2:3.2f}m/s".format(hour, b5, b6))
    print("The maximum b5 was reached at", a2, "hours.")
    print("The maximum b5 reached was", a1, "meters.")
b7 = int(input("Enter the initial time to calculate b4 and b5 for the weather balloon: "))
b8 = int(input("Enter the final time: "))
b9 = int(input("Enter the b9 in hours: "))
if 0 <= b7 < 48 and b7 < b8 <= 48:
    fonk4(b7, b8, b9)
else:
    print("Error: Initial time should be greater than or equal to 0 and less than 48.")
    print("Final time should be greater than initial time and less than or equal to 48.")