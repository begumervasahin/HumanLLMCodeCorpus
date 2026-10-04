import chars2vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
b1 = []
with open('words.txt', 'r') as f:
    for word in f.read().split():
        b1.append(str(word))
print("Words loaded:", b1)
b2 = chars2vec.load_model('eng_50')
b3 = b2.vectorize_words(b1)
print("Word embeddings shape:", b3.shape)
b4 = str(input("Enter a word: "))
b5 = [b4]
b6 = b2.vectorize_words(b5)
print("Embedding for input word:", b6)
b7 = cosine_similarity(b3, b6)
b8 = np.argmax(b7)
b9 = np.max(b7)
b10 = b1[b8]
print("Most similar word:", b10)
print("Cosine similarity score:", b9)