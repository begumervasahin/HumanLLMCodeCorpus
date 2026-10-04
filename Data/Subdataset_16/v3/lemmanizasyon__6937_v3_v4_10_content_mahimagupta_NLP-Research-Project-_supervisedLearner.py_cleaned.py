
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(existing_lemma, new_lemma):
    return (
        existing_lemma["root"] == new_lemma["root"] and
        existing_lemma["tag1"] == new_lemma["tag1"] and
        existing_lemma["b4"] == new_lemma["b4"]
    )
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b4"])
def fonk3(line):
    b3 = line.split("\t")
    if len(b3) < 5:
        return None, None, None, None
    word, root, tag1, b4 = b3[1:5]
    return word, root, tag1, b4
def fonk4(input_training_file, b5 = None):
    b6 = {}
    with open(input_training_file, 'r', b7 = 'utf-8') as hindi_file:
        for line in hindi_file.readlines():
            if len(line) < 5 or line[0] == '\n':
                continue
            word, root, tag1, b4 = fonk3(line)
            if not word:
                continue
            if word not in b6:
                b6[word] = []
            b8 = {"root": root, "tag1": tag1, "b4": b4}
            if any(fonk1(existing_lemma, b8) for existing_lemma in b6[word]):
                continue
            b6[word].append(b8)
    if b5 is not None:
        fonk5(b6, b5)
    return b6
def fonk5(b6, b5):
    with open(b5, 'w', b7 = 'utf-8') as out:
        b9 = [
            '{}:{}\n'.format(word, ', '.join([fonk2(b8) for b8 in lemmas]))
            for word, lemmas in b6.items()
        ]
        out.writelines(b9)
def fonk6():
    b10 = fonk4(b1, b2)
    for word, lemmas in b10.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
if b11 = = '__main__':
    fonk6()