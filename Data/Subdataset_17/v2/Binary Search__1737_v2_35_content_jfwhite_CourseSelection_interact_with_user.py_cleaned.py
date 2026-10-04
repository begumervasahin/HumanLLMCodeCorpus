import sqlite3
import pandas as pd
conn = sqlite3.connect("courses.db")
c = conn.cursor()
cleanup_query =
conn.execute(cleanup_query)
data = pd.read_sql("SELECT * FROM coursedata", con=conn)
def get_most_variable_column(data):
    variability = []
    for column in ['course_level', 'course_category', 'course_enrollment']:
        column_data = data[column]
        if column_data.max() != column_data.min():
            normalized_range = (column_data.max() - column_data.min()) / column_data.std()
            variability.append((normalized_range, column))
    _, most_variable_column = max(variability)
    return most_variable_column
def display_course_options(low, mid, high):
    print("Here are three example courses to choose from:")
    for course in [low, mid, high]:
        print(f"\n{course['course_name']}")
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def get_user_selection():
    while True:
        selection = input("Please select a course (1, 2, or 3):\n")
        if selection in ["1", "2", "3"]:
            return int(selection)
        print("Invalid input. Please enter 1, 2, or 3.")
def refine_selection(data):
    most_variable_column = get_most_variable_column(data)
    data_sorted = data.sort_values(by=most_variable_column)
    display_course_options(
        data_sorted.iloc[0],
        data_sorted.iloc[len(data_sorted)
        data_sorted.iloc[-1]
    )
    print(f"Based on the dimension of {most_variable_column.split('_')[1]},")
    selection = get_user_selection()
    segment_start = round((selection - 1) * len(data_sorted) / 3)
    segment_end = round(selection * len(data_sorted) / 3)
    return data_sorted.iloc[segment_start:segment_end]
while len(data) > 6:
    print("__________________________________________")
    data = refine_selection(data)
    print("Your top courses are:")
    print(data.head())
    print(f"There are {len(data)} courses remaining.")
    if len(data) < 3:
        print("Stopping execution because there are too few courses.")
        break
conn.close()