import xlrd
import xlwt
import pandas as pd
import os
def calculate_grade(marks):
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
def calculate_semester_gpa(marks_list, subjects, credit_4, credit_3, credit_2, credit_1, record):
    total_credit_points = credit_4 * 4 + credit_3 * 3 + credit_2 * 2 + credit_1 * 1
    total_points = 0
    for credit in range(credit_4):
        record += str(subjects.pop(0))
        grade_letter, grade_point = calculate_grade(marks_list.pop(0))
        record += grade_letter
        total_points += grade_point * 4
    for credit in range(credit_3):
        record += str(subjects.pop(0))
        grade_letter, grade_point = calculate_grade(marks_list.pop(0))
        record += grade_letter
        total_points += grade_point * 3
    for credit in range(credit_2):
        record += str(subjects.pop(0))
        grade_letter, grade_point = calculate_grade(marks_list.pop(0))
        record += grade_letter
        total_points += grade_point * 2
    for credit in range(credit_1):
        record += str(subjects.pop(0))
        grade_letter, grade_point = calculate_grade(marks_list.pop(0))
        record += grade_letter
        total_points += grade_point * 1
    semester_gpa = round((total_points / total_credit_points), 2)
    return record, semester_gpa
def calculate_gpa(college, year, branch, low, high, semester):
    credit_mapping = {
        '1': (2, 0, 3, 3),
        '2': (2, 0, 3, 3),
        '5': (4, 2, 2, 0),
        '6': (4, 2, 2, 0),
        '7': (3, 3, 2, 0),
        '8': (3, 3, 2, 0)
    }
    credit_4, credit_2, credit_3, credit_1 = credit_mapping.get(semester, (6, 2, 0, 0))
    file_path = 'ExcelFiles/'
    workbook = xlrd.open_workbook(f'{file_path}1{college}{year}{branch}{low}-{high - 1}.xls')
    sheet = workbook.sheet_by_name('Sheet1')
    with open('gpa.txt', 'w+') as file:
        for row_idx in range(sheet.nrows):
            record = f"{sheet.cell_value(row_idx, 0)},{sheet.cell_value(row_idx, 1)},"
            subjects, marks_list = [], []
            for col_idx in range(5, 41, 5):
                if sheet.cell_value(row_idx, col_idx + 1) in ['P', 'A']:
                    subjects.append(sheet.cell_value(row_idx, col_idx - 3))
                    marks_list.append(-1 if sheet.cell_value(row_idx, col_idx + 1) == 'A' else int(sheet.cell_value(row_idx, col_idx)))
                else:
                    subjects.append(sheet.cell_value(row_idx, col_idx - 3))
                    marks_list.append(0)
            record, semester_gpa = calculate_semester_gpa(marks_list, subjects, credit_4, credit_3, credit_2, credit_1, record)
            percentage = round((semester_gpa - 0.750) * 10, 2)
            record += f"{semester_gpa},{percentage},"
            print(record, end='\t')
            print('\n')
            file.write(record + '\n')
    file.close()
    workbook_new = xlwt.Workbook()
    worksheet = workbook_new.add_sheet('Sheet1')
    file = open('gpa.txt', 'r+')
    data = file.readlines()
    for i, line in enumerate(data):
        row_data = line.split(',')
        for j, item in enumerate(row_data):
            if item.replace('.', '', 1).isdigit():
                worksheet.write(i, j, float(item))
            else:
                worksheet.write(i, j, item)
    workbook_new.save(f'{file_path}1{college}{year}{branch}{low}-{high - 1}GPA.xls')
    file.close()
    df = pd.read_csv("gpa.txt")
    relevant_cols = ['USN', 'Name', 'GPA', 'Percentage']
    df[relevant_cols].to_csv("gpar.txt", index=False)
    df_rank = pd.read_csv("gpar.txt")
    df_rank.columns = ['USN', 'Name', 'GPA', 'Percentage']
    try:
        df_rank = df_rank.sort_values(by=['GPA'], ascending=False)
    except AttributeError:
        print(" ")
    writer = pd.ExcelWriter(f'{file_path}1{college}{year}{branch}{low}-{high - 1}RANK.xls')
    df_rank.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    files = ['gpa.txt', 'gpar.txt']
    for file_name in files:
        try:
            os.remove(file_name)
        except:
            pass
calculate_gpa('College', '2024', 'Branch', 1, 5, '1')