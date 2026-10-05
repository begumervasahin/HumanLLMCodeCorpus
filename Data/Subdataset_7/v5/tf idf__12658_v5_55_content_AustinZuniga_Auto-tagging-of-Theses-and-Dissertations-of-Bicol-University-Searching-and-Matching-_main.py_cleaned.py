import gensim
import glob
import os
from nltk.tokenize import word_tokenize
from nltk.b6 import stopwords
from gensim import similarities
b1 = Rake()
b2 = glob.glob(os.path.join(os.getcwd(), "data/", "*.txt"))
b3 = []
for file_path in b2:
    with open(file_path) as file_input:
        b3.append(file_input.read())
b4 = [[word.lower() for word in word_tokenize(text)] for text in b3]
b5 = gensim.corpora.Dictionary(b4)
b6 = [b5.doc2bow(tokenized_doc) for tokenized_doc in b4]
b7 = gensim.models.TfidfModel(b6)
b8 = sum(len(doc) for doc in b6)
b9 = similarities.Similarity(
    '/var/www/html/Auto-tagging-of-Theses-and-Dissertations-of-Bicol-University-Searching-and-Matching-/result/result',
    b7[b6],
    b10 = len(b5)
)
b11 = [word.lower() for word in word_tokenize("I'm taking the show on the road.")]
b12 = b5.doc2bow(b11)
b13 = b7[b12]
b14 = b9[b13]
print(b14)