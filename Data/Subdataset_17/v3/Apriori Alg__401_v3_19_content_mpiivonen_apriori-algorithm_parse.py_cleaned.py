import pandas as pd
def parse_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        for student_id, line in enumerate(file):
            split_line = line.split(' ')
            no_courses = (len(split_line) - 1)
            for i in range(no_courses):
                course_data = {
                    'student_id': student_id,
                    'registration_year': split_line[0].strip(),
                    'course_year_and_month': split_line[(i * 5) + 1].strip(),
                    'course_code': split_line[(i * 5) + 2].strip(),
                    'course_name': split_line[(i * 5) + 3].strip().strip('"'),
                    'credits': float(split_line[(i * 5) + 4].strip()),
                    'final_grade': int(split_line[(i * 5) + 5].strip())
                }
                data.append(course_data)
    return data
def calculate_unique_courses(df):
    unique_course_codes = pd.unique(df['course_code'])
    unique_course_count = len(unique_course_codes)
    print("Unique courses:", unique_course_count)
    return unique_course_codes
def calculate_combinations(unique_course_count):
    two_course_combinations = (unique_course_count * (unique_course_count - 1))
    three_course_combinations = (unique_course_count * (unique_course_count - 1) * (unique_course_count - 2))
    print("Unique two-course combinations:", two_course_combinations)
    print("Unique three-course combinations:", three_course_combinations)
def generate_two_course_pairs(unique_course_codes):
    two_course_pairs = [(course1, course2) for i, course1 in enumerate(unique_course_codes) for course2 in unique_course_codes[i + 1:]]
    return two_course_pairs
def count_unique_students(df):
    unique_students = pd.unique(df['student_id'])
    print("Number of students:", len(unique_students))
    return unique_students
def filter_students_by_courses(df, unique_students, course_1, course_2):
    filtered_students = [df[(df['student_id'] == student) & (df['course_code'].isin([course_1, course_2]))] for student in unique_students]
    for student_df in filtered_students:
        if not student_df.empty:
            print(student_df)
def main():
    file_path = 'data-2016.csv'
    data = parse_csv(file_path)
    df = pd.DataFrame(data)
    unique_course_codes = calculate_unique_courses(df)
    calculate_combinations(len(unique_course_codes))
    generate_two_course_pairs(unique_course_codes)
    unique_students = count_unique_students(df)
    filter_students_by_courses(df, unique_students, '582103', '582104')
if __name__ == "__main__":
    main()