import codecs
import re
def fonk1(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'ignore') as file:
        return file.readlines()[::-1]
def fonk2(file_path, lines):
    with codecs.open(file_path, 'w+', 'utf-8', 'ignore') as file:
        file.writelines(lines)
def fonk3(b8, pattern):
    b1 = []
    b2 = []
    for index, line in enumerate(b8):
        b3 = re.search(pattern, line)
        if b3:
            b1.append(b3.group())
            b2.append(index)
    return b1, b2
def fonk4(b1, b2):
    b4 = []
    for i in range(1, len(b1)):
        if b1[i] != b1[i - 1]:
            b4.append(b2[i - 1])
    return b4
def fonk5():
    b5 = 'app.log'
    b6 = 'app_convert.log'
    b7 = r'vvid=[A-Z0-9-]{36}'
    b8 = fonk1(b5)
    fonk2(b6, b8)
    b9 = len(b8)
    print(f"Total number of lines in the log file: {b9}\n")
    b1, b2 = fonk3(b8, b7)
    b10 = len(b2)
    print(f"Total number of VVIDs found: {b10}\n")
    for line_number, vvid in zip(b2, b1):
        print(line_number)
        print(vvid)
    b4 = fonk4(b1, b2)
    print("Cut points where VVID changes:", b4)
if b11 = = "__main__":
    fonk5()