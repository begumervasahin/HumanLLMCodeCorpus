import codecs
import re
b1 = r'vvid=[A-Z0-9-]{36}'
with codecs.open('app.log', 'r', 'utf-8', 'ignore') as log_file:
    b2 = log_file.readlines()[::-1]
with codecs.open('app_convert.log', 'w+', 'utf-8', 'ignore') as result_log:
    result_log.writelines(b2)
b3 = len(b2)
print("Total number of lines in the log file:", b3, '\n')
b4 = []
b5 = []
for index, line in enumerate(b2):
    b6 = re.search(b1, line)
    if b6:
        b4.append(b6.group())
        b5.append(index)
b7 = len(b5)
print("Total number of VVIDs found:", b7, '\n')
for line_number, vvid in zip(b5, b4):
    print(line_number)
    print(vvid)
b8 = []
for i in range(1, b7):
    if b4[i] != b4[i - 1]:
        b8.append(b5[i - 1])
        print(b8)