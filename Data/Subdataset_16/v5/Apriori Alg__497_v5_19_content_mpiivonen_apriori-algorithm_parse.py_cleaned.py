import pandas as pd
b1 = []
with open('b1-2016.csv', 'r') as f:
    for index, line in enumerate(f):
        b2 = line.split(' ')
        b3 = (len(b2) - 1)
        for item in range(b3):
            b4 = {
                'b13': index,
                'registration_year': b2[0].strip(),
                'course_year_and_month': b2[(item * 5) + 1].strip(),
                'course_code': b2[(item * 5) + 2].strip(),
                'course_name': b2[(item * 5) + 3].strip().strip('"'),
                'credits': float(b2[(item * 5) + 4].strip()),
                'final_grade': int(b2[(item * 5) + 5].strip())
            }
            b1.append(b4)
b5 = pd.DataFrame(b1)
b6 = pd.unique(b5.course_code)
b7 = len(b6)
print("Unique courses:", b7)
b8 = (b7 * (b7 - 1))
print("Unique two-course combinations:", b8)
b9 = (b7 * (b7 - 1) * (b7 - 2))
print("Unique three-course combinations:", b9)
b10 = [(j, i) for j in b6 for i in b6 if i != j]
b11 = pd.unique(b5.b13)
print("Number of students:", len(b11))
b12 = [
    b5[(b5.b13 = = student) & (b5.course_code.isin(['582103', '582104']))]
    for student in b11
]
for student_df in b12:
    print(student_df)