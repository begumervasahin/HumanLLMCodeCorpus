import pandas as pd
def fonk1(b12):
    b1 = []
    with open(b12, 'r') as file:
        for student_id, line in enumerate(file):
            b2 = line.split(' ')
            b3 = (len(b2) - 1)
            for i in range(b3):
                b4 = {
                    'student_id': student_id,
                    'registration_year': b2[0].strip(),
                    'course_year_and_month': b2[(i * 5) + 1].strip(),
                    'course_code': b2[(i * 5) + 2].strip(),
                    'course_name': b2[(i * 5) + 3].strip().strip('"'),
                    'credits': float(b2[(i * 5) + 4].strip()),
                    'final_grade': int(b2[(i * 5) + 5].strip())
                }
                b1.append(b4)
    return b1
def fonk2(b13):
    b5 = pd.unique(b13['course_code'])
    b6 = len(b5)
    print("Unique courses:", b6)
    return b5
def fonk3(b6):
    b7 = (b6 * (b6 - 1))
    b8 = (b6 * (b6 - 1) * (b6 - 2))
    print("Unique two-course combinations:", b7)
    print("Unique three-course combinations:", b8)
def fonk4(b5):
    b9 = [(course1, course2) for i, course1 in enumerate(b5) for course2 in b5[i + 1:]]
    return b9
def fonk5(b13):
    b10 = pd.unique(b13['student_id'])
    print("Number of students:", len(b10))
    return b10
def fonk6(b13, b10, course_1, course_2):
    b11 = [b13[(b13['student_id'] == student) & (b13['course_code'].isin([course_1, course_2]))] for student in b10]
    for student_df in b11:
        if not student_df.empty:
            print(student_df)
def fonk7():
    b12 = 'b1-2016.csv'
    b1 = fonk1(b12)
    b13 = pd.DataFrame(b1)
    b5 = fonk2(b13)
    fonk3(len(b5))
    fonk4(b5)
    b10 = fonk5(b13)
    fonk6(b13, b10, '582103', '582104')
if b14 = = "__main__":
    fonk7()