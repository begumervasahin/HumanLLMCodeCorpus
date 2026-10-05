import sqlite3
import numpy as np
import pandas as pd
conn = sqlite3.connect("courses.db")
c = conn.cursor()
statement = "DELETE FROM coursedata WHERE {} OR {} OR {}"
statement = statement.format(
    "course_level = -1",
    "course_category = -1",
    "course_enrollment = -1"
)
conn.execute(statement)
data = pd.read_sql("SELECT * FROM coursedata", con=conn)
def which_col(data):
    results = []
    for col in ["course_level", "course_category", "course_enrollment"]:
        dim = data[col]
        if dim.max() != dim.min():
            result = (dim.max() - dim.min()) / dim.std()
            results.append((result, col))
    max_result, max_dimension = max(results)
    return max_dimension
def print_options(low, med, high):
    print("Here are three example courses:")
    print(low[1])
    print("\tLevel:\t\t{}".format(low[2]))
    print("\tCategory:\t{}".format(low[3]))
    print("\tEnrollment:\t{}".format(low[4]))
    print(med[1])
    print("\tLevel:\t\t{}".format(med[2]))
    print("\tCategory:\t{}".format(med[3]))
    print("\tEnrollment:\t{}".format(med[4]))
    print(high[1])
    print("\tLevel:\t\t{}".format(high[2]))
    print("\tCategory:\t{}".format(high[3]))
    print("\tEnrollment:\t{}".format(high[4]))
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
        data.iloc[round(len(data)/2)],
        data.iloc[-1]
    )
    print("Based on the dimension of " + col.split("_")[1] + ",")
    selection = parse(input("Do you prefer course 1, 2, or 3?\n"))
    segment_start = round((selection-1) * len(data)/3)
    segment_end = round(selection * len(data)/3)
    return data.iloc[segment_start:segment_end]
while len(data) > 6:
    print("__________________________________________")
    newdata = step(data)
    print("Your top courses are: ")
    print(newdata.head())
    print("There are {} courses remaining.".format(len(newdata)))
    if len(newdata) < 3:
        print("Stopping execution because there are too few courses.")
        break
    data = newdata
conn.close()