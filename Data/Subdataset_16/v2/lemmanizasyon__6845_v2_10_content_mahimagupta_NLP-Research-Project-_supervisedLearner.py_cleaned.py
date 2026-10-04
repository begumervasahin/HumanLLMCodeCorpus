
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b8):
    for existing_lemma in lemmas:
        if (existing_lemma["root"] == b8["root"] and
                existing_lemma["tag1"] == b8["tag1"] and
                existing_lemma["b7"] == b8["b7"]):
            return True
    return False
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b7"])
def fonk3(input_file, b3 = None):
    b4 = {}
    with open(input_file, 'r', b5 = 'utf-8') as file:
        for line in file:
            if len(line) < 5 or line.startswith('
                continue
            b6 = line.strip().split("\t")
            if len(b6) < 4:
                continue
            word, root, tag1, b7 = b6[1:5]
            if word not in b4:
                b4[word] = []
            b8 = {"root": root, "tag1": tag1, "b7": b7}
            if not fonk1(b4[word], b8):
                b4[word].append(b8)
    if b3:
        with open(b3, 'w', b5 = 'utf-8') as file:
            for word, lemmas in b4.items():
                b9 = ', '.join([fonk2(b8) for b8 in lemmas])
                file.write('{}:{}\n'.format(word, b9))
    return b4
def fonk4():
    b10 = fonk3(b1, b2)
    for word, lemmas in b10.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
if b11 = = "__main__":
    fonk4()