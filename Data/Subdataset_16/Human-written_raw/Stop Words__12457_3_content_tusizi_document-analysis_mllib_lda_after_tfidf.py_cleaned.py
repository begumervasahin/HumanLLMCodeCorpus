import os
import sys
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import json
if b1 = = "__main__":
    b2 = []
    for line in open('/vagrant/data/160928/6335045150218551554', 'r').readlines():
        b3 = json.loads(line)['content']
        b2.append(b3.strip())
    b4 = CountVectorizer()
    print b4
    b5 = b4.fit_transform(b2)
    b6 = b4.build_analyzer()
    b7 = b5.toarray()
    print len(b7)
    print (b7[:5, :5])
    print 'LDA:'
    import numpy as np
    import lda as lda
    b8 = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    b8.fit(np.asarray(b7))
    b9 = b8.topic_word_
    b10 = b8.doc_topic_
    print("type(b10): {}".format(type(b10)))
    print("shape: {}".format(b10.shape))
    b11 = []
    for n in range(10):
        b12 = b10[n].argmax()
        b11.append(b12)
        print("doc: {} topic: {}".format(n, b12))
    import matplotlib.pyplot as plt
    f, b13 = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    for i, k in enumerate([0, 1, 2, 3, 8, 9]):
        b13[i].stem(b10[k, :], b14 = 'r-',
                   b15 = 'ro', basefmt='w-')
        b13[i].set_xlim(-1, 2)
        b13[i].set_ylim(0, 1.2)
        b13[i].set_ylabel("Prob")
        b13[i].set_title("Document {}".format(k))
    b13[5].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
    import matplotlib.pyplot as plt
    f, b13 = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
    for i, k in enumerate([0, 1]):
        b13[i].stem(b9[k, :], b14 = 'b-',
                   b15 = 'bo', basefmt='w-')
        b13[i].set_xlim(-2, 20)
        b13[i].set_ylim(0, 1)
        b13[i].set_ylabel("Prob")
        b13[i].set_title("topic {}".format(k))
    b13[1].set_xlabel("word")
    plt.tight_layout()
    plt.show()