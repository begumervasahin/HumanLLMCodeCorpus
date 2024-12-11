import xlrd
import xlwt
import pandas as pd
import os
def fonk1(b2):
    a1 = 0
    b1 = ''
    if b2 >= 90:
        b1 += ',S+,'
        a1 = 10
    elif b2 >= 80:
        b1 += ',S,'
        a1 = 9
    elif b2 >= 70:
        b1 += ',A,'
        a1 = 8
    elif b2 >= 60:
        b1 += ',B,'
        a1 = 7
    elif b2 >= 50:
        b1 += ',C,'
        a1 = 6
    elif b2 >= 45:
        b1 += ',D,'
        a1 = 5
    elif b2 >= 40:
        b1 += ',E,'
        a1 = 4
    elif b2 >= 0:
        b1 += ',F,'
        a1 = 0
    elif b2 = = -1:
        b1 += ',Ab,'
        a1 = 0
    return b1, a1
def fonk2(b11, subjects, credit_4, credit_3, credit_2, b6, b10):
    b3 = credit_4 * 4 + credit_3 * 3 + credit_2 * 2 + b6 * 1
    a2 = 0
    for credit in range(credit_4):
        b10 += str(subjects.pop(0))
        b1, a1 = fonk1(b11.pop(0))
        b10 += b1
        a2 += a1 * 4
    for credit in range(credit_3):
        b10 += str(subjects.pop(0))
        b1, a1 = fonk1(b11.pop(0))
        b10 += b1
        a2 += a1 * 3
    for credit in range(credit_2):
        b10 += str(subjects.pop(0))
        b1, a1 = fonk1(b11.pop(0))
        b10 += b1
        a2 += a1 * 2
    for credit in range(b6):
        b10 += str(subjects.pop(0))
        b1, a1 = fonk1(b11.pop(0))
        b10 += b1
        a2 += a1 * 1
    b4 = round((a2 / b3), 2)
    return b10, b4
def fonk3(college, year, branch, low, high, semester):
    b5 = {
        '1': (2, 0, 3, 3),
        '2': (2, 0, 3, 3),
        '5': (4, 2, 2, 0),
        '6': (4, 2, 2, 0),
        '7': (3, 3, 2, 0),
        '8': (3, 3, 2, 0)
    }
    credit_4, credit_2, credit_3, b6 = b5.get(semester, (6, 2, 0, 0))
    b7 = 'ExcelFiles/'
    b8 = xlrd.open_workbook(f'{b7}1{college}{year}{branch}{low}-{high - 1}.xls')
    b9 = b8.sheet_by_name('Sheet1')
    with open('gpa.txt', 'w+') as b16:
        for row_idx in range(b9.nrows):
            b10 = f"{b9.cell_value(row_idx, 0)},{b9.cell_value(row_idx, 1)},"
            subjects, b11 = [], []
            for col_idx in range(5, 41, 5):
                if b9.cell_value(row_idx, col_idx + 1) in ['P', 'A']:
                    subjects.append(b9.cell_value(row_idx, col_idx - 3))
                    b11.append(-1 if b9.cell_value(row_idx, col_idx + 1) == 'A' else int(b9.cell_value(row_idx, col_idx)))
                else:
                    subjects.append(b9.cell_value(row_idx, col_idx - 3))
                    b11.append(0)
            b10, b4 = fonk2(b11, subjects, credit_4, credit_3, credit_2, b6, b10)
            b12 = round((b4 - 0.750) * 10, 2)
            b10 += f"{b4},{b12},"
            print(b10, b13 = '\t')
            print('\n')
            b16.write(b10 + '\n')
    b16.close()
    b14 = xlwt.Workbook()
    b15 = b14.add_sheet('Sheet1')
    b16 = open('gpa.txt', 'r+')
    b17 = b16.readlines()
    for i, line in enumerate(b17):
        b18 = line.split(',')
        for j, item in enumerate(b18):
            if item.replace('.', '', 1).isdigit():
                b15.write(i, j, float(item))
            else:
                b15.write(i, j, item)
    b14.save(f'{b7}1{college}{year}{branch}{low}-{high - 1}GPA.xls')
    b16.close()
    b19 = pd.read_csv("gpa.txt")
    b20 = ['USN', 'Name', 'GPA', 'Percentage']
    b19[b20].to_csv("gpar.txt", b21 = False)
    b22 = pd.read_csv("gpar.txt")
    b22.b23 = ['USN', 'Name', 'GPA', 'Percentage']
    try:
        b22 = b22.sort_values(by=['GPA'], ascending=False)
    except AttributeError:
        print(" ")
    b24 = pd.ExcelWriter(f'{b7}1{college}{year}{branch}{low}-{high - 1}RANK.xls')
    b22.to_excel(b24, b25 = 'Sheet1', b21=False)
    b24.save()
    b26 = ['gpa.txt', 'gpar.txt']
    for file_name in b26:
        try:
            os.remove(file_name)
        except:
            pass
fonk3('College', '2024', 'Branch', 1, 5, '1')