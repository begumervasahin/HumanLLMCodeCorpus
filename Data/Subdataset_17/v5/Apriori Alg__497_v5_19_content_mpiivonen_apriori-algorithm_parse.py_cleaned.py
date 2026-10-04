import pandas as pd
data = []
with open('data-2016.csv', 'r') as f:
    for index, line in enumerate(f):
        split_line = line.split(' ')
        no_courses = (len(split_line) - 1)
        for item in range(no_courses):
            new_dict = {
                'student_id': index,
                'registration_year': split_line[0].strip(),
                'course_year_and_month': split_line[(item * 5) + 1].strip(),
                'course_code': split_line[(item * 5) + 2].strip(),
                'course_name': split_line[(item * 5) + 3].strip().strip('"'),
                'credits': float(split_line[(item * 5) + 4].strip()),
                'final_grade': int(split_line[(item * 5) + 5].strip())
            }
            data.append(new_dict)
df = pd.DataFrame(data)
course_codes_list = pd.unique(df.course_code)
unique_len = len(course_codes_list)
print("Unique courses:", unique_len)
two_combinations = (unique_len * (unique_len - 1))
print("Unique two-course combinations:", two_combinations)
three_combinations = (unique_len * (unique_len - 1) * (unique_len - 2))
print("Unique three-course combinations:", three_combinations)
two_courses = [(j, i) for j in course_codes_list for i in course_codes_list if i != j]
student_list = pd.unique(df.student_id)
print("Number of students:", len(student_list))
filtered_students = [
    df[(df.student_id == student) & (df.course_code.isin(['582103', '582104']))]
    for student in student_list
]
for student_df in filtered_students:
    print(student_df)