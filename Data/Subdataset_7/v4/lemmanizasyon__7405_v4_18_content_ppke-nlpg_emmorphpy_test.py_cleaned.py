import emmorphpy
b1 = emmorphpy.EmMorphPy()
with open('test/test_words.txt') as file:
    for line in file:
        b2 = line.strip()
        b3 = b1.dstem(b2, out_mode=list)
        for analysis in b3:
            if len(analysis) == 5:
                b4 = analysis[0]
                b5 = analysis[1]
                b6 = analysis[2]
                print(b2, b6, b4, b5, b7 = '\t')
            else:
                print(b2, '<unknown>', b7 = '\t')
        print()