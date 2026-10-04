import sqlite3
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = b1.execute(b3)
b4 = pd.read_sql("SELECT * FROM coursedata", con=b1)
def fonk1(b4):
    b5 = ["course_level", "course_category", "course_enrollment"]
    b6 = {
        col: (b4[col].max() - b4[col].min()) / b4[col].std()
        for col in b5 if b4[col].max() != b4[col].min()
    }
    return max(b6, b7 = b6.get)
def fonk2(courses):
    print("Here are three example courses:")
    for i, course in enumerate(courses, 1):
        print(f"Course {i}:")
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def fonk3(b8):
    while b8 not in {"1", "2", "3"}:
        b8 = input("Please enter 1, 2, or 3.\n")
    return int(b8)
def fonk4(b4):
    b9 = fonk1(b4)
    b10 = b4.sort_values(by=b9).reset_index(drop=True)
    b11 = len(b10)
    b12 = [
        b10.iloc[0],
        b10.iloc[b11],
        b10.iloc[-1]
    ]
    fonk2(b12)
    print(f"Based on the dimension of {b9.split('_')[1]},")
    b8 = fonk3(input("Do you prefer course 1, 2, or 3?\n"))
    b13 = len(b10)
    b14 = (b8 - 1) * b13
    b15 = b8 * b13
    return b10.iloc[b14:b15]
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