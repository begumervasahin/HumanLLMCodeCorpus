import json
import re
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from data_utils import savedata
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
def extract_tokens_from_binary_parse(parse):
    return parse.replace('(', ' ').replace(')', ' ').replace('-LRB-', '(').replace('-RRB-', ')').split()
def yield_examples(fn, skip_no_majority=True, limit=None):
    with open(fn, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if limit and i >= limit:
                break
            data = json.loads(line)
            label = data['gold_label']
            s1 = ' '.join(extract_tokens_from_binary_parse(data['sentence1_binary_parse']))
            s2 = ' '.join(extract_tokens_from_binary_parse(data['sentence2_binary_parse']))
            if skip_no_majority and label == '-':
                continue
            yield (label, s1, s2)
def clean_data(sentence_list):
    clean_sentences = []
    for sentence in sentence_list:
        sentence = re.sub(r"[^a-zA-Z]", " ", sentence)
        words = sentence.lower().split()
        words = [ps.stem(w) for w in words]
        clean_sentences.append(" ".join(words))
    return clean_sentences
def preprocess(fn, limit=None):
    raw_data = list(yield_examples(fn=fn, limit=limit))
    left_sentences = [s1 for _, s1, _ in raw_data]
    right_sentences = [s2 for _, _, s2 in raw_data]
    left_clean = clean_data(left_sentences)
    right_clean = clean_data(right_sentences)
    LABELS = {'contradiction': 0, 'neutral': 1, 'entailment': 2}
    Y = np.array([LABELS[label] for label, _, _ in raw_data])
    return left_clean, right_clean, Y
def main():
    train = preprocess('snli_1.0/snli_1.0_train.jsonl')
    test = preprocess('snli_1.0/snli_1.0_test.jsonl')
    dev = preprocess('snli_1.0/snli_1.0_dev.jsonl')
    savedata(test, "test_stem")
    savedata(train, "train_stem")
    savedata(dev, "dev_stem")
if __name__ == '__main__':
    main()