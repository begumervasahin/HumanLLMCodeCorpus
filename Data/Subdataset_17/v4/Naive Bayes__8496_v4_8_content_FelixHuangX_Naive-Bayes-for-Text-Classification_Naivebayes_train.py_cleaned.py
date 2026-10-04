import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def load_data_set(raw_path, stop_path):
    result, data_target = fenci(raw_path, stop_path)
    return result, data_target
def create_unique_set(dataset):
    unique_set = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            if word in unique_set:
                unique_set[word] += 1
            else:
                unique_set[word] = 1
        print(f"Processing document {i+1}/{len(dataset)}")
    unique_set = {k: v for k, v in unique_set.items() if v > 50}
    sorted_items = sorted(unique_set.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items]
def words_to_vec(unique_set_list, input_doc):
    return_vec = [0] * len(unique_set_list)
    for word in input_doc:
        if word in unique_set_list:
            return_vec[unique_set_list.index(word)] += 1
    return return_vec
def train_naive_bayes(train_matrix, train_classes):
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    data_classes = set(train_classes)
    p_target = []
    p_vec_list = []
    for cls in data_classes:
        class_count = train_classes.count(cls)
        pos_sample_rate = class_count / float(num_train_docs)
        p_target.append(pos_sample_rate)
        p_num = np.ones(num_words)
        p_denom = 2.0
        for i in range(num_train_docs):
            if train_classes[i] == cls:
                p_num += train_matrix[i]
                p_denom += sum(train_matrix[i])
        print(f"Training class {cls}")
        p_vec = np.log(p_num / p_denom)
        p_vec_list.append(p_vec)
    return p_vec_list, p_target
if __name__ == "__main__":
    labels = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    stop_path = './cnews/cnews.vocab.txt'
    train_path = './cnews/cnews.train.txt'
    test_path = './cnews/cnews.test.txt'
    raw_features, raw_classes = load_data_set(train_path, stop_path)
    unique_set_list = create_unique_set(raw_features)
    train_matrix = []
    for i, single_features in enumerate(raw_features):
        train_matrix.append(words_to_vec(unique_set_list, single_features))
        print(f"Vectorizing document {i+1}/{len(raw_features)}")
    p_vectors, pos_probabilities = train_naive_bayes(np.array(train_matrix), raw_classes)
    np.save('models/pos.npy', np.array(pos_probabilities))
    with open('models/unique_set_list.txt', 'w') as file:
        for word in unique_set_list:
            file.write(f"{word}\n")
    np.save('models/p_vectors.npy', np.array(p_vectors))
    print("Model training completed and parameters saved.")