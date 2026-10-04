import os
hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'
def are_lemmas_equal(lemma1, lemma2):
    return all(lemma1[key] == lemma2[key] for key in ["root", "tag1", "tag2"])
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line.startswith('\n'):
                continue
            fields = line.split("\t")
            if len(fields) < 5:
                continue
            word, root, tag1, tag2 = fields[1:5]
            if word not in dataset:
                dataset[word] = []
            new_lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not any(are_lemmas_equal(existing_lemma, new_lemma) for existing_lemma in dataset[word]):
                dataset[word].append(new_lemma)
    if dest_file:
        with open(dest_file, 'w') as out_file:
            for word, lemmas in dataset.items():
                serialized_lemmas = ', '.join(serialize_lemma(lemma) for lemma in lemmas)
                out_file.write(f'{word}:{serialized_lemmas}\n')
    return dataset
def supervised_learn():
    training_data = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
os.makedirs(os.path.dirname(hindi_out_file), exist_ok=True)
supervised_learn()