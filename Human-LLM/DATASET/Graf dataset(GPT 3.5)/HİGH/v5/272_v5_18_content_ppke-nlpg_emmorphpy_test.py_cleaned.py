import emmorphpy
b1 = emmorphpy.EmMorphPy()
def fonk1(b5):
    b2 = b1.dstem(b5, out_mode=list)
    for analysis in b2:
        if len(analysis) == 5:
            base_form, pos_tag, b3 = analysis[:3]
            print(b5, b3, base_form, pos_tag, b4 = '\t')
        else:
            print(b5, '<unknown>', b4 = '\t')
with open('test/test_words.txt') as file:
    for line in file:
        b5 = line.strip()
        fonk1(b5)
        print()