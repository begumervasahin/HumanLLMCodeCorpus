import sys
def fonk1(b10):
    b1 = []
    b2 = ''
    with open(b10, 'r', b3 = 'utf-8') as dictionary_file:
        for line in dictionary_file:
            word, *b4 = line.split('\t')
            if word != b2:
                b1.append(word)
            b2 = word
    return b1
def fonk2(lemma, pos_tag, b8, b12):
    if pos_tag != 'VERB':
        return lemma
    b5 = 'Reflex=Yes' in b8
    b6 = None
    if lemma.startswith('nebesi') and b5:
        b6 = lemma[6:] + 's' if lemma[6:] + 's' in b12 else None
    elif lemma.startswith('nebe'):
        b6 = lemma[4:] if lemma[4:] in b12 else lemma[2:] if lemma[2:] in b12 else None
    elif lemma.startswith('ne') or lemma.startswith('be'):
        b6 = (lemma[4:] + 's' if b5 else lemma[2:]) if lemma[2:] in b12 else None
    elif lemma.startswith('tebe'):
        b6 = lemma[6:] + 's' if b5 else lemma[4:] if lemma[4:] in b12 else lemma[2:]
    return b6 if b6 in b12 else lemma
def fonk3(input_file_path, b11, b12):
    with open(input_file_path, 'r', b3 = 'utf-8') as input_file, \
         open(b11, 'w', b3 = 'utf-8') as output_file:
        for line in input_file:
            b7 = line.strip().split('\t')
            if len(b7) == 10:
                lemma, pos_tag, b8 = b7[2], b7[3], b7[5]
                b9 = fonk2(lemma, pos_tag, b8, b12)
                b7[2] = b9
            output_file.write('\t'.join(b7) + '\n')
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: script.py <input_file> <output_file>")
        sys.exit(1)
    b10 = 'dazninis.utf8.txt'
    input_file_path, b11 = sys.argv[1], sys.argv[2]
    b12 = fonk1(b10)
    fonk3(input_file_path, b11, b12)
if b13 = = '__main__':
    fonk4()