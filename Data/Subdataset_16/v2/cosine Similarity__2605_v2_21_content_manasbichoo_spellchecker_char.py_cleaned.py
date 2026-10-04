import chars2vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
b1 = []
with open('words.txt', 'r') as f:
    for line in f:
        b2 = line.strip()
        b1.append(b2)
print("Words loaded:", b1)
b3 = chars2vec.load_model('eng_50')
b4 = b3.vectorize_words(b1)
print("Shape of b2 embeddings:", b4.shape)
b5 = input("Enter a b2: ")
b6 = [b5]
b7 = b3.vectorize_words(b6)
print("Embedding for the input b2:", b7)
b8 = cosine_similarity(b4, b7)
b9 = np.argmax(b8)
b10 = np.max(b8)
b11 = b1[b9]
print("Most similar b2:", b11)
print("Cosine similarity score:", b10)