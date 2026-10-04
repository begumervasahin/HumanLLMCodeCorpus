
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b6):
    return any(
        existing_lemma["root"] == b6["root"] and
        existing_lemma["tag1"] == b6["tag1"] and
        existing_lemma["b5"] == b6["b5"]
        for existing_lemma in lemmas
    )
def fonk2(b6):
    return f"[{b6['root']}, {b6['tag1']}, {b6['b5']}]"
def fonk3(input_file, b3 = None):
    b4 = {}
    with open(input_file, 'r') as file:
        for line in file:
            if len(line) < 5 or line.startswith('
                continue
            word, root, tag1, b5 = line.split("\t")[1:5]
            if word not in b4:
                b4[word] = []
            b6 = {"root": root, "tag1": tag1, "b5": b5}
            if not fonk1(b4[word], b6):
                b4[word].append(b6)
    if b3:
        with open(b3, 'w') as file:
            for word, lemmas in b4.items():
                b7 = ', '.join(fonk2(b6) for b6 in lemmas)
                file.write(f"{word}:{b7}\n")
    return b4
def fonk4():
    b8 = fonk3(b1, b2)
    for word, lemmas in b8.items():
        print(f"Processing word: {word} with {len(lemmas)} lemmas")
fonk4()