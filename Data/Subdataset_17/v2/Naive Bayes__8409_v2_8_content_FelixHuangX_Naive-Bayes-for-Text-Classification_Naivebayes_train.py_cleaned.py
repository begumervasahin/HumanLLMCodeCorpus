import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
def load_data_set(raw_path, stop_path):
    result, data_target = fenci(raw_path, stop_path)
    return result, data_target
def create_unique_set(dataset):
    unique_set = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            unique_set[word] = unique_set.get(word, 0) + 1
        print(f"Processing document {i}")
    unique_set = {k: v for k, v in unique_set.items() if v > 50}
    sorted_items = sorted(unique_set.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_items]
def words_to_vec(unique_set_list, input_doc):
    return_vec = [0] * len(unique_set_list)
    for word in input_doc:
        if word in unique_set_list:
            return_vec[unique_set_list.index(word)] += 1
    return return_vec
def train_naive_bayes(train_mat, train_class):
    num_train_docs = len(train_mat)
    num_words = len(train_mat[0])
    data_classes = set(train_class)
    p_target = []
    p_vec_list = []
    for class_label in data_classes:
        class_prob = train_class.count(class_label) / float(num_train_docs)
        p_target.append(class_prob)
        p_num = np.ones(num_words)
        p_sum = 2.0
        for i in range(num_train_docs):
            if train_class[i] == class_label:
                p_num += train_mat[i]
                p_sum += sum(train_mat[i])
        print(f"Training class {class_label}")
        p_vec = np.log(p_num / p_sum)
        p_vec_list.append(p_vec)
    return p_vec_list, p_target
if __name__ == "__main__":
    labels = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    stop_path = './cnews/cnews.vocab.txt'
    train_path = './cnews/cnews.train.txt'
    test_path = './cnews/cnews.test.txt'
    raw_features, raw_classes = load_data_set(train_path, stop_path)
    unique_set_list = create_unique_set(raw_features)
    train_mat = [words_to_vec(unique_set_list, doc) for doc in raw_features]
    for i, single_features in enumerate(raw_features):
        print(f"Processed document {i}")
    p_vec_list, pos_probs = train_naive_bayes(np.array(train_mat), raw_classes)
    if not os.path.exists('models'):
        os.makedirs('models')
    np.save('models/pos.npy', np.array(pos_probs))
    with open('models/unique_set_list.txt', 'w') as file:
        for word in unique_set_list:
            file.write(f"{word}\n")
    np.save('models/p_vec_list.npy', np.array(p_vec_list))