import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
words_array = []
with open('words.txt', 'r') as f:
    for word in f.read().split():
        words_array.append(str(word))
print("Words loaded:", words_array)
c2v_model = chars2vec.load_model('eng_50')
word_embeddings = c2v_model.vectorize_words(words_array)
print("Shape of word embeddings:", word_embeddings.shape)
input_word = str(input("Enter a word: "))
input_words = [input_word]
input_word_embedding = c2v_model.vectorize_words(input_words)
print("Embedding for the input word:", input_word_embedding)
similarities = cosine_similarity(word_embeddings, input_word_embedding)
max_similarity = np.max(similarities)
max_similarity_index = np.argmax(similarities)
most_similar_word = words_array[max_similarity_index]
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