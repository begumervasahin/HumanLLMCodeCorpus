import emmorphpy
b1 = emmorphpy.EmMorphPy()
for l in open('test/test_words.txt'):
    for i in b1.dstem(l.strip(), b2 = list):
        if len(i) == 5:
            print(l.strip(), i[2], i[0], i[1], b3 = '\t')
        else:
            print(l.strip(), '<unknown>', b3 = '\t')
    print()