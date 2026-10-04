import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
wordnet_lemmatizer = WordNetLemmatizer()
def read_titles(filename):
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f]
titles = read_titles('all_book_titles.txt')
def read_stopwords(filename):
    with open(filename, 'r') as f:
        return set(w.rstrip() for w in f)
stopwords = read_stopwords('stopwords.txt')
custom_stopwords = {
    'introduction', 'edition', 'series', 'application',
    'approach', 'card', 'access', 'package', 'plus', 'etext',
    'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
    'third', 'second', 'fourth',
}
stopwords.update(custom_stopwords)
def my_tokenizer(s, lemmatizer, stopwords):
    s = s.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [t for t in tokens if len(t) > 2]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    tokens = [t for t in tokens if t not in stopwords]
    tokens = [t for t in tokens if not any(c.isdigit() for c in t)]
    return tokens
def process_titles(titles, lemmatizer, stopwords):
    word_index_map = {}
    index_word_map = []
    all_tokens = []
    current_index = 0
    for title in titles:
        try:
            title = title.encode('ascii', 'ignore').decode('utf-8')
            tokens = my_tokenizer(title, lemmatizer, stopwords)
            all_tokens.append(tokens)
            for token in tokens:
                if token not in word_index_map:
                    word_index_map[token] = current_index
                    index_word_map.append(token)
                    current_index += 1
        except Exception as e:
            print(f"Error processing title: {title} - {e}")
    return all_tokens, word_index_map, index_word_map
all_tokens, word_index_map, index_word_map = process_titles(titles, wordnet_lemmatizer, stopwords)
def tokens_to_vector(tokens, word_index_map):
    x = np.zeros(len(word_index_map))
    for t in tokens:
        if t in word_index_map:
            x[word_index_map[t]] = 1
    return x
def create_matrix(all_tokens, word_index_map):
    D = len(word_index_map)
    N = len(all_tokens)
    X = np.zeros((D, N))
    for i, tokens in enumerate(all_tokens):
        X[:, i] = tokens_to_vector(tokens, word_index_map)
    return X
X = create_matrix(all_tokens, word_index_map)
def perform_svd(X, n_components=2):
    svd = TruncatedSVD(n_components=n_components)
    return svd.fit_transform(X)
Z = perform_svd(X)
def plot_svd(Z, index_word_map):
    plt.figure(figsize=(10, 8))
    plt.scatter(Z[:, 0], Z[:, 1])
    for i, word in enumerate(index_word_map):
        plt.annotate(s=word, xy=(Z[i, 0], Z[i, 1]))
    plt.title('Truncated SVD of Book Titles')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.grid(True)
    plt.show()
plot_svd(Z, index_word_map)