import sqlite3
import pandas as pd
conn = sqlite3.connect("courses.db")
c = conn.cursor()
delete_query =
conn.execute(delete_query)
data = pd.read_sql("SELECT * FROM coursedata", con=conn)
def find_most_variable_column(data):
    columns = ["course_level", "course_category", "course_enrollment"]
    variabilities = {
        col: (data[col].max() - data[col].min()) / data[col].std()
        for col in columns if data[col].max() != data[col].min()
    }
    return max(variabilities, key=variabilities.get)
def print_course_options(courses):
    print("Here are three example courses:")
    for i, course in enumerate(courses, 1):
        print(f"Course {i}:")
        print(f"\tLevel:\t\t{course['course_level']}")
        print(f"\tCategory:\t{course['course_category']}")
        print(f"\tEnrollment:\t{course['course_enrollment']}")
def parse_selection(selection):
    while selection not in {"1", "2", "3"}:
        selection = input("Please enter 1, 2, or 3.\n")
    return int(selection)
def select_course_segment(data):
    most_variable_col = find_most_variable_column(data)
    data_sorted = data.sort_values(by=most_variable_col).reset_index(drop=True)
    mid_index = len(data_sorted)
    course_examples = [
        data_sorted.iloc[0],
        data_sorted.iloc[mid_index],
        data_sorted.iloc[-1]
    ]
    print_course_options(course_examples)
    print(f"Based on the dimension of {most_variable_col.split('_')[1]},")
    selection = parse_selection(input("Do you prefer course 1, 2, or 3?\n"))
    segment_size = len(data_sorted)
    segment_start = (selection - 1) * segment_size
    segment_end = selection * segment_size
    return data_sorted.iloc[segment_start:segment_end]
while len(data) > 6:
    print("__________________________________________")
    data = select_course_segment(data)
    print("Your top courses are: ")
    print(data.head())
    print(f"There are {len(data)} courses remaining.")
    if len(data) < 3:
        print("Stopping execution because there are too few courses.")
        break
conn.close()