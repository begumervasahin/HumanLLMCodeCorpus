import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def load_words(file_path):
    words = []
    with open(file_path, 'r') as f:
        for line in f:
            word = line.strip()
            words.append(word)
    return words
def vectorize_words(model, words):
    return model.vectorize_words(words)
def calculate_similarity(embeddings, input_embedding):
    return cosine_similarity(embeddings, input_embedding)
def find_most_similar_word(words, similarities):
    max_similarity_index = np.argmax(similarities)
    max_similarity_value = np.max(similarities)
    most_similar_word = words[max_similarity_index]
    return most_similar_word, max_similarity_value
def main():
    words_array = load_words('words.txt')
    print("Words loaded:", words_array)
    c2v_model = chars2vec.load_model('eng_50')
    word_embeddings = vectorize_words(c2v_model, words_array)
    print("Shape of word embeddings:", word_embeddings.shape)
    input_word = input("Enter a word: ")
    input_words = [input_word]
    input_word_embedding = vectorize_words(c2v_model, input_words)
    print("Embedding for the input word:", input_word_embedding)
    similarities = calculate_similarity(word_embeddings, input_word_embedding)
    most_similar_word, max_similarity = find_most_similar_word(words_array, similarities)
    print("Most similar word:", most_similar_word)
    print("Cosine similarity score:", max_similarity)
    '''
    projection_2d = sklearn.decomposition.PCA(n_components=2).fit_transform(word_embeddings)
    plt.figure(figsize=(8, 6))
    for j in range(len(projection_2d)):
        plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                    marker=('$' + words_array[j] + '$'),
                    s=500 * len(words_array[j]), label=j,
                    facecolors='green' if words_array[j]
                                in ['Natural', 'Language', 'Understanding'] else 'black')
    plt.title('2D Projection of Word Embeddings')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
    '''
if __name__ == "__main__":
    main()