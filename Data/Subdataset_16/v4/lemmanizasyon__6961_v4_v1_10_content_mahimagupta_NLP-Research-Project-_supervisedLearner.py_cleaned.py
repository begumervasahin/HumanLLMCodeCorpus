b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b8):
    for l in lemmas:
        if l["root"] != b8["root"]:
            continue
        if l["tag1"] != b8["tag1"]:
            continue
        if l["b7"] != b8["b7"]:
            continue
        return True
    return False
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b7"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r', b5 = 'utf-8') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line[0] == '
                continue
            b6 = line.split("\t")
            if len(b6) < 5:
                continue
            word, root, tag1, b7 = b6[1:5]
            if word not in b4:
                b4[word] = []
            b8 = {"root": root, "tag1": tag1, "b7": b7}
            if not fonk1(b4[word], b8):
                b4[word].append(b8)
    if b3:
        with open(b3, 'w', b5 = 'utf-8') as out_file:
            b9 = [
                '{}:{}\n'.format(word, ', '.join(fonk2(b8) for b8 in lemmas))
                for word, lemmas in b4.items()
            ]
            out_file.writelines(b9)
    return b4
def fonk4():
    b10 = fonk3(b1, b2)
    for word, lemmas in b10.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
if b11 = = "__main__":
    fonk4()