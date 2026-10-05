
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b6):
    for l in lemmas:
        if all(l[key] == b6[key] for key in ("root", "tag1", "b5")):
            return True
    return False
def fonk2(b6):
    return '[{}, {}, {}]'.format(b6["root"], b6["tag1"], b6["b5"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line[0] == '
                continue
            word, root, tag1, b5 = line.split("\t")[1:1+4]
            if word not in b4:
                b4[word] = []
            b6 = {"root": root, "tag1": tag1, "b5": b5}
            if not fonk1(b4[word], b6):
                b4[word].append(b6)
    if b3 is not None:
        with open(b3, 'w') as output_file:
            b7 = [f'{word}:{", ".join([fonk2(l) for l in lemmas])}\n' for word, lemmas in b4.items()]
            output_file.writelines(b7)
    return b4
def fonk4():
    b8 = fonk3(b1, b2)
    for word, lemmas in b8.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
fonk4()