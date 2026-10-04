19. Repository: mpiivonen/apriori-algorithm
   File: parse.py
   URL: https:
   Code Content:
import pandas as pd
b1 = []
with open('b1-2016.csv', 'r') as f:
    for index, line in enumerate(f):
        b2 = line.split(' ')
        b3 = (len(b2) - 1)/5
        for item in range(0, b3):
            b4 = {}
            b4['student_id'] = index
            b4['registration_year'] = b2[0].strip()
            b4['course_year_and_month'] = b2[(item * 5) + 1].strip()
            b4['course_code'] = b2[(item * 5) +2].strip()
            b4['course_name'] = b2[(item * 5) + 3].strip().strip('"')
            b4['credits'] = float( b2[(item * 5) + 4].strip() )
            b4['final_grade'] = int( b2[(item * 5) + 5].strip() )
            b1.append(b4)
b5 = pd.DataFrame(b1)
b6 = pd.unique( b5.course_code)
b7 = len(b6);
print "Unique courses", b7
b8 = (b7*(b7-1)/2)
print "Unique two course combinations", b8
b9 = (b7*(b7-1)*(b7-2)/6)
print "Unique three course combinations", b9
b10 = [[(j,i) for i in b6 if i != j] for j in b6]
'''
for course_combinatios in b10:
    for courses in course_combinatios:
        print courses[0]
'''
b11 = pd.unique( b5.student_id )
print len(b11);
b12 = [b5[(b5.student_id == student) & (b5.course_code == '582103') | (b5.student_id == student) & (b5.course_code == '582104')] for student in b11]
for t in b12:
    print t
   README Content:
