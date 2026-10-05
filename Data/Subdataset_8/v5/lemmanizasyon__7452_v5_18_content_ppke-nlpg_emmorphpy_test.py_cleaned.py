import emmorphpy
emmorph = emmorphpy.EmMorphPy()
def process_word(word):
    analyses = emmorph.dstem(word, out_mode=list)
    for analysis in analyses:
        if len(analysis) == 5:
            base_form, pos_tag, lemma = analysis[:3]
            print(word, lemma, base_form, pos_tag, sep='\t')
        else:
            print(word, '<unknown>', sep='\t')
with open('test/test_words.txt') as file:
    for line in file:
        word = line.strip()
        process_word(word)
        print()