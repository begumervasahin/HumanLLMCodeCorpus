import sqlite3
import numpy as np
import pandas as pd
conn = sqlite3.connect("courses.db")
c = conn.cursor()
delete_statement =
c.execute(delete_statement)
conn.commit()
data = pd.read_sql("SELECT * FROM coursedata", con=conn)
def determine_most_variable_dimension(data):
    variations = []
    for col in ["course_level", "course_category", "course_enrollment"]:
        dim = data[col]
        if dim.max() != dim.min():
            variation = (dim.max() - dim.min()) / dim.std()
            variations.append((variation, col))
    max_variation, most_variable_dimension = max(variations)
    return most_variable_dimension
def print_course_options(low, med, high):
    print("Here are three example courses:")
    print_course_info(low)
    print_course_info(med)
    print_course_info(high)
def print_course_info(course):
    print(course[1])
    print(f"\tLevel:\t\t{course[2]}")
    print(f"\tCategory:\t{course[3]}")
    print(f"\tEnrollment:\t{course[4]}")
def get_user_selection():
    selection = input("Do you prefer course 1, 2, or 3?\n")
    if selection in ["1", "2", "3"]:
        return int(selection)
    else:
        print("Please enter 1, 2, or 3.")
        return get_user_selection()
def step(data):
    col = determine_most_variable_dimension(data)
    data.sort_values(by=col, inplace=True)
    print_course_options(
        data.iloc[0],
        data.iloc[round(len(data)/2)],
        data.iloc[-1]
    )
    print(f"Based on the dimension of {col.split('_')[1]},")
    selection = get_user_selection()
    segment_start = round((selection-1) * len(data)/3)
    segment_end = round(selection * len(data)/3)
    return data.iloc[segment_start:segment_end]
while len(data) > 6:
    print("__________________________________________")
    newdata = step(data)
    print("Your top courses are: ")
    print(newdata.head())
    print(f"There are {len(newdata)} courses remaining.")
    if len(newdata) < 3:
        print("Stopping execution because there are too few courses.")
        break
    data = newdata
conn.close()