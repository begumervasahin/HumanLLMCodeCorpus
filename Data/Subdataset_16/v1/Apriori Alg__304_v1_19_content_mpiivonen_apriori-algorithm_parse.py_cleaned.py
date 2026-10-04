import pandas as pd
def fonk1(b5):
    b1 = []
    with open(b5, 'r') as f:
        for index, line in enumerate(f):
            b2 = line.split(' ')
            b3 = (len(b2) - 1)
            for item in range(b3):
                b4 = {
                    'student_id': index,
                    'registration_year': b2[0].strip(),
                    'course_year_and_month': b2[(item * 5) + 1].strip(),
                    'course_code': b2[(item * 5) + 2].strip(),
                    'course_name': b2[(item * 5) + 3].strip().strip('"'),
                    'credits': float(b2[(item * 5) + 4].strip()),
                    'final_grade': int(b2[(item * 5) + 5].strip())
                }
                b1.append(b4)
    return b1
def fonk2():
    b5 = 'b1-2016.csv'
    b1 = fonk1(b5)
    b6 = pd.DataFrame(b1)
    b7 = pd.unique(b6.course_code)
    b8 = len(b7)
    print("Unique courses:", b8)
    b9 = (b8 * (b8 - 1))
    print("Unique two-course combinations:", b9)
    b10 = (b8 * (b8 - 1) * (b8 - 2))
    print("Unique three-course combinations:", b10)
    b11 = [[(j, i) for i in b7 if i != j] for j in b7]
    b12 = pd.unique(b6.student_id)
    print("Number of students:", len(b12))
    b13 = '582103'
    b14 = '582104'
    b15 = [b6[(b6.student_id == student) & ((b6.course_code == b13) | (b6.course_code == b14))] for student in b12]
    for t in b15:
        if not t.empty:
            print(t)
if b16 = = "__main__":
    fonk2()