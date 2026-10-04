
HINDI_DIC_FILE = './datasets/hi_hdtb-ud-dev.conllu'
HINDI_OUT_FILE = './outputs/train_data.txt'
def is_lemma_in(lemmas, lemma):
    return any(
        l["root"] == lemma["root"] and l["tag1"] == lemma["tag1"] and l["tag2"] == lemma["tag2"]
        for l in lemmas
    )
def serialize_lemma(lemma):
    return f"[{lemma['root']}, {lemma['tag1']}, {lemma['tag2']}]"
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line.startswith('
                continue
            word, root, tag1, tag2 = line.split("\t")[1:5]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not is_lemma_in(dataset[word], lemma):
                dataset[word].append(lemma)
    if dest_file is not None:
        with open(dest_file, 'w') as output_file:
            lines = [
                f"{word}:{', '.join(serialize_lemma(lemma) for lemma in lemmas)}\n"
                for word, lemmas in dataset.items()
            ]
            output_file.writelines(lines)
    return dataset
def supervised_learn():
    training_data = read_training_data(HINDI_DIC_FILE, HINDI_OUT_FILE)
    for word, lemmas in training_data.items():
        print(f"Processing word: {word} with {len(lemmas)} lemmas")
supervised_learn()