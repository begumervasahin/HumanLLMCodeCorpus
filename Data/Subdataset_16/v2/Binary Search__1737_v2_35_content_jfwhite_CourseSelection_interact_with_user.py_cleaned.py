import sqlite3
import pandas as pd
b1 = sqlite3.connect("courses.db")
b2 = b1.cursor()
b3 = b1.execute(b3)
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
def fonk2(low, mid, high):
    print("Here are three example courses to choose from:")
    for course in [low, mid, high]:
        print(f"\n{course['course_name']}")
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def fonk3():
    while True:
        b9 = input("Please select a course (1, 2, or 3):\n")
        if b9 in ["1", "2", "3"]:
            return int(b9)
        print("Invalid input. Please enter 1, 2, or 3.")
def fonk4(b4):
    b8 = fonk1(b4)
    b10 = b4.sort_values(by=b8)
    fonk2(
        b10.iloc[0],
        b10.iloc[len(b10)
        b10.iloc[-1]
    )
    print(f"Based on the dimension of {b8.split('_')[1]},")
    b9 = fonk3()
    b11 = round((b9 - 1) * len(b10) / 3)
    b12 = round(b9 * len(b10) / 3)
    return b10.iloc[b11:b12]
while len(b4) > 6:
    print("__________________________________________")
    b4 = fonk4(b4)
    print("Your top courses are:")
    print(b4.head())
    print(f"There are {len(b4)} courses remaining.")
    if len(b4) < 3:
        print("Stopping execution because there are too few courses.")
        break
b1.close()