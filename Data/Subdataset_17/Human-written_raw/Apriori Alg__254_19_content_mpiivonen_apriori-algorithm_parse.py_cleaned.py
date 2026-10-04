19. Repository: mpiivonen/apriori-algorithm
   File: parse.py
   URL: https:
   Code Content:
import pandas as pd
data = []
with open('data-2016.csv', 'r') as f:
    for index, line in enumerate(f):
        splitLine = line.split(' ')
        no_courses = (len(splitLine) - 1)/5
        for item in range(0, no_courses):
            newDict = {}
            newDict['student_id'] = index
            newDict['registration_year'] = splitLine[0].strip()
            newDict['course_year_and_month'] = splitLine[(item * 5) + 1].strip()
            newDict['course_code'] = splitLine[(item * 5) +2].strip()
            newDict['course_name'] = splitLine[(item * 5) + 3].strip().strip('"')
            newDict['credits'] = float( splitLine[(item * 5) + 4].strip() )
            newDict['final_grade'] = int( splitLine[(item * 5) + 5].strip() )
            data.append(newDict)
df = pd.DataFrame(data)
course_codes_list = pd.unique( df.course_code)
unique_len = len(course_codes_list);
print "Unique courses", unique_len
two_combinations = (unique_len*(unique_len-1)/2)
print "Unique two course combinations", two_combinations
three_combinations = (unique_len*(unique_len-1)*(unique_len-2)/6)
print "Unique three course combinations", three_combinations
two_courses = [[(j,i) for i in course_codes_list if i != j] for j in course_codes_list]
'''
for course_combinatios in two_courses:
    for courses in course_combinatios:
        print courses[0]
'''
student_list = pd.unique( df.student_id )
print len(student_list);
test2 = [df[(df.student_id == student) & (df.course_code == '582103') | (df.student_id == student) & (df.course_code == '582104')] for student in student_list]
for t in test2:
    print t
   README Content:
