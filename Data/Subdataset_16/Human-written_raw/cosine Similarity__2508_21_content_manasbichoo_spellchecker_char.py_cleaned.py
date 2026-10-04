import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
b1 = []
b2 = open('words.txt')
for b5 in b2.read().split():
    b1.append(str(b5))
print(b1)
b3 = chars2vec.load_model('eng_50')
b4 = b3.vectorize_words(b1)
print(b4)
b5 = str(input("enter a b5"))
b6 = []
b6.append(b5)
b7 = b3.vectorize_words(b6)
print(b7)
b8 = cosine_similarity(b4, b7)
print(max(b8))
b9 = b8.tolist().index(max(b8))
print(b9)
print("The result is")
print(b1[b9])
'''
b10 = sklearn.decomposition.PCA(n_components=2).fit_transform(b4)
b2 = plt.figure(figsize=(8, 6))
for j in range(len(b10)):
    plt.scatter(b10[j, 0], b10[j, 1],
                b11 = ('$' + words[j] + '$'),
                b12 = 500 * len(words[j]), label=j,
                b13 = 'green' if words[j]
                            in ['Natural', 'Language', 'Understanding'] else 'black')
plt.show()'''