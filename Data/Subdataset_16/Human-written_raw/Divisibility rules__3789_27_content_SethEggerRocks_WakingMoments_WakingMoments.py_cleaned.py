import math
import random
b1 = 24 * 60
b2 = float(input("How many hours will you work today?\n")) * 60
b3 = float(input("How many hours will you sleep of today?\n")) * 60
b4 = float(input("How many hours will you spend eating today?\n")) * 60
b5 = float(input("How many hours will you spend driving today?\n")) * 60
b6 = float(input("How many hours will you spend cleaning today?\n")) * 60
b7 = b1 - (b2 + b3 + b4 +
                            b5 + b6)
a1 = 45
a2 = 15
a3 = 60
b8 = b7
b9 = b7 % 60
print(str(b9) + " Minutes available today to do something thoughtful for someone.")
print(str(b8) + " Sessions available today for creating something!")