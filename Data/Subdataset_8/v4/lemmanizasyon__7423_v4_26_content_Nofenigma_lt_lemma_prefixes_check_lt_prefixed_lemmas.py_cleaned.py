import sys
with open('dazninis.utf8.txt', 'r', encoding='utf-8') as dic:
    lt_lemmas = []
    word_0 = ''
    for line in dic:
        line = line.split('\t')
        if line[0] != word_0:
            lt_lemmas.append(line[0])
        word_0 = line[0]
file_path = sys.argv[1]
doc_path = sys.argv[2]
with open(file_path, 'r', encoding='utf-8') as file:
    with open(doc_path, 'w', encoding='utf-8') as doc:
        for line in file:
            line = line.split('\t')
            if len(line) == 10:
                lemma = line[2]
                if line[3] == 'VERB':
                    if lemma.startswith('nebe'):
                        if lemma.startswith('nebesi'):
                            if 'Reflex=Yes' in line[5]:
                                if lemma[6:] + 's' in lt_lemmas:
                                    line[2] = lemma[6:] + 's'
                        elif lemma[4:] in lt_lemmas:
                            line[2] = lemma[4:]
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]
                    elif lemma.startswith('ne'):
                        if 'Reflex=Yes' in line[5]:
                            line[2] = lemma[4:] + 's'
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]
                    elif lemma.startswith('tebe'):
                        if 'Reflex=Yes' in line[5]:
                            line[2] = lemma[6:] + 's'
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]
                        else:
                            line[2] = lemma[4:]
                    elif lemma.startswith('be'):
                        if 'Reflex=Yes' in line[5]:
                            line[2] = lemma[4:] + 's'
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]
                line1 = '\t'.join(line)
                doc.write(line1)
            else:
                line1 = '\t'.join(line)
                doc.write(line1)