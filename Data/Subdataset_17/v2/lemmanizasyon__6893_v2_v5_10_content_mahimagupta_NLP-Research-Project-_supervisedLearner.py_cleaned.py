
HINDI_DIC_FILE = './datasets/hi_hdtb-ud-dev.conllu'
HINDI_OUT_FILE = './outputs/train_data.txt'
def are_lemmas_equal(lemma1, lemma2):
    return all(lemma1[key] == lemma2[key] for key in ["root", "tag1", "tag2"])
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r', encoding='utf-8') as hindi_file:
        for line in hindi_file.readlines():
            if len(line) < 5 or line.startswith('\n'):
                continue
            word, root, tag1, tag2 = line.split("\t")[1:5]
            if word not in dataset:
                dataset[word] = []
            new_lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if any(are_lemmas_equal(existing_lemma, new_lemma) for existing_lemma in dataset[word]):
                continue
            dataset[word].append(new_lemma)
    if dest_file:
        with open(dest_file, 'w', encoding='utf-8') as out_file:
            for word, lemmas in dataset.items():
                serialized_lemmas = ', '.join(serialize_lemma(lemma) for lemma in lemmas)
                out_file.write(f'{word}:{serialized_lemmas}\n')
    return dataset
def supervised_learn():
    training_data = read_training_data(HINDI_DIC_FILE, HINDI_OUT_FILE)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
if __name__ == "__main__":
    supervised_learn()