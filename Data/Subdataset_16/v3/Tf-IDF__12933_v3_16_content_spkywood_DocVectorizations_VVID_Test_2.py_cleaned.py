import codecs
import re
def fonk1(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'ignore') as log_file:
        return log_file.readlines()
def fonk2(lines, file_path):
    with codecs.open(file_path, 'w+', 'utf-8', 'ignore') as result_log:
        result_log.writelines(lines[::-1])
def fonk3(lines, b5):
    b1 = []
    b2 = []
    for i, line in enumerate(lines):
        b3 = re.search(b5, line)
        if b3:
            b1.append(b3.group())
            b2.append(i)
    return b1, b2
def fonk4(b1, b2):
    b4 = []
    for i in range(1, len(b1)):
        if b1[i] != b1[i - 1]:
            b4.append(b2[i - 1])
    return b4
def fonk5():
    b5 = r'vvid=[A-Z0-9-]{36}'
    b6 = fonk1('app.log')
    fonk2(b6, 'app_convert.log')
    b7 = b6[::-1]
    print(f"All logfile lines: {len(b7)}\n")
    b1, b2 = fonk3(b7, b5)
    print(f"The number of all VVIDs: {len(b1)}\n")
    for line_number, vvid in zip(b2, b1):
        print(line_number)
        print(vvid)
    b4 = fonk4(b1, b2)
    print("Cut line numbers where VVID changes:")
    for cut_line in b4:
        print(cut_line)
if b8 = = "__main__":
    fonk5()