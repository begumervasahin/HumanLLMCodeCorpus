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
def fonk2(sub, b9, a3, a4, a5, a6, b10):
    b3 = a3 * 4 + a5 * 3 + a4 * 2 + a6 * 1
    a2 = 0
    for i in range(0, a3):
        b10 += str(b9.pop(0))
        st, b4 = fonk1(sub.pop(0))
        b10 += st
        a2 += b4 * 4
    for i in range(0, a5):
        b10 += str(b9.pop(0))
        st, b4 = fonk1(sub.pop(0))
        b10 += st
        a2 += b4 * 3
    for i in range(0, a4):
        b10 += str(b9.pop(0))
        st, b4 = fonk1(sub.pop(0))
        b10 += st
        a2 += b4 * 2
    for i in range(0, a6):
        b10 += str(b9.pop(0))
        st, b4 = fonk1(sub.pop(0))
        b10 += st
        a2 += b4 * 1
    b5 = str(round((a2 / b3), 2))
    return b10, b5
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
    b6 = 'ExcelFiles/'
    import xlrd
    b7 = xlrd.open_workbook(b6 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + '.xls')
    b8 = b7.sheet_by_name('Sheet1')
    sub, b9 = [], []
    with open('gpa.txt', 'w+') as b16:
        for i in range(0, b8.nrows):
            b10 = ''
            b10 += b8.cell_value(i, 0) + ',' + b8.cell_value(i, 1) + ','
            for j in range(5, a7, 5):
                if b8.cell_value(i, j + 1) == 'P':
                    b9.append(b8.cell_value(i, j - 3))
                    sub.append(int(b8.cell_value(i, j)))
                elif b8.cell_value(i, j + 1) == 'A':
                    b9.append(b8.cell_value(i, j - 3))
                    sub.append(-1)
                else:
                    b9.append(b8.cell_value(i, j - 3))
                    sub.append(0)
            b10, b11 = fonk2(sub, b9, a3, a4, a5, a6, b10)
            b12 = str(round((float(b11) - 0.750) * 10, 2))
            b10 += b11 + ',' + b12 + ','
            print(b10, b13 = '\t')
            print('\n')
            b16.write(b10 + '\n')
    b16.close()
    import xlwt
    b14 = xlwt.Workbook()
    b15 = b14.add_sheet('Sheet1')
    b16 = open('gpa.txt', 'b20+')
    b17 = b16.readlines()
    for i in range(len(b17)):
        b18 = b17[i].split(',')
        for j in range(len(b18)):
            if b18[j].replace('.', '', 1).isdigit():
                b15.write(i, j, float(b18[j]))
            else:
                b15.write(i, j, b18[j])
    b14.save(b6 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'GPA.xls')
    b16.close()
    import pandas as pd
    import os
    b19 = pd.read_csv("gpa.txt").b24
    b20 = [0, 1, -3, -2]
    b21 = pd.read_csv("gpa.txt", b22=",", usecols=b19[b20])
    b21.to_csv("gpar.txt", b22 = ",", index=False)
    b23 = pd.read_csv("gpar.txt", b22=",", header=None)
    b23.b24 = ['USN', 'Name', 'GPA', 'Percentage']
    try:
        b23 = b23.sort_values(by=[b23.b24[2]], ascending=False)
    except AttributeError:
        print(" ")
    b25 = pd.ExcelWriter(b6 + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'RANK.xls')
    b23.to_excel(b25, b26 = 'Sheet1', index=False)
    b25.save()
    b27 = ['gpa.txt', 'gpar.txt']
    for file in b27:
        try:
            os.remove(file)
        except:
            pass