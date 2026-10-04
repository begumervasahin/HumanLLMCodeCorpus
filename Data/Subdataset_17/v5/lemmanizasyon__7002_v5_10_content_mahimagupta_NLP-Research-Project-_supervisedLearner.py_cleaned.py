
HINDI_DIC_FILE = './datasets/hi_hdtb-ud-dev.conllu'
HINDI_OUT_FILE = './outputs/train_data.txt'
def lemma_exists(lemmas, lemma):
    return any(
        l["root"] == lemma["root"] and l["tag1"] == lemma["tag1"] and l["tag2"] == lemma["tag2"]
        for l in lemmas
    )
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r', encoding='utf-8') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line[0] == '
                continue
            parts = line.strip().split("\t")
            if len(parts) < 5:
                continue
            word, root, tag1, tag2 = parts[1:5]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not lemma_exists(dataset[word], lemma):
                dataset[word].append(lemma)
    if dest_file:
        with open(dest_file, 'w', encoding='utf-8') as out:
            for word, lemmas in dataset.items():
                serialized_lemmas = ', '.join(serialize_lemma(lemma) for lemma in lemmas)
                out.write('{}:{}\n'.format(word, serialized_lemmas))
    return dataset
def supervised_learn():
    training_data = read_training_data(HINDI_DIC_FILE, HINDI_OUT_FILE)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
if __name__ == "__main__":
    supervised_learn()