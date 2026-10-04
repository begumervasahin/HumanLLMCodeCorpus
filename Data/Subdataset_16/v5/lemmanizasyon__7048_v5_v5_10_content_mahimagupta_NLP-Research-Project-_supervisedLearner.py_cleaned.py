import os
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemma1, lemma2):
    return all(lemma1[key] == lemma2[key] for key in ["root", "tag1", "b6"])
def fonk2(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["b6"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line.startswith('\n'):
                continue
            b5 = line.split("\t")
            if len(b5) < 5:
                continue
            word, root, tag1, b6 = b5[1:5]
            if word not in b4:
                b4[word] = []
            b7 = {"root": root, "tag1": tag1, "b6": b6}
            if not any(fonk1(existing_lemma, b7) for existing_lemma in b4[word]):
                b4[word].append(b7)
    if b3:
        with open(b3, 'w') as out_file:
            for word, lemmas in b4.items():
                b8 = ', '.join(fonk2(lemma) for lemma in lemmas)
                out_file.write(f'{word}:{b8}\n')
    return b4
def fonk4():
    b9 = fonk3(b1, b2)
    for word, lemmas in b9.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
os.makedirs(os.path.dirname(b2), b10 = True)
fonk4()