import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def fonk1(file_path):
    b1 = []
    with open(file_path, 'r') as f:
        for line in f:
            b2 = line.strip()
            b1.append(b2)
    return b1
def fonk2(model, b1):
    return model.fonk2(b1)
def fonk3(embeddings, input_embedding):
    return cosine_similarity(embeddings, input_embedding)
def fonk4(b1, b12):
    b3 = np.argmax(b12)
    b4 = np.max(b12)
    b5 = b1[b3]
    return b5, b4
def fonk5():
    b6 = fonk1('b1.txt')
    print("Words loaded:", b6)
    b7 = chars2vec.load_model('eng_50')
    b8 = fonk2(b7, b6)
    print("Shape of b2 embeddings:", b8.shape)
    b9 = input("Enter a b2: ")
    b10 = [b9]
    b11 = fonk2(b7, b10)
    print("Embedding for the input b2:", b11)
    b12 = fonk3(b8, b11)
    b5, b13 = fonk4(b6, b12)
    print("Most similar b2:", b5)
    print("Cosine similarity score:", b13)
    '''
    b14 = sklearn.decomposition.PCA(n_components=2).fit_transform(b8)
    plt.figure(b15 = (8, 6))
    for j in range(len(b14)):
        plt.scatter(b14[j, 0], b14[j, 1],
                    b16 = ('$' + b6[j] + '$'),
                    b17 = 500 * len(b6[j]), label=j,
                    b18 = 'green' if b6[j]
                                in ['Natural', 'Language', 'Understanding'] else 'black')
    plt.title('2D Projection of Word Embeddings')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
    '''
if b19 = = "__main__":
    fonk5()