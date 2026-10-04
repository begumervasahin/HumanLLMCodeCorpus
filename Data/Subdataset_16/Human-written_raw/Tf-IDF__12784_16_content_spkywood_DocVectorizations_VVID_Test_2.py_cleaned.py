import codecs
import re
b1 = r'vvid=[A-Z0-9-]{36}'
b2 = codecs.open('app.log', 'r', 'utf-8', 'ignore')
b3 = b2.readlines()[::-1]
b4 = codecs.open('app_convert.log', 'w+', 'utf-8', 'ignore')
b4.writelines(b3)
b5 = len(b3)
print "All logfile lines:", b5, '\n'
b6 = []
b7 = []
for i in range(0, b5):
    re.match(b1, b3[i])
    b8 = re.search(b1, b3[i])
    if b8:
        b6.append(b8.group())
        b9 = i
        b7.append(b9)
b10 = len(b7)
print "The number of the All vvid", b10, '\n'
for j in range(0, b10):
    print b7[j]
    print b6[j]
b11 = []
for cut_item in range(1,b10):
    if b6[cut_item] != b6[cut_item - 1]:
        b11.append(b7[cut_item - 1])
        print b11