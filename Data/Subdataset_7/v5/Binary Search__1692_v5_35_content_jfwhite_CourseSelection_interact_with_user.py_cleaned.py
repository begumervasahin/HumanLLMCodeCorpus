import sqlite3
import numpy as np
import pandas as pd
def fonk1(db_name):
    b1 = sqlite3.connect(db_name)
    return b1
def fonk2(cursor):
    b2 = cursor.execute(b2)
def fonk3(b1):
    b3 = pd.read_sql("SELECT * FROM coursedata", con=b1)
    return b3
def fonk4(b3):
    b4 = []
    for b9 in ["course_level", "course_category", "course_enrollment"]:
        b5 = b3[b9]
        if b5.max() != b5.min():
            b6 = (b5.max() - b5.min()) / b5.std()
            b4.append((b6, b9))
    max_variation, b7 = max(b4)
    return b7
def fonk5(low, med, high):
    print("Here are three example courses:")
    fonk6(low)
    fonk6(med)
    fonk6(high)
def fonk6(course):
    print(course[1])
    print(f"\tLevel:\t\t{course[2]}")
    print(f"\tCategory:\t{course[3]}")
    print(f"\tEnrollment:\t{course[4]}")
def fonk7():
    b8 = input("Do you prefer course 1, 2, or 3?\n")
    if b8 in ["1", "2", "3"]:
        return int(b8)
    else:
        print("Please enter 1, 2, or 3.")
        return fonk7()
def fonk8(b3):
    b9 = fonk4(b3)
    b3.sort_values(b10 = b9, inplace=True)
    fonk5(
        b3.iloc[0],
        b3.iloc[round(len(b3)/2)],
        b3.iloc[-1]
    )
    print(f"Based on the dimension of {b9.split('_')[1]},")
    b8 = fonk7()
    b11 = round((b8-1) * len(b3)/3)
    b12 = round(b8 * len(b3)/3)
    return b3.iloc[b11:b12]
def fonk9():
    b1 = fonk1("courses.db")
    b13 = b1.cursor()
    fonk2(b13)
    b1.commit()
    b3 = fonk3(b1)
    while len(b3) > 6:
        print("__________________________________________")
        b14 = fonk8(b3)
        print("Your top courses are: ")
        print(b14.head())
        print(f"There are {len(b14)} courses remaining.")
        if len(b14) < 3:
            print("Stopping execution because there are too few courses.")
            break
        b3 = b14
    b1.close()
if b15 = = "__main__":
    fonk9()