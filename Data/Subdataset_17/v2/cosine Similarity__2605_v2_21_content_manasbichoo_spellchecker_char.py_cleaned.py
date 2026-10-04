import chars2vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
words_array = []
with open('words.txt', 'r') as f:
    for line in f:
        word = line.strip()
        words_array.append(word)
print("Words loaded:", words_array)
c2v_model = chars2vec.load_model('eng_50')
word_embeddings = c2v_model.vectorize_words(words_array)
print("Shape of word embeddings:", word_embeddings.shape)
word_input = input("Enter a word: ")
words_input = [word_input]
word_embed_input = c2v_model.vectorize_words(words_input)
print("Embedding for the input word:", word_embed_input)
similarities = cosine_similarity(word_embeddings, word_embed_input)
max_similarity_index = np.argmax(similarities)
max_similarity_value = np.max(similarities)
most_similar_word = words_array[max_similarity_index]
print("Most similar word:", most_similar_word)
print("Cosine similarity score:", max_similarity_value)