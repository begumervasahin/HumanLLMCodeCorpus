
HINDI_DIC_FILE = './datasets/hi_hdtb-ud-dev.conllu'
HINDI_OUT_FILE = './outputs/train_data.txt'
def is_lemma_in(lemmas, lemma):
    return any(all(existing_lemma[key] == lemma[key] for key in ("root", "tag1", "tag2")) for existing_lemma in lemmas)
def serialize_lemma(lemma):
    return f'[{lemma["root"]}, {lemma["tag1"]}, {lemma["tag2"]}]'
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r', encoding='utf-8') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line.startswith('
                continue
            fields = line.split("\t")
            word, root, tag1, tag2 = fields[1], fields[2], fields[3], fields[4]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not is_lemma_in(dataset[word], lemma):
                dataset[word].append(lemma)
    if dest_file is not None:
        with open(dest_file, 'w', encoding='utf-8') as output_file:
            for word, lemmas in dataset.items():
                serialized_lemmas = ', '.join(serialize_lemma(lemma) for lemma in lemmas)
                output_file.write(f'{word}:{serialized_lemmas}\n')
    return dataset
def supervised_learn():
    training_data = read_training_data(HINDI_DIC_FILE, HINDI_OUT_FILE)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
if __name__ == "__main__":
    supervised_learn()