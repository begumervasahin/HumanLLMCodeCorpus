import sqlite3
import pandas as pd
conn = sqlite3.connect("courses.db")
c = conn.cursor()
statement = "DELETE FROM coursedata WHERE course_level = -1 OR course_category = -1 OR course_enrollment = -1"
conn.execute(statement)
data = pd.read_sql("SELECT * FROM coursedata", con=conn)
def which_col(data):
    results = []
    for column in ['course_level', 'course_category', 'course_enrollment']:
        column_data = data[column]
        if column_data.max() != column_data.min():
            normalized_range = (column_data.max() - column_data.min()) / column_data.std()
            results.append((normalized_range, column))
    _, max_dimension = max(results)
    return max_dimension
def print_options(low, med, high):
    print("Here are three example courses:")
    for course in [low, med, high]:
        print(course["course_name"])
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def parse(selection):
    if selection in ["1", "2", "3"]:
        return int(selection)
    else:
        return parse(input("Please enter 1, 2, or 3.\n"))
def step(data):
    col = which_col(data)
    data.sort_values(by=col, inplace=True)
    print_options(
        data.iloc[0],
        data.iloc[len(data)
        data.iloc[-1]
    )
    print(f"Based on the dimension of {col.split('_')[1]},")
    selection = parse(input("Do you prefer course 1, 2, or 3?\n"))
    segment_start = round((selection - 1) * len(data) / 3)
    segment_end = round(selection * len(data) / 3)
    return data.iloc[segment_start:segment_end]
while len(data) > 6:
    print("__________________________________________")
    new_data = step(data)
    print("Your top courses are: ")
    print(new_data.head())
    print(f"There are {len(new_data)} courses remaining.")
    if len(new_data) < 3:
        print("Stopping execution because there are too few courses.")
        break
    data = new_data
conn.close()