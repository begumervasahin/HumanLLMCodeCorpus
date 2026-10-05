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
    string = re.sub(r"\'s|\'ve|n\'t|\'re|\'d|\'ll", lambda x: " " + x.group() + " ", string)
    string = re.sub(r",|!|\(|\)|\?", lambda x: " " + x.group() + " ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()
def load_examples(file_path):
    with open(file_path, 'r') as file:
        examples = [clean_str(line.strip()) for line in file.readlines()]
    return examples
def sample_fraction(examples, fraction):
    return random.sample(examples, int(len(examples) * fraction))
def load_data_and_labels(dataset_fraction):
    print("\tdata_helpers: loading positive examples...")
    positive_examples = load_examples(POS_DATASET_PATH)
    print("\tdata_helpers: [OK]")
    print("\tdata_helpers: loading negative examples...")
    negative_examples = load_examples(NEG_DATASET_PATH)
    print("\tdata_helpers: [OK]")
    positive_examples = sample_fraction(positive_examples, dataset_fraction)
    negative_examples = sample_fraction(negative_examples, dataset_fraction)
    x_text = positive_examples + negative_examples
    print("\tdata_helpers: generating labels...")
    positive_labels = np.array([[0, 1] for _ in positive_examples])
    negative_labels = np.array([[1, 0] for _ in negative_examples])
    y = np.concatenate([positive_labels, negative_labels], axis=0)
    print("\tdata_helpers: [OK]")
    return [x_text, y]
def pad_sentences(sentences, max_length, padding_word="<PAD/>"):
    padded_sentences = [sentence + [padding_word] * (max_length - len(sentence)) for sentence in sentences]
    return padded_sentences
def build_vocab():
    with open(VOC_PATH, 'r') as file:
        voc = csv.reader(file)
        vocabulary = {word: index for index, word in voc}
    with open(VOC_INV_PATH, 'r') as file:
        voc_inv = csv.reader(file)
        vocabulary_inv = [row for row in voc_inv]
    return vocabulary, vocabulary_inv
def build_input_data(sentences, labels, vocabulary):
    x = np.array([[vocabulary[word] for word in sentence] for sentence in sentences])
    y = np.array(labels)
    return x, y
def string_to_int(sentence, vocabulary, max_length):
    cleaned_sentence = clean_str(sentence)
    split_sentence = cleaned_sentence.split(" ")
    padded_sentence = pad_sentences([split_sentence], max_length)[0]
    x = np.array([vocabulary.get(word, vocabulary['<PAD/>']) for word in padded_sentence])
    return x
def load_data(dataset_fraction):
    sentences, labels = load_data_and_labels(dataset_fraction)
    max_length = max(len(sentence.split(" ")) for sentence in sentences)
    print("\tdata_helpers: building vocabulary...")
    vocabulary, vocabulary_inv = build_vocab()
    print("\tdata_helpers: [OK]")
    print("\tdata_helpers: building processed datasets...")
    x, y = build_input_data(sentences, labels, vocabulary)
    print("\tdata_helpers: [OK]")
    return x, y, vocabulary, vocabulary_inv
def batch_iter(data, batch_size, num_epochs):
    data_size = len(data)
    num_batches_per_epoch = (data_size + batch_size - 1)
    for epoch in range(num_epochs):
        shuffle_indices = np.random.permutation(np.arange(data_size))
        shuffled_data = data[shuffle_indices]
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]