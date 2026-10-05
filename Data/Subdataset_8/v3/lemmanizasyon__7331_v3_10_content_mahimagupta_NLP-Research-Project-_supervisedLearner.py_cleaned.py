
hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'
def is_lemma_in(lemmas, lemma):
    for l in lemmas:
        if all(l[key] == lemma[key] for key in ("root", "tag1", "tag2")):
            return True
    return False
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line[0] == '
                continue
            word, root, tag1, tag2 = line.split("\t")[1:1+4]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not is_lemma_in(dataset[word], lemma):
                dataset[word].append(lemma)
    if dest_file is not None:
        with open(dest_file, 'w') as output_file:
            lines = [f'{word}:{", ".join([serialize_lemma(l) for l in lemmas])}\n' for word, lemmas in dataset.items()]
            output_file.writelines(lines)
    return dataset
def supervised_learn():
    training_data = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
supervised_learn()