import sqlite3
import numpy as np
import pandas as pd
def fonk1(database_name):
    return sqlite3.connect(database_name)
def fonk2(b12):
    b1 = b12.execute(b1)
def fonk3(b11):
    return pd.read_sql("SELECT * FROM coursedata", b2 = b11)
def fonk4(b13):
    b3 = []
    for col in ["course_level", "course_category", "course_enrollment"]:
        b4 = b13[col]
        if b4.max() != b4.min():
            b5 = (b4.max() - b4.min()) / b4.std()
            b3.append((b5, col))
    max_variation, b6 = max(b3)
    return b6
def fonk5(low, medium, high):
    print("Here are three example courses:")
    print(low[1])
    print(f"\tLevel:\t\t{low[2]}")
    print(f"\tCategory:\t{low[3]}")
    print(f"\tEnrollment:\t{low[4]}")
    print(medium[1])
    print(f"\tLevel:\t\t{medium[2]}")
    print(f"\tCategory:\t{medium[3]}")
    print(f"\tEnrollment:\t{medium[4]}")
    print(high[1])
    print(f"\tLevel:\t\t{high[2]}")
    print(f"\tCategory:\t{high[3]}")
    print(f"\tEnrollment:\t{high[4]}")
def fonk6():
    b7 = input("Do you prefer course 1, 2, or 3?\n")
    if b7 in ["1", "2", "3"]:
        return int(b7)
    else:
        print("Please enter 1, 2, or 3.")
        return fonk6()
def fonk7(b13):
    b4 = fonk4(b13)
    b13.sort_values(b8 = b4, inplace=True)
    fonk5(
        b13.iloc[0],
        b13.iloc[round(len(b13)/2)],
        b13.iloc[-1]
    )
    print(f"Based on the b4 of {b4.split('_')[1]},")
    b7 = fonk6()
    b9 = round((b7-1) * len(b13)/3)
    b10 = round(b7 * len(b13)/3)
    return b13.iloc[b9:b10]
def fonk8():
    b11 = fonk1("courses.db")
    b12 = b11.b12()
    fonk2(b12)
    b13 = fonk3(b11)
    while len(b13) > 6:
        print("__________________________________________")
        b14 = fonk7(b13)
        print("Your top courses are: ")
        print(b14.head())
        print(f"There are {len(b14)} courses remaining.")
        if len(b14) < 3:
            print("Stopping execution because there are too few courses.")
            break
        b13 = b14
    b11.close()
if b15 = = "__main__":
    fonk8()