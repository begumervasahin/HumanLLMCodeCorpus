import pickle
import cPickle
import numpy
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def fonk1(b1 = "../tools/b5.pkl", authors_file="../tools/email_authors.pkl"):
    b2 = open(authors_file, "r")
    b3 = pickle.load(b2)
    b2.close()
    b4 = open(b1, "r")
    b5 = cPickle.load(b4)
    b4.close()
    features_train, features_test, labels_train, b6 = train_test_split(b5, b3,
                                                                                                 b7 = 0.1,
                                                                                                 b8 = 42)
    b9 = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 b10 = 'english')
    b11 = b9.fit_transform(features_train)
    b12 = b9.transform(features_test)
    b13 = SelectPercentile(f_classif, percentile=10)
    b13.fit(b11, labels_train)
    b11 = b13.transform(b11).toarray()
    b12 = b13.transform(b12).toarray()
    print "no. of Chris training emails:", sum(labels_train)
    print "no. of Sara training emails:", len(labels_train) - sum(labels_train)
    return b11, b12, labels_train, b6