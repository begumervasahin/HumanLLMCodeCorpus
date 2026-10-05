import emmorphpy
emmorph = emmorphpy.EmMorphPy()
file_path = 'test/test_words.txt'
with open(file_path, 'r') as file:
    for line in file:
        word = line.strip()
        stem_results = emmorph.dstem(word, out_mode=list)
        if stem_results:
            for result in stem_results:
                if len(result) == 5:
                    print(word, result[2], result[0], result[1], sep='\t')
                else:
                    print(word, '<unknown>', sep='\t')
        else:
            print(word, '<unknown>', sep='\t')
        print()