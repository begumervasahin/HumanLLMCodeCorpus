import math
def calculate_cosine(vector1=[], vector2=[]):
    if len(vector1) != len(vector2):
        return 0
    sca = 0
    for i in range(0, len(vector1)):
        sca = sca + (vector1[i] * vector2[i])
    length1 = 0
    length2 = 0
    for i in range(0, len(vector1)):
        length1 = length1 + (vector1[i] ** 2)
        length2 = length2 + (vector2[i] ** 2)
    nonsca = math.sqrt(length1 * length2)
    if nonsca == 0:
        return 0
    return sca * 1.0 / nonsca
f = open('dict_new.csv', 'r')
list = []
for line in f:
    list.append(str(line).lower().split('\n')[0])
f.close()
fi = open('doc.csv', 'r')
doc = []
for line in fi:
    doc.append(str(line).lower())
fi.close()
fs = open('stopword.txt', 'r')
sword = []
for line in fs:
    sword.append(str(line).lower())
fs.close()
for l in doc:
    print l
output = open('cos.csv', 'w')
vec = []
space = [1] * (len(list))
arr = []
for d in doc:
    v = [0] * (len(list))
    for w in list:
        if w in d:
            v[list.index(w)] = 1
    output.write(str(calculate_cosine(v, space)) + '\n')
    arr.append(calculate_cosine(v, space))
output.close()