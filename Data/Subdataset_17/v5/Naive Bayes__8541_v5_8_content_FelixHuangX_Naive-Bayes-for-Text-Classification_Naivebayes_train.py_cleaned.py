import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def load_data_set(raw_path, stop_path):
    return fenci(raw_path, stop_path)
def create_unique_set(dataset, frequency_threshold=50):
    word_freq = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            word_freq[word] = word_freq.get(word, 0) + 1
        print(f"Processing document {i+1}/{len(dataset)}")
    filtered_words = {word: freq for word, freq in word_freq.items() if freq > frequency_threshold}
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words]
def words_to_vec(unique_words, input_doc):
    word_vector = [0] * len(unique_words)
    for word in input_doc:
        if word in unique_words:
            word_vector[unique_words.index(word)] += 1
    return word_vector
def train_naive_bayes(train_matrix, train_classes):
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    class_labels = set(train_classes)
    class_probs = []
    log_prob_vectors = []
    for cls in class_labels:
        class_count = train_classes.count(cls)
        class_prob = class_count / float(num_train_docs)
        class_probs.append(class_prob)
        word_counts = np.ones(num_words)
        total_count = 2.0
        for i in range(num_train_docs):
            if train_classes[i] == cls:
                word_counts += train_matrix[i]
                total_count += sum(train_matrix[i])
        print(f"Training class {cls}")
        log_prob_vectors.append(np.log(word_counts / total_count))
    return log_prob_vectors, class_probs
def save_model(unique_words, class_probs, log_prob_vectors, model_dir='models'):
    np.save(f'{model_dir}/pos.npy', np.array(class_probs))
    with open(f'{model_dir}/unique_set_list.txt', 'w') as file:
        for word in unique_words:
            file.write(f"{word}\n")
    np.save(f'{model_dir}/p_vectors.npy', np.array(log_prob_vectors))
if __name__ == "__main__":
    labels = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    stop_path = './cnews/cnews.vocab.txt'
    train_path = './cnews/cnews.train.txt'
    test_path = './cnews/cnews.test.txt'
    raw_features, raw_classes = load_data_set(train_path, stop_path)
    unique_set_list = create_unique_set(raw_features)
    train_matrix = [words_to_vec(unique_set_list, doc) for doc in raw_features]
    for i, _ in enumerate(train_matrix):
        print(f"Vectorizing document {i+1}/{len(train_matrix)}")
    p_vectors, pos_probabilities = train_naive_bayes(np.array(train_matrix), raw_classes)
    save_model(unique_set_list, pos_probabilities, p_vectors)
    print("Model training completed and parameters saved.")