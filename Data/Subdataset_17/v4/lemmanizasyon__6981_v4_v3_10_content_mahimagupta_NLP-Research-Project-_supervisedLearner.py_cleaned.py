
hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'
def is_lemma_in(lemmas, lemma):
    for existing_lemma in lemmas:
        if all(existing_lemma[key] == lemma[key] for key in ("root", "tag1", "tag2")):
            return True
    return False
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_file, output_file=None):
    dataset = {}
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line) < 5 or line.startswith('
                continue
            parts = line.split("\t")
            word = parts[1]
            root = parts[2]
            tag1 = parts[3]
            tag2 = parts[4]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not is_lemma_in(dataset[word], lemma):
                dataset[word].append(lemma)
    if output_file is not None:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, lemmas in dataset.items():
                line = '{}: {}\n'.format(word, ', '.join([serialize_lemma(l) for l in lemmas]))
                file.write(line)
    return dataset
def supervised_learn():
    training_data = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
supervised_learn()