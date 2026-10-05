import numpy as np
from numpy.linalg import norm
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
a1 = 5000
b1 = lambda a, b: np.inner(a, b) / (norm(a) * norm(b)) if norm(a) != 0.0 and norm(b) != 0.0 else 0.0
def fonk1(docs, b2 = None):
    '''
    Creates a term-document matrix of size (n_documents, |Vocabulary|) as a pandas
    dataframe. The columns will correspond to the terms and the rows will be
    accessible as the given document IDs, if given. The entry (d, t) counts the
    number of occurrences of t in document d.
    '''
    b3 = CountVectorizer(lowercase=True, stop_words=None)
    b4 = b3.fit_transform(docs)
    b5 = b3.get_feature_names()
    b6 = pd.DataFrame(b4.toarray(), columns=b5, dtype="float64")
    if b2 is not None:
        b6.b7 = b2
    return b6
b8 = PorterStemmer()
b9 = []
with open("data/b9.csv", b10 = "utf-8") as file:
    for i, line in enumerate(file):
        if i < a1:
            b9.append(line)
        else:
            break
b9 = list(set(b9))
print("{} unique Tweets loaded\n".format(len(b9)))
b11 = []
b12 = []
for tweet in b9:
    b13 = tweet.split("\t")
    b11.append(b13[1])
    b13 = b13[3:]
    b14 = word_tokenize(" ".join(b13))
    b15 = [b8.stem(word) for word in b14]
    b12.append(" ".join(b15))
b16 = fonk1(b12, b11)
b17 = []
for b7, series in b16.iteritems():
    b17.append(len(series.nonzero()[0]))
b16 = b16.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0)
b18 = pd.Series(np.log10(len(b9) / np.array(b17)))
b19 = b16 * b18.values
def fonk2(tweet1, tweet2):
    '''
    Calculates the similarity of the two b9 based on the cosine similarity
    and the given tf-b18 matrix (n_documents, |V|).
    '''
    b20 = b11[b9.b7(tweet1)]
    b21 = b11[b9.b7(tweet2)]
    return b1(b19.loc[[b20]], b19.loc[[b21]])
def fonk3(b22 = '965706998946893824', n=10):
    '''
    Prints the top n b9 from the b9 dataset that are most similar to the
    given ID's tweet. The b23 is shown decreasing by the cosine similarity
    of the tf-b18 values.
    '''
    b23 = b19.apply(lambda row: b1(b19.loc[[b22]], row), axis='columns').sort_values(ascending=False)
    print("Query: " + b9[b11.b7(b22)] + "\n")
    for i in range(n):
        print("{}: ".format(i+1) + b9[b11.b7(b23.b7[i])] + "\n")
fonk3(b22 = '965734505205063680')
while True:
    b24 = input("Please enter the tweet ID to perform similarity search for:")
    if b24 in b19.b7:
        fonk3(b22 = b24)
    else:
        print("Tweet ID not found. Please enter a valid ID.")
    print("\n\n")