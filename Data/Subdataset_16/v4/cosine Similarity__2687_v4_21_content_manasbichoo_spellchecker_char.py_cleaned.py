import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
b1 = []
with open('words.txt', 'r') as f:
    for word in f.read().split():
        b1.append(str(word))
print("Words loaded:", b1)
b2 = chars2vec.load_model('eng_50')
b3 = b2.vectorize_words(b1)
print("Shape of word embeddings:", b3.shape)
b4 = str(input("Enter a word: "))
b5 = [b4]
b6 = b2.vectorize_words(b5)
print("Embedding for the input word:", b6)
b7 = cosine_similarity(b3, b6)
b8 = np.max(b7)
b9 = np.argmax(b7)
b10 = b1[b9]
print("Most similar word:", b10)
print("Cosine similarity score:", b8)
'''
b11 = sklearn.decomposition.PCA(n_components=2).fit_transform(b3)
plt.figure(b12 = (8, 6))
for j in range(len(b11)):
    plt.scatter(b11[j, 0], b11[j, 1],
                b13 = ('$' + b1[j] + '$'),
                b14 = 500 * len(b1[j]), label=j,
                b15 = 'green' if b1[j]
                            in ['Natural', 'Language', 'Understanding'] else 'black')
plt.title('2D Projection of Word Embeddings')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()
'''