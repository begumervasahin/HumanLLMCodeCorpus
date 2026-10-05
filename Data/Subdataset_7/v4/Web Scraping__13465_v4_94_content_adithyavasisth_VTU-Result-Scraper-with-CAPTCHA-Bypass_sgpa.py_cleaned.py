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
def fonk2(college, year, branch, low, high, semester):
    if int(semester) == 1 or int(semester) == 2:
        a2 = 2
        a3 = 0
        a4 = 3
        a5 = 3
    elif int(semester) == 5 or int(semester) == 6:
        a2 = 4
        a3 = 2
        a4 = 2
        a5 = 0
    elif int(semester) == 7 or int(semester) == 8:
        a2 = 3
        a3 = 3
        a4 = 2
        a5 = 0
    else:
        a2 = 6
        a3 = 2
        a4 = 0
        a5 = 0
    b3 = 'ExcelFiles/'
    b4 = xlrd.open_workbook(b3 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + '.xls')
    b5 = b4.sheet_by_name('Sheet1')
    subjects, b6 = [], []
    with open('gpa.txt', 'w+') as b13:
        for i in range(b5.nrows):
            b7 = ''
            b7 += b5.cell_value(i, 0) + ',' + b5.cell_value(i, 1) + ','
            for j in range(5, 41, 5):
                if b5.cell_value(i, j + 1) == 'P':
                    subjects.append(b5.cell_value(i, j - 3))
                    b6.append(int(b5.cell_value(i, j)))
                elif b5.cell_value(i, j + 1) == 'A':
                    subjects.append(b5.cell_value(i, j - 3))
                    b6.append(-1)
                else:
                    subjects.append(b5.cell_value(i, j - 3))
                    b6.append(0)
            b7, b8 = fonk3(b6, subjects, a2, a3, a4, a5, b7)
            b9 = str(round((float(b8) - 0.750) * 10, 2))
            b7 += b8 + ',' + b9 + ','
            print(b7, b10 = '\t')
            print('\n')
            b13.write(b7 + '\n')
    b13.close()
    b11 = xlwt.Workbook()
    b12 = b11.add_sheet('Sheet1')
    b13 = open('gpa.txt', 'r+')
    b14 = b13.readlines()
    for i in range(len(b14)):
        b15 = b14[i].split(',')
        for j in range(len(b15)):
            if b15[j].replace('.', '', 1).isdigit():
                b12.write(i, j, float(b15[j]))
            else:
                b12.write(i, j, b15[j])
    b11.save(b3 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'GPA.xls')
    b13.close()
    b16 = pd.read_csv("gpa.txt").b16
    b17 = [0, 1, -3, -2]
    b18 = pd.read_csv("gpa.txt", b19=",", usecols=b16[b17])
    b18.to_csv("gpar.txt", b19 = ",", index=False)
    b20 = pd.read_csv("gpar.txt", b19=",", header=None)
    b20.b16 = ['USN', 'Name', 'GPA', 'Percentage']
    try:
        b20 = b20.sort_values(by=[b20.b16[2]], ascending=False)
    except AttributeError:
        print(" ")
    b21 = pd.ExcelWriter(b3 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'RANK.xls')
    b20.to_excel(b21, b22 = 'Sheet1', index=False)
    b21.save()
    b23 = ['gpa.txt', 'gpar.txt']
    for file_name in b23:
        try:
            os.remove(file_name)
        except:
            pass
def fonk3(b6, subjects, a2, a3, a4, a5, b7):
    b24 = a2 * 4 + a4 * 3 + a3 * 2 + a5 * 1
    a6 = 0
    for i in range(a2):
        b7 += str(subjects.pop(0))
        b1, a1 = fonk1(b6.pop(0))
        b7 += b1
        a6 += a1 * 4
    for i in range(a4):
        b7 += str(subjects.pop(0))
        b1, a1 = fonk1(b6.pop(0))
        b7 += b1
        a6 += a1 * 3
    for i in range(a3):
        b7 += str(subjects.pop(0))
        b1, a1 = fonk1(b6.pop(0))
        b7 += b1
        a6 += a1 * 2
    for