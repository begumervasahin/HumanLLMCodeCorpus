import sqlite3
import numpy as np
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = "delete from coursedata where {} or {} or {}"
b3 = b3.format(
    "b4 = -1",
    "b5 = -1",
    "b6 = -1"
)
b1.execute(b3)
b7 = pd.read_sql("select * from coursedata", con=b1)
def fonk1(b7):
    b8 = []
    b9 = b7["b4"]
    b10 = b7["b5"]
    b11 = b7["b6"]
    if b9.max() != b9.min():
        b12 = (b9.max() - b9.min()) / b9.std()
        b8.append((b12, "b4"))
    if b10.max() != b10.min():
        b13 = (b10.max() - b10.min()) / b10.std()
        b8.append((b13, "b5"))
    if b11.max() != b11.min():
        b14 = (b11.max() - b11.min()) / b11.std()
        b8.append((b14, "b6"))
    max_result, b15 = max(b8)
    return b15
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
def fonk3(b18):
    if b18 in ["1", "2", "3"]:
        return int(b18)
    else:
        return fonk3(input("Please enter 1, 2, or 3.\n"))
def fonk4(b7):
    b16 = fonk1(b7)
    b7.sort_values(b17 = b16, inplace=True)
    fonk2(
        b7.iloc[0],
        b7.iloc[round(len(b7)/2)],
        b7.iloc[-1]
    )
    print("Based on the dimension of " + b16.split("_")[1] + ",")
    b18 = fonk3(input("Do you prefer course 1, 2, or 3?\n"))
    b19 = round((b18-1) * len(b7)/3)
    b20 = round(b18 * len(b7)/3)
    return b7.iloc[b19:b20]
while len(b7) > 6:
    print("__________________________________________")
    b21 = fonk4(b7)
    print("Your top courses are: ")
    print(b21.head())
    print("There are {} courses remaining.".format(len(b21)))
    if len(b21) < 3:
        print("Stopping execution because there are too few courses.")
        break
    b7 = b21
b1.close()