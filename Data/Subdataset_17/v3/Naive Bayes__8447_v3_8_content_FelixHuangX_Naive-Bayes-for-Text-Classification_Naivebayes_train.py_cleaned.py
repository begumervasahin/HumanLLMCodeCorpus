import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
def load_data_set(raw_path, stop_path):
    result, data_target = fenci(raw_path, stop_path)
    return result, data_target
def create_unique_set(dataset, min_occurrence=50):
    word_counts = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            word_counts[word] = word_counts.get(word, 0) + 1
        print(f"Processing document {i}")
    filtered_words = {word: count for word, count in word_counts.items() if count > min_occurrence}
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words]
def words_to_vec(unique_set_list, input_doc):
    word_vector = [0] * len(unique_set_list)
    for word in input_doc:
        if word in unique_set_list:
            word_vector[unique_set_list.index(word)] += 1
    return word_vector
def train_naive_bayes(train_mat, train_class):
    num_train_docs = len(train_mat)
    num_words = len(train_mat[0])
    unique_classes = set(train_class)
    p_target = []
    p_vec_list = []
    for class_label in unique_classes:
        class_prob = train_class.count(class_label) / float(num_train_docs)
        p_target.append(class_prob)
        word_counts = np.ones(num_words)
        total_words = 2.0
        for i in range(num_train_docs):
            if train_class[i] == class_label:
                word_counts += train_mat[i]
                total_words += sum(train_mat[i])
        print(f"Training class {class_label}")
        p_vec = np.log(word_counts / total_words)
        p_vec_list.append(p_vec)
    return p_vec_list, p_target
def save_model(pos_probs, unique_set_list, p_vec_list, model_dir='models'):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    np.save(os.path.join(model_dir, 'pos.npy'), np.array(pos_probs))
    with open(os.path.join(model_dir, 'unique_set_list.txt'), 'w') as file:
        for word in unique_set_list:
            file.write(f"{word}\n")
    np.save(os.path.join(model_dir, 'p_vec_list.npy'), np.array(p_vec_list))
def main():
    labels = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    stop_path = './cnews/cnews.vocab.txt'
    train_path = './cnews/cnews.train.txt'
    raw_features, raw_classes = load_data_set(train_path, stop_path)
    unique_set_list = create_unique_set(raw_features)
    train_mat = [words_to_vec(unique_set_list, doc) for doc in raw_features]
    for i, single_features in enumerate(raw_features):
        print(f"Processed document {i}")
    p_vec_list, pos_probs = train_naive_bayes(np.array(train_mat), raw_classes)
    save_model(pos_probs, unique_set_list, p_vec_list)
if __name__ == "__main__":
    main()