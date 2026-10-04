
hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'
def _lemma_in(lemmas, lemma):
    for l in lemmas:
        if l["root"] == lemma["root"] and l["tag1"] == lemma["tag1"] and l["tag2"] == lemma["tag2"]:
            return True
    return False
def _serialize_lemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])
def read_training_data(input_training_file, dest_file=None):
    dataset = {}
    with open(input_training_file, 'r', encoding='utf-8') as hindi_file:
        for ln in hindi_file.readlines():
            if len(ln) < 5 or ln[0] == '
                continue
            parts = ln.strip().split("\t")
            if len(parts) < 5:
                continue
            word, root, tag1, tag2 = parts[1:1+4]
            if word not in dataset:
                dataset[word] = []
            lemma = {"root": root, "tag1": tag1, "tag2": tag2}
            if not _lemma_in(dataset[word], lemma):
                dataset[word].append(lemma)
    if dest_file:
        with open(dest_file, 'w', encoding='utf-8') as out:
            lines = []
            for word, lemmas in dataset.items():
                serialized_lemmas = ', '.join([_serialize_lemma(lemma) for lemma in lemmas])
                lines.append('{}:{}\n'.format(word, serialized_lemmas))
            out.writelines(lines)
    return dataset
def supervised_learn():
    training_data = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training_data.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
supervised_learn()