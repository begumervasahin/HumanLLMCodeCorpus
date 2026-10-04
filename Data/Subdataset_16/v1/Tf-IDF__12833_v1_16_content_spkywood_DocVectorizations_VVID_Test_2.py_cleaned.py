import codecs
import re
b1 = r'vvid=[A-Z0-9-]{36}'
with codecs.open('app.log', 'r', 'utf-8', 'ignore') as log_file:
    b2 = log_file.readlines()
b3 = b2[::-1]
with codecs.open('app_convert.log', 'w+', 'utf-8', 'ignore') as result_log:
    result_log.writelines(b3)
b4 = len(b3)
print("All logfile lines:", b4, '\n')
b5 = []
b6 = []
for i, line in enumerate(b3):
    b7 = re.search(b1, line)
    if b7:
        b5.append(b7.group())
        b6.append(i)
b8 = len(b6)
print("The number of all VVIDs:", b8, '\n')
for line_number, vvid in zip(b6, b5):
    print(line_number)
    print(vvid)
b9 = []
for i in range(1, b8):
    if b5[i] != b5[i - 1]:
        b9.append(b6[i - 1])
        print(b9)