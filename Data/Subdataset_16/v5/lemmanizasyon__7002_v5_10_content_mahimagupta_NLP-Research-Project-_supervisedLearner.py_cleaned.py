
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b8):
    return any(
        l["root"] == b8["root"] and l["tag1"] == b8["tag1"] and l["b7"] == b8["b7"]
        for l in lemmas
    )
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b7"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r', b5 = 'utf-8') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line[0] == '
                continue
            b6 = line.strip().split("\t")
            if len(b6) < 5:
                continue
            word, root, tag1, b7 = b6[1:5]
            if word not in b4:
                b4[word] = []
            b8 = {"root": root, "tag1": tag1, "b7": b7}
            if not fonk1(b4[word], b8):
                b4[word].append(b8)
    if b3:
        with open(b3, 'w', b5 = 'utf-8') as out:
            for word, lemmas in b4.items():
                b9 = ', '.join(fonk2(b8) for b8 in lemmas)
                out.write('{}:{}\n'.format(word, b9))
    return b4
def fonk4():
    b10 = fonk3(b1, b2)
    for word, lemmas in b10.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
if b11 = = "__main__":
    fonk4()