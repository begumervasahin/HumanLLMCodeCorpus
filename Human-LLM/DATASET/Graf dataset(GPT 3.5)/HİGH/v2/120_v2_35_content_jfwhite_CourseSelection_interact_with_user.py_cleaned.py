import sqlite3
import numpy as np
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.b2()
b3 = b2.execute(b3)
b1.commit()
b4 = pd.read_sql("SELECT * FROM coursedata", con=b1)
def fonk1(b4):
    b5 = []
    for col in ["course_level", "course_category", "course_enrollment"]:
        b6 = b4[col]
        if b6.max() != b6.min():
            b7 = (b6.max() - b6.min()) / b6.std()
            b5.append((b7, col))
    max_variation, b8 = max(b5)
    return b8
def fonk2(low, medium, high):
    print("Here are three example courses:")
    print(low[1])
    print("\tLevel:\t\t{}".format(low[2]))
    print("\tCategory:\t{}".format(low[3]))
    print("\tEnrollment:\t{}".format(low[4]))
    print(medium[1])
    print("\tLevel:\t\t{}".format(medium[2]))
    print("\tCategory:\t{}".format(medium[3]))
    print("\tEnrollment:\t{}".format(medium[4]))
    print(high[1])
    print("\tLevel:\t\t{}".format(high[2]))
    print("\tCategory:\t{}".format(high[3]))
    print("\tEnrollment:\t{}".format(high[4]))
def fonk3():
    b9 = input("Do you prefer course 1, 2, or 3?\n")
    if b9 in ["1", "2", "3"]:
        return int(b9)
    else:
        print("Please enter 1, 2, or 3.")
        return fonk3()
def fonk4(b4):
    b6 = fonk1(b4)
    b4.sort_values(b10 = b6, inplace=True)
    fonk2(
        b4.iloc[0],
        b4.iloc[round(len(b4)/2)],
        b4.iloc[-1]
    )
    print(f"Based on the b6 of {b6.split('_')[1]},")
    b9 = fonk3()
    b11 = round((b9-1) * len(b4)/3)
    b12 = round(b9 * len(b4)/3)
    return b4.iloc[b11:b12]
while len(b4) > 6:
    print("__________________________________________")
    b13 = fonk4(b4)
    print("Your top courses are: ")
    print(b13.head())
    print(f"There are {len(b13)} courses remaining.")
    if len(b13) < 3:
        print("Stopping execution because there are too few courses.")
        break
    b4 = b13
b1.close()