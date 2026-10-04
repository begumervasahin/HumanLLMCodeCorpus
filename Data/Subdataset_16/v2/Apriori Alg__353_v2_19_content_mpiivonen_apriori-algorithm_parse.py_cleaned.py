import pandas as pd
def fonk1(b5):
    b1 = []
    with open(b5, 'r') as file:
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
def fonk2():
    b5 = 'b1-2016.csv'
    b1 = fonk1(b5)
    b6 = pd.DataFrame(b1)
    b7 = pd.unique(b6['course_code'])
    b8 = len(b7)
    print("Unique courses:", b8)
    b9 = (b8 * (b8 - 1))
    print("Unique two-course combinations:", b9)
    b10 = (b8 * (b8 - 1) * (b8 - 2))
    print("Unique three-course combinations:", b10)
    b11 = [(course1, course2) for i, course1 in enumerate(b7) for course2 in b7[i+1:]]
    b12 = pd.unique(b6['student_id'])
    print("Number of students:", len(b12))
    b13 = '582103'
    b14 = '582104'
    b15 = [b6[(b6['student_id'] == student) & (b6['course_code'].isin([b13, b14]))] for student in b12]
    for student_df in b15:
        if not student_df.empty:
            print(student_df)
if b16 = = "__main__":
    fonk2()