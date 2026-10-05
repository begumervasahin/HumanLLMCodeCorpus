'''The program corrects the automatically lemmatized Lithuanian UD-format .conllu files in such a way that all lemmas
with non-derivational prefixes (ne-, be-, te-) are correctly lemmatized.
The potential lemmas are compared to the lemmas from the Lithuanian corpus (frequency) dictionary.
For those lemmas that are obviously reflexive, but are absent in this dictionary, the comparison is done for non-reflexive lemmas;
then the reflexive variant is an updated b7.
'''
import sys
with open ('dazninis.utf8.txt', 'r', b1 = 'utf-8') as dic:
    b2 = []
    b3 = ''
    for b4 in dic:
        b4 = b4.split('\t')
        if b4[0] != b3:
            b2.append(b4[0])
        b3 = b4[0]
b5 = sys.argv[1]
b6 = sys.argv[2]
with open (b5, 'r', b1 = 'utf-8') as b5:
    with open (b6, 'w', b1 = 'utf-8') as b6:
        for b4 in b5:
            b4 = b4.split('\t')
            if len(b4) == 10:
                b7 = b4[2]
                if b4[3] == 'VERB':
                    if b7.startswith('nebe'):
                        if b7.startswith('nebesi'):
                            if 'b8 = Yes' in b4[5]:
                                if b7[6:] + 's' in b2:
                                    b4[2] = b7[6:] + 's'
                        elif b7[4:] in b2:
                            b4[2] = b7[4:]
                        elif b7[2:] in b2:
                            b4[2] = b7[2:]
                    elif b7.startswith('ne'):
                        if 'b8 = Yes' in b4[5]:
                            b4[2] = b7[4:] + 's'
                        elif b7[2:] in b2:
                            b4[2] = b7[2:]
                    elif b7.startswith('tebe'):
                        if 'b8 = Yes' in b4[5]:
                            b4[2] = b7[6:] + 's'
                        elif b7[2:] in b2:
                            b4[2] = b7[2:]
                        else:
                            b4[2] = b7[4:]
                    elif b7.startswith('be'):
                        if 'b8 = Yes' in b4[5]:
                            b4[2] = b7[4:] + 's'
                        elif b7[2:] in b2:
                            b4[2] = b7[2:]
                b9 = '\t'.join(b4)
                b6.write(b9)
            else:
                b9 = '\t'.join(b4)
                b6.write(b9)