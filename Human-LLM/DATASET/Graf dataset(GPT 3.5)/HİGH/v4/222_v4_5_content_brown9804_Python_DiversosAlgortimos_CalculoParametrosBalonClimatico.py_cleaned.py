def fonk1(t):
    b1 = -0.48 * (t ** 3) + 36 * (t ** 2) - 760 * t + 4100
    return b1
def fonk2(t):
    b2 = -0.12 * t ** 4 + 12 * t ** 3 - 380 * t ** 2 + 4100 * t + 220
    return b2
def fonk3(t):
    b3 = t / 3600
    return b3
def fonk4(b5, b6, b7):
    a1 = 0
    a2 = 0
    for hour in range(b5, b6 + 1, b7):
        b1 = fonk1(hour)
        b2 = fonk2(hour)
        b4 = fonk3(b1)
        if b2 > a1:
            a1 = b2
            a2 = hour
        print("{0:2}h   {1:8.2f}m       {2:3.2f}m/s".format(hour, b2, b4))
    print("The maximum altitude was reached at", a2, "hours.")
    print("The maximum altitude reached was", a1, "meters.")
b5 = int(input("Enter the initial time to calculate velocity and altitude for the weather balloon: "))
b6 = int(input("Enter the final time: "))
b7 = int(input("Enter the b7 in hours: "))
if 0 <= b5 < 48 and b5 < b6 <= 48:
    fonk4(b5, b6, b7)
else:
    print("Error: Initial time should be greater than or equal to 0 and less than 48.")
    print("Final time should be greater than initial time and less than or equal to 48.")