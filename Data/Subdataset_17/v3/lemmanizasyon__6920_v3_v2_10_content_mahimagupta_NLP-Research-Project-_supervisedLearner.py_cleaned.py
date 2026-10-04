
HINDI_DIC_FILE = './datasets/hi_hdtb-ud-dev.conllu'
HINDI_OUT_FILE = './outputs/train_data.txt'
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
            if is_valid_line(line):
                process_line(line, dataset)
    if output_file:
        write_dataset_to_file(dataset, output_file)
    return dataset
def is_valid_line(line):
    return len(line) >= 5 and not line.startswith('
def process_line(line, dataset):
    columns = line.split("\t")
    if len(columns) < 5:
        return
    word, root, tag1, tag2 = columns[1:5]
    lemma = {"root": root, "tag1": tag1, "tag2": tag2}
    if word not in dataset:
        dataset[word] = []
    if not is_lemma_present(dataset[word], lemma):
        dataset[word].append(lemma)
def write_dataset_to_file(dataset, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, lemmas in dataset.items():
            lemmas_str = ', '.join([serialize_lemma(lemma) for lemma in lemmas])
            file.write(f'{word}:{lemmas_str}\n')
def supervised_learning():
    training_data = read_training_data(HINDI_DIC_FILE, HINDI_OUT_FILE)
    for word, lemmas in training_data.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
supervised_learning()