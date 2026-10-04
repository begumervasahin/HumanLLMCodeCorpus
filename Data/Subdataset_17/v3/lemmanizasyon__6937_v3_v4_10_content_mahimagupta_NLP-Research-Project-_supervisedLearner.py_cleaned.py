
HINDI_DIC_FILE = './datasets/hi_hdtb-ud-dev.conllu'
HINDI_OUT_FILE = './outputs/train_data.txt'
def is_same_lemma(existing_lemma, new_lemma):
    return (
        existing_lemma["root"] == new_lemma["root"] and
        existing_lemma["tag1"] == new_lemma["tag1"] and
        existing_lemma["tag2"] == new_lemma["tag2"]
    )
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def process_line(line):
    parts = line.split("\t")
    if len(parts) < 5:
        return None, None, None, None
    word, root, tag1, tag2 = parts[1:5]
    return word, root, tag1, tag2
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r', encoding='utf-8') as hindi_file:
        for line in hindi_file.readlines():
            if len(line) < 5 or line[0] == '\n':
                continue
            word, root, tag1, tag2 = process_line(line)
            if not word:
                continue
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if any(is_same_lemma(existing_lemma, lemma) for existing_lemma in dataset[word]):
                continue
            dataset[word].append(lemma)
    if dest_file is not None:
        write_output_file(dataset, dest_file)
    return dataset
def write_output_file(dataset, dest_file):
    with open(dest_file, 'w', encoding='utf-8') as out:
        lines = [
            '{}:{}\n'.format(word, ', '.join([serialize_lemma(lemma) for lemma in lemmas]))
            for word, lemmas in dataset.items()
        ]
        out.writelines(lines)
def supervised_learn():
    training_data = read_training_data(HINDI_DIC_FILE, HINDI_OUT_FILE)
    for word, lemmas in training_data.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
if __name__ == '__main__':
    supervised_learn()