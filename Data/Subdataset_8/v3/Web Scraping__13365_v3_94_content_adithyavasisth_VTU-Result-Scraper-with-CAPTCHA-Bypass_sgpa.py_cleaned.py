import xlrd
import xlwt
import pandas as pd
import os
def assign_grade(marks):
    grade_point = 0
    grade_letter = ''
    if marks >= 90:
        grade_letter += ',S+,'
        grade_point = 10
    elif marks >= 80:
        grade_letter += ',S,'
        grade_point = 9
    elif marks >= 70:
        grade_letter += ',A,'
        grade_point = 8
    elif marks >= 60:
        grade_letter += ',B,'
        grade_point = 7
    elif marks >= 50:
        grade_letter += ',C,'
        grade_point = 6
    elif marks >= 45:
        grade_letter += ',D,'
        grade_point = 5
    elif marks >= 40:
        grade_letter += ',E,'
        grade_point = 4
    elif marks >= 0:
        grade_letter += ',F,'
        grade_point = 0
    elif marks == -1:
        grade_letter += ',Ab,'
        grade_point = 0
    return grade_letter, grade_point
def calculate_gpa(subject_marks, subject_names, count_4, count_2, count_3, count_1, record):
    total_credits = count_4 * 4 + count_3 * 3 + count_2 * 2 + count_1 * 1
    total_points = 0
    for _ in range(count_4):
        record += str(subject_names.pop(0))
        grade_letter, grade_point = assign_grade(subject_marks.pop(0))
        record += grade_letter
        total_points += grade_point * 4
    for _ in range(count_3):
        record += str(subject_names.pop(0))
        grade_letter, grade_point = assign_grade(subject_marks.pop(0))
        record += grade_letter
        total_points += grade_point * 3
    for _ in range(count_2):
        record += str(subject_names.pop(0))
        grade_letter, grade_point = assign_grade(subject_marks.pop(0))
        record += grade_letter
        total_points += grade_point * 2
    for _ in range(count_1):
        record += str(subject_names.pop(0))
        grade_letter, grade_point = assign_grade(subject_marks.pop(0))
        record += grade_letter
        total_points += grade_point * 1
    gpa = str(round((total_points / total_credits), 2))
    return record, gpa
def process_gradesheet(file_path):
    marks_code = 41
    subject_marks, subject_names = [], []
    with open('gpa.txt', 'w+') as f:
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_name('Sheet1')
        for i in range(sheet.nrows):
            record = ''
            record += sheet.cell_value(i, 0) + ',' + sheet.cell_value(i, 1) + ','
            for j in range(5, marks_code, 5):
                if sheet.cell_value(i, j + 1) == 'P':
                    subject_names.append(sheet.cell_value(i, j - 3))
                    subject_marks.append(int(sheet.cell_value(i, j)))
                elif sheet.cell_value(i, j + 1) == 'A':
                    subject_names.append(sheet.cell_value(i, j - 3))
                    subject_marks.append(-1)
                else:
                    subject_names.append(sheet.cell_value(i, j - 3))
                    subject_marks.append(0)
            record, sgpa = calculate_gpa(subject_marks, subject_names, count_4, count_2, count_3, count_1, record)
            percentage = str(round((float(sgpa) - 0.750) * 10, 2))
            record += sgpa + ',' + percentage + ','
            print(record, end='\t')
            print('\n')
            f.write(record + '\n')
    f.close()
def save_to_excel(file_path, data):
    book = xlwt.Workbook()
    ws = book.add_sheet('Sheet1')
    f = open('gpa.txt', 'r+')
    data = f.readlines()
    for i in range(len(data)):
        row = data[i].split(',')
        for j in range(len(row)):
            if row[j].replace('.', '', 1).isdigit():
                ws.write(i, j, float(row[j]))
            else:
                ws.write(i, j, row[j])
    book.save(file_path)
    f.close()
def save_rank_to_excel(file_path, data):
    cols = pd.read_csv("gpa.txt").columns
    r = [0, 1, -3, -2]
    df = pd.read_csv("gpa.txt", sep=",", usecols=cols[r])
    df.to_csv("gpar.txt", sep=",", index=False)
    df1 = pd.read_csv("gpar.txt", sep=",", header=None)
    df1.columns = ['USN', 'Name', 'GPA', 'Percentage']
    try:
        df1 = df1.sort_values(by=[df1.columns[2]], ascending=False)
    except AttributeError:
        print(" ")
    writer = pd.ExcelWriter(file_path)
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
def calculate_and_write_gpa(college, year, branch, low, high, sem):
    if int(sem) == 1 or int(sem) == 2:
        count_4 = 2
        count_2 = 0
        count_3 = 3
        count_1 = 3
    elif int(sem) == 5 or int(sem) == 6:
        count_4 = 4
        count_2 = 2
        count_3 = 2
        count_1 = 0
    elif int(sem) == 7 or int(sem) == 8:
        count_4 = 3
        count_2 = 3
        count_3 = 2
        count_1 = 0
    else:
        count_4 = 6
        count_2 = 2
        count_3 = 0
        count_1 = 0
    pth = 'ExcelFiles/'
    file_path = pth + '1' + college + year + branch + str(low) + '-' + str
(high - 1) + '.xls'
process_gradesheet(file_path)
save_to_excel(pth + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'GPA.xls', data)
save_rank_to_excel(pth + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'RANK.xls', data)