import sqlite3
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = "DELETE FROM coursedata WHERE course_level = -1 OR course_category = -1 OR course_enrollment = -1"
b1.execute(b3)
b4 = pd.read_sql("SELECT * FROM coursedata", con=b1)
def fonk1(b4):
    b5 = []
    for column in ['course_level', 'course_category', 'course_enrollment']:
        b6 = b4[column]
        if b6.max() != b6.min():
            b7 = (b6.max() - b6.min()) / b6.std()
            b5.append((b7, column))
    _, b8 = max(b5)
    return b8
def fonk2(low, med, high):
    print("Here are three example courses:")
    for course in [low, med, high]:
        print(course["course_name"])
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def fonk3(b11):
    if b11 in ["1", "2", "3"]:
        return int(b11)
    else:
        return fonk3(input("Please enter 1, 2, or 3.\n"))
def fonk4(b4):
    b9 = fonk1(b4)
    b4.sort_values(b10 = b9, inplace=True)
    fonk2(
        b4.iloc[0],
        b4.iloc[len(b4)
        b4.iloc[-1]
    )
    print(f"Based on the dimension of {b9.split('_')[1]},")
    b11 = fonk3(input("Do you prefer course 1, 2, or 3?\n"))
    b12 = round((b11 - 1) * len(b4) / 3)
    b13 = round(b11 * len(b4) / 3)
    return b4.iloc[b12:b13]
while len(b4) > 6:
    print("__________________________________________")
    b14 = fonk4(b4)
    print("Your top courses are: ")
    print(b14.head())
    print(f"There are {len(b14)} courses remaining.")
    if len(b14) < 3:
        print("Stopping execution because there are too few courses.")
        break
    b4 = b14
b1.close()