import chars2vec
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
    word_input = input("Enter a word: ")
    words_input = [word_input]
    word_embed_input = vectorize_words(c2v_model, words_input)
    print("Embedding for the input word:", word_embed_input)
    similarities = calculate_similarity(word_embeddings, word_embed_input)
    most_similar_word, max_similarity_value = find_most_similar_word(words_array, similarities)
    print("Most similar word:", most_similar_word)
    print("Cosine similarity score:", max_similarity_value)
if __name__ == "__main__":
    main()