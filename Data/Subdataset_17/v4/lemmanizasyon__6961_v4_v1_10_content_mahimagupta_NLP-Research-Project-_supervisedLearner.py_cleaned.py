hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'
def lemma_in(lemmas, lemma):
    for l in lemmas:
        if l["root"] != lemma["root"]:
            continue
        if l["tag1"] != lemma["tag1"]:
            continue
        if l["tag2"] != lemma["tag2"]:
            continue
        return True
    return False
def serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r', encoding='utf-8') as hindi_file:
        for line in hindi_file:
            if len(line) < 5 or line[0] == '
                continue
            columns = line.split("\t")
            if len(columns) < 5:
                continue
            word, root, tag1, tag2 = columns[1:5]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not lemma_in(dataset[word], lemma):
                dataset[word].append(lemma)
    if dest_file:
        with open(dest_file, 'w', encoding='utf-8') as out_file:
            lines = [
                '{}:{}\n'.format(word, ', '.join(serialize_lemma(lemma) for lemma in lemmas))
                for word, lemmas in dataset.items()
            ]
            out_file.writelines(lines)
    return dataset
def supervised_learn():
    training_data = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training_data.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
if __name__ == "__main__":
    supervised_learn()