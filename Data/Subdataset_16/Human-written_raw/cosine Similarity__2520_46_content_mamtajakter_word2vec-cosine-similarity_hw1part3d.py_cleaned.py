import gensim
from gensim.models.word2vec import Word2Vec
b1 = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary = True);
from nltk.corpus import brown
b2 = "rebellion"
b3 = "slave"
b4 = b1.most_similar(positive=[b2], topn = 10)
b5 = b1.most_similar(positive=[b3], topn = 10)
b6 = []
for p in b4:
    b6.append(p[0])
b7 = []
for p in b5:
    b7.append(p[0])
b8 = ""
for p in b6:
    b9 = b1.similarity(b2,p)
    b8 = b8+"\n"+ b2 + " - "+ p+ ": "+ str(b9)
b10 = ""
for p in b7:
    b9 = b1.similarity(b3,p)
    b10 = b10+"\n"+ b3 + " - "+ p+ ": "+ str(b9)
print("Top ten Similar words: \n")
print(b2 + " = " + str(b6))
print(b3 + " = " + str(b7))
print("Cosine Similarities: \n")
print(b8)
print(b10)