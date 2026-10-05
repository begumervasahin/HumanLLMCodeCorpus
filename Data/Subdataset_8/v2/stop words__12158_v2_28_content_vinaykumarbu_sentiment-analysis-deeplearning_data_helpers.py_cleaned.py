import numpy as np
import re
import random
import csv
POS_DATASET_PATH = 'twitter-sentiment-dataset/tw-data.pos'
NEG_DATASET_PATH = 'twitter-sentiment-dataset/tw-data.neg'
VOC_PATH = 'twitter-sentiment-dataset/vocab.csv'
VOC_INV_PATH = 'twitter-sentiment-dataset/vocab_inv.csv'
def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r'(.)\1+', r'\1\1', string)
    string = re.sub(r"\'s", " 's", string)
    string = re.sub(r"\'ve", " 've", string)
    string = re.sub(r"n\'t", " n't", string)
    string = re.sub(r"\'re", " 're", string)
    string = re.sub(r"\'d", " 'd", string)
    string = re.sub(r"\'ll", " 'll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " ( ", string)
    string = re.sub(r"\)", " ) ", string)
    string = re.sub(r"\?", " ? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()
def sample_list(lst, fraction):
    return random.sample(lst, int(len(lst) * fraction))
def load_data_and_labels(dataset_fraction):
    print("Loading and processing data...")
    positive_examples = [line.strip() for line in open(POS_DATASET_PATH).readlines()]
    negative_examples = [line.strip() for line in open(NEG_DATASET_PATH).readlines()]
    positive_examples = sample_list(positive_examples, dataset_fraction)
    negative_examples = sample_list(negative_examples, dataset_fraction)
    x_text = positive_examples + negative_examples
    print("Cleaning strings...")
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [sent.split(" ") for sent in x_text]
    print("Generating labels...")
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return x_text, y
def pad_sentences(sentences, padding_word="<PAD/>"):
    max_len = max(len(sentence) for sentence in sentences)
    padded_sentences = [sentence + [padding_word] * (max_len - len(sentence)) for sentence in sentences]
    return padded_sentences
def build_vocab():
    voc = csv.reader(open(VOC_PATH))
    voc_inv = csv.reader(open(VOC_INV_PATH))
    vocabulary_inv = [x for x in voc_inv]
    vocabulary = {x: i for x, i in voc}
    return vocabulary, vocabulary_inv
def build_input_data(sentences, labels, vocabulary):
    x = np.array([[vocabulary[word] for word in sentence] for sentence in sentences])
    y = np.array(labels)
    return x, y
def load_data(dataset_fraction):
    x_text, labels = load_data_and_labels(dataset_fraction)
    print("Padding strings...")
    sentences_padded = pad_sentences(x_text)
    print("Building vocabulary...")
    vocabulary, vocabulary_inv = build_vocab()
    print("Building processed datasets...")
    x, y = build_input_data(sentences_padded, labels, vocabulary)
    return x, y, vocabulary, vocabulary_inv
def batch_iter(data, batch_size, num_epochs):
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(len(data) / batch_size) + 1
    for epoch in range(num_epochs):
        shuffle_indices = np.random.permutation(np.arange(data_size))
        shuffled_data = data[shuffle_indices]
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
if __name__ == "__main__":
    dataset_fraction = 0.8
    x, y, vocabulary, vocabulary_inv = load_data(dataset_fraction)
