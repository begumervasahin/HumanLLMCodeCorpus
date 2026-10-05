import emmorphpy
b1 = emmorphpy.EmMorphPy()
with open('test/test_words.txt', 'r') as file:
    for line in file:
        b2 = line.strip()
        b3 = b1.dstem(b2, out_mode=list)
        if b3:
            for result in b3:
                if len(result) == 5:
                    print(b2, result[2], result[0], result[1], b4 = '\t')
                else:
                    print(b2, '<unknown>', b4 = '\t')
        else:
            print(b2, '<unknown>', b4 = '\t')
        print()
