import sqlite3
import numpy as np
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = "DELETE FROM coursedata WHERE {} OR {} OR {}"
b3 = b3.format(
    "b4 = -1",
    "b5 = -1",
    "b6 = -1"
)
b1.execute(b3)
b7 = pd.read_sql("SELECT * FROM coursedata", con=b1)
def fonk1(b7):
    b8 = []
    for b12 in ["b4", "b5", "b6"]:
        b9 = b7[b12]
        if b9.max() != b9.min():
            b10 = (b9.max() - b9.min()) / b9.std()
            b8.append((b10, b12))
    max_result, b11 = max(b8)
    return b11
def fonk2(low, med, high):
    print("Here are three example courses:")
    print(low[1])
    print("\tLevel:\t\t{}".format(low[2]))
    print("\tCategory:\t{}".format(low[3]))
    print("\tEnrollment:\t{}".format(low[4]))
    print(med[1])
    print("\tLevel:\t\t{}".format(med[2]))
    print("\tCategory:\t{}".format(med[3]))
    print("\tEnrollment:\t{}".format(med[4]))
    print(high[1])
    print("\tLevel:\t\t{}".format(high[2]))
    print("\tCategory:\t{}".format(high[3]))
    print("\tEnrollment:\t{}".format(high[4]))
def fonk3(b14):
    if b14 in ["1", "2", "3"]:
        return int(b14)
    else:
        return fonk3(input("Please enter 1, 2, or 3.\n"))
def fonk4(b7):
    b12 = fonk1(b7)
    b7.sort_values(b13 = b12, inplace=True)
    fonk2(
        b7.iloc[0],
        b7.iloc[round(len(b7)/2)],
        b7.iloc[-1]
    )
    print("Based on the dimension of " + b12.split("_")[1] + ",")
    b14 = fonk3(input("Do you prefer course 1, 2, or 3?\n"))
    b15 = round((b14-1) * len(b7)/3)
    b16 = round(b14 * len(b7)/3)
    return b7.iloc[b15:b16]
while len(b7) > 6:
    print("__________________________________________")
    b17 = fonk4(b7)
    print("Your top courses are: ")
    print(b17.head())
    print("There are {} courses remaining.".format(len(b17)))
    if len(b17) < 3:
        print("Stopping execution because there are too few courses.")
        break
    b7 = b17
b1.close()