import sqlite3
import numpy as np
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = b2.execute(b3)
b1.commit()
b4 = pd.read_sql("SELECT * FROM coursedata", con=b1)
def fonk1(b4):
    b5 = []
    for b10 in ["course_level", "course_category", "course_enrollment"]:
        b6 = b4[b10]
        if b6.max() != b6.min():
            b7 = (b6.max() - b6.min()) / b6.std()
            b5.append((b7, b10))
    max_variation, b8 = max(b5)
    return b8
def fonk2(low, med, high):
    print("Here are three example courses:")
    fonk3(low)
    fonk3(med)
    fonk3(high)
def fonk3(course):
    print(course[1])
    print(f"\tLevel:\t\t{course[2]}")
    print(f"\tCategory:\t{course[3]}")
    print(f"\tEnrollment:\t{course[4]}")
def fonk4():
    b9 = input("Do you prefer course 1, 2, or 3?\n")
    if b9 in ["1", "2", "3"]:
        return int(b9)
    else:
        print("Please enter 1, 2, or 3.")
        return fonk4()
def fonk5(b4):
    b10 = fonk1(b4)
    b4.sort_values(b11 = b10, inplace=True)
    fonk2(
        b4.iloc[0],
        b4.iloc[round(len(b4)/2)],
        b4.iloc[-1]
    )
    print(f"Based on the dimension of {b10.split('_')[1]},")
    b9 = fonk4()
    b12 = round((b9-1) * len(b4)/3)
    b13 = round(b9 * len(b4)/3)
    return b4.iloc[b12:b13]
while len(b4) > 6:
    print("__________________________________________")
    b14 = fonk5(b4)
    print("Your top courses are: ")
    print(b14.head())
    print(f"There are {len(b14)} courses remaining.")
    if len(b14) < 3:
        print("Stopping execution because there are too few courses.")
        break
    b4 = b14
b1.close()