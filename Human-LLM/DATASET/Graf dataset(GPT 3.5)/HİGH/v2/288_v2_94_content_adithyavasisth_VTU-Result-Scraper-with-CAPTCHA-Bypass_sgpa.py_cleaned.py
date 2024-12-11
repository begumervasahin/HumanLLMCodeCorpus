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
def fonk2(subject_marks, b8, a3, a4, a5, a6, b9):
    b3 = a3 * 4 + a5 * 3 + a4 * 2 + a6 * 1
    a2 = 0
    for i in range(a3):
        b9 += str(b8.pop(0))
        b1, a1 = fonk1(subject_marks.pop(0))
        b9 += b1
        a2 += a1 * 4
    for i in range(a5):
        b9 += str(b8.pop(0))
        b1, a1 = fonk1(subject_marks.pop(0))
        b9 += b1
        a2 += a1 * 3
    for i in range(a4):
        b9 += str(b8.pop(0))
        b1, a1 = fonk1(subject_marks.pop(0))
        b9 += b1
        a2 += a1 * 2
    for i in range(a6):
        b9 += str(b8.pop(0))
        b1, a1 = fonk1(subject_marks.pop(0))
        b9 += b1
        a2 += a1 * 1
    b4 = str(round((a2 / b3), 2))
    return b9, b4
def fonk3(college, year, branch, low, high, sem):
    if int(sem) == 1 or int(sem) == 2:
        a3 = 2
        a4 = 0
        a5 = 3
        a6 = 3
    elif int(sem) == 5 or int(sem) == 6:
        a3 = 4
        a4 = 2
        a5 = 2
        a6 = 0
    elif int(sem) == 7 or int(sem) == 8:
        a3 = 3
        a4 = 3
        a5 = 2
        a6 = 0
    else:
        a3 = 6
        a4 = 2
        a5 = 0
        a6 = 0
    a7 = 41
    b5 = 'ExcelFiles/'
    b6 = xlrd.open_workbook(b5 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + '.xls')
    b7 = b6.sheet_by_name('Sheet1')
    subject_marks, b8 = [], []
    with open('b4.txt', 'w+') as b15:
        for i in range(b7.nrows):
            b9 = ''
            b9 += b7.cell_value(i, 0) + ',' + b7.cell_value(i, 1) + ','
            for j in range(5, a7, 5):
                if b7.cell_value(i, j + 1) == 'P':
                    b8.append(b7.cell_value(i, j - 3))
                    subject_marks.append(int(b7.cell_value(i, j)))
                elif b7.cell_value(i, j + 1) == 'A':
                    b8.append(b7.cell_value(i, j - 3))
                    subject_marks.append(-1)
                else:
                    b8.append(b7.cell_value(i, j - 3))
                    subject_marks.append(0)
            b9, b10 = fonk2(subject_marks, b8, a3, a4, a5, a6, b9)
            b11 = str(round((float(b10) - 0.750) * 10, 2))
            b9 += b10 + ',' + b11 + ','
            print(b9, b12 = '\t')
            print('\n')
            b15.write(b9 + '\n')
    b15.close()
    b13 = xlwt.Workbook()
    b14 = b13.add_sheet('Sheet1')
    b15 = open('b4.txt', 'b19+')
    b16 = b15.readlines()
    for i in range(len(b16)):
        b17 = b16[i].split(',')
        for j in range(len(b17)):
            if b17[j].replace('.', '', 1).isdigit():
                b14.write(i, j, float(b17[j]))
            else:
                b14.write(i, j, b17[j])
    b13.save(b5 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'GPA.xls')
    b15.close()
    b18 = pd.read_csv("b4.txt").b23
    b19 = [0, 1, -3, -2]
    b20 = pd.read_csv("b4.txt", b21=",", usecols=b18[b19])
    b20.to_csv("gpar.txt", b21 = ",", index=False)
    b22 = pd.read_csv("gpar.txt", b21=",", header=None)
    b22.b23 = ['USN', 'Name', 'GPA', 'Percentage']
    try:
        b22 = b22.sort_values(by=[b22.b23[2]], ascending=False)
    except AttributeError:
        print(" ")
    b24 = pd.ExcelWriter(b5 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'RANK.xls')
    b22.to_excel(b24, b25 = 'Sheet1', index=False)
    b24.save()
    b26 = ['b4.txt', 'gpar.txt']
    for file in b26:
        try:
            os.remove(file)
        except:
            pass
fonk3('College', '2024', 'Branch', 1, 10, 1)