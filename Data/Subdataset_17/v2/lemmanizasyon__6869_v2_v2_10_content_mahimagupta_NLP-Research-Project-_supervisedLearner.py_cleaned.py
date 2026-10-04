
hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'
def is_lemma_present(lemmas, lemma):
    for existing_lemma in lemmas:
        if (existing_lemma["root"] == lemma["root"] and
            existing_lemma["tag1"] == lemma["tag1"] and
            existing_lemma["tag2"] == lemma["tag2"]):
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
            columns = line.split("\t")
            if len(columns) < 5:
                continue
            word, root, tag1, tag2 = columns[1:5]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not is_lemma_present(dataset[word], lemma):
                dataset[word].append(lemma)
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, lemmas in dataset.items():
                lemmas_str = ', '.join([serialize_lemma(lemma) for lemma in lemmas])
                file.write(f'{word}:{lemmas_str}\n')
    return dataset
def supervised_learning():
    training_data = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
supervised_learning()