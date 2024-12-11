import math
b1 = 24 * 60
b2 = float(input("How many hours will you work today?\n"))
b3 = float(input("How many hours will you sleep today?\n"))
b4 = float(input("How many hours will you spend eating today?\n"))
b5 = float(input("How many hours will you spend driving today?\n"))
b6 = float(input("How many hours will you spend cleaning today?\n"))
b7 = b2 * 60
b8 = b3 * 60
b9 = b4 * 60
b10 = b5 * 60
b11 = b6 * 60
b12 = (
    b7 + b8 + b9 +
    b10 + b11
)
b13 = b1 - b12
a1 = 45
a2 = 15
b14 = b13
b15 = b13 % 60
print(f"{b15} minutes available today to do something thoughtful for someone.")
print(f"{b14} b14 available today for creating something!")