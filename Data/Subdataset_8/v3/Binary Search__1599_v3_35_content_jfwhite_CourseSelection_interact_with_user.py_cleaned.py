import sqlite3
import numpy as np
import pandas as pd
def connect_to_database(database_name):
    return sqlite3.connect(database_name)
def delete_invalid_rows(cursor):
    delete_statement =
    cursor.execute(delete_statement)
def read_data_from_database(conn):
    return pd.read_sql("SELECT * FROM coursedata", con=conn)
def determine_most_variable_dimension(data):
    variations = []
    for col in ["course_level", "course_category", "course_enrollment"]:
        dimension = data[col]
        if dimension.max() != dimension.min():
            variation = (dimension.max() - dimension.min()) / dimension.std()
            variations.append((variation, col))
    max_variation, most_variable_dimension = max(variations)
    return most_variable_dimension
def print_course_options(low, medium, high):
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
def get_user_selection():
    selection = input("Do you prefer course 1, 2, or 3?\n")
    if selection in ["1", "2", "3"]:
        return int(selection)
    else:
        print("Please enter 1, 2, or 3.")
        return get_user_selection()
def recommend_courses(data):
    dimension = determine_most_variable_dimension(data)
    data.sort_values(by=dimension, inplace=True)
    print_course_options(
        data.iloc[0],
        data.iloc[round(len(data)/2)],
        data.iloc[-1]
    )
    print(f"Based on the dimension of {dimension.split('_')[1]},")
    selection = get_user_selection()
    start_index = round((selection-1) * len(data)/3)
    end_index = round(selection * len(data)/3)
    return data.iloc[start_index:end_index]
def main():
    conn = connect_to_database("courses.db")
    cursor = conn.cursor()
    delete_invalid_rows(cursor)
    data = read_data_from_database(conn)
    while len(data) > 6:
        print("__________________________________________")
        new_data = recommend_courses(data)
        print("Your top courses are: ")
        print(new_data.head())
        print(f"There are {len(new_data)} courses remaining.")
        if len(new_data) < 3:
            print("Stopping execution because there are too few courses.")
            break
        data = new_data
    conn.close()
if __name__ == "__main__":
    main()