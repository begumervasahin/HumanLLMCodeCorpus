import emmorphpy
emmorph = emmorphpy.EmMorphPy()
with open('test/test_words.txt') as file:
    for line in file:
        word = line.strip()
        analyses = emmorph.dstem(word, out_mode=list)
        for analysis in analyses:
            if len(analysis) == 5:
                base_form = analysis[0]
                pos_tag = analysis[1]
                lemma = analysis[2]
                print(word, lemma, base_form, pos_tag, sep='\t')
            else:
                print(word, '<unknown>', sep='\t')
        print()