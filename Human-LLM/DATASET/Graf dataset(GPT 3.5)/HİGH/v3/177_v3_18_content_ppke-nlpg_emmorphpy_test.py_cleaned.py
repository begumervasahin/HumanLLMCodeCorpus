import emmorphpy
b1 = emmorphpy.EmMorphPy()
b2 = 'test/test_words.txt'
with open(b2, 'r') as file:
    for line in file:
        b3 = line.strip()
        b4 = b1.dstem(b3, out_mode=list)
        if b4:
            for result in b4:
                if len(result) == 5:
                    print(b3, result[2], result[0], result[1], b5 = '\t')
                else:
                    print(b3, '<unknown>', b5 = '\t')
        else:
            print(b3, '<unknown>', b5 = '\t')
        print()