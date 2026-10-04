import math
import random
todayMinutes = 24 * 60
workingMinutes = float(input("How many hours will you work today?\n")) * 60
sleepingMinutes = float(input("How many hours will you sleep of today?\n")) * 60
eatingMinutes = float(input("How many hours will you spend eating today?\n")) * 60
drivingMinutes = float(input("How many hours will you spend driving today?\n")) * 60
cleaningMinutes = float(input("How many hours will you spend cleaning today?\n")) * 60
whatIsLeft = todayMinutes - (workingMinutes + sleepingMinutes + eatingMinutes +
                            drivingMinutes + cleaningMinutes)
artisticWindows = 45
articisticBreaks = 15
aWaB = 60
sessions = whatIsLeft
thoughtFul = whatIsLeft % 60
print(str(thoughtFul) + " Minutes available today to do something thoughtful for someone.")
print(str(sessions) + " Sessions available today for creating something!")