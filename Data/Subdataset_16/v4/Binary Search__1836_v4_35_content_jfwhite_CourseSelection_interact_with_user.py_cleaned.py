import sqlite3
import numpy as np
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = b1.execute(b3)
b4 = pd.read_sql("SELECT * FROM coursedata", con=b1)
def fonk1(b4):
    b5 = []
    b6 = ["course_level", "course_category", "course_enrollment"]
    for col in b6:
        b7 = b4[col]
        if b7.max() != b7.min():
            b8 = (b7.max() - b7.min()) / b7.std()
            b5.append((b8, col))
    max_result, b9 = max(b5, key=lambda x: x[0])
    return b9
def fonk2(low, med, high):
    print("Here are three example courses:")
    for course in [low, med, high]:
        print(course[1])
        print(f"\tLevel:\t\t{course[2]}")
        print(f"\tCategory:\t{course[3]}")
        print(f"\tEnrollment:\t{course[4]}")
def fonk3(b12):
    if b12 in ["1", "2", "3"]:
        return int(b12)
    else:
        return fonk3(input("Please enter 1, 2, or 3.\n"))
def fonk4(b4):
    b10 = fonk1(b4)
    b4.sort_values(b11 = b10, inplace=True)
    fonk2(
        b4.iloc[0],
        b4.iloc[len(b4)
        b4.iloc[-1]
    )
    print(f"Based on the dimension of {b10.split('_')[1]},")
    b12 = fonk3(input("Do you prefer course 1, 2, or 3?\n"))
    b13 = (b12 - 1) * len(b4)
    b14 = b12 * len(b4)
    return b4.iloc[b13:b14]
while len(b4) > 6:
    print("__________________________________________")
    b4 = fonk4(b4)
    print("Your top courses are: ")
    print(b4.head())
    print(f"There are {len(b4)} courses remaining.")
    if len(b4) < 3:
        print("Stopping execution because there are too few courses.")
        break
b1.close()