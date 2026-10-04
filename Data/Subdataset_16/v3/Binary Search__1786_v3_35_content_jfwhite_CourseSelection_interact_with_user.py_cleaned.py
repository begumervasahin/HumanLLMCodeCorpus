import sqlite3
import pandas as pd
def fonk1(b1 = "courses.db"):
    return sqlite3.connect(b1)
def fonk2(b14):
    b2 = b14.execute(b2)
def fonk3(b14):
    return pd.read_sql("SELECT * FROM coursedata", b3 = b14)
def fonk4(b6):
    return (b6.max() - b6.min()) / b6.std()
def fonk5(b15):
    b4 = []
    b5 = ['course_level', 'course_category', 'course_enrollment']
    for column in b5:
        b6 = b15[column]
        if b6.max() != b6.min():
            b7 = fonk4(b6)
            b4.append((b7, column))
    _, b8 = max(b4)
    return b8
def fonk6(low, mid, high):
    print("Here are three example courses to choose from:")
    for i, course in enumerate([low, mid, high], b9 = 1):
        print(f"\n{i}. {course['course_name']}")
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def fonk7():
    while True:
        b10 = input("Please select a course (1, 2, or 3):\n")
        if b10 in ["1", "2", "3"]:
            return int(b10)
        print("Invalid input. Please enter 1, 2, or 3.")
def fonk8(b15):
    b8 = fonk5(b15)
    b11 = b15.sort_values(by=b8)
    fonk6(
        b11.iloc[0],
        b11.iloc[len(b11)
        b11.iloc[-1]
    )
    print(f"Based on the dimension of {b8.split('_')[1]},")
    b10 = fonk7()
    b12 = round((b10 - 1) * len(b11) / 3)
    b13 = round(b10 * len(b11) / 3)
    return b11.iloc[b12:b13]
def fonk9():
    b14 = fonk1()
    try:
        fonk2(b14)
        b15 = fonk3(b14)
        while len(b15) > 6:
            print("__________________________________________")
            b15 = fonk8(b15)
            print("Your top courses are:")
            print(b15.head())
            print(f"There are {len(b15)} courses remaining.")
            if len(b15) < 3:
                print("Stopping execution because there are too few courses.")
                break
    finally:
        b14.close()
if b16 = = "__main__":
    fonk9()