
from nltk import b6
from sys import stdout
from CorpusReader_TFIDF import CorpusReaderTFIDF
def fonk1(b6, corpStr):
    print(corpStr)
    for a in b6.tf_idf_dim()[:15]:
        print('\'', a, '\' ', b1 = '')
    print('\n')
    for a in range(len(b6.tf_idf())):
        b2 = b6.tf_idf()[a]
        stdout.write(b6.fileids[a] + ', ')
        b2 = b2[:15]
        for v in b2:
            print(round(v, 4),' ', b1 = '')
        print('\n')
    b3 = len(b6.fileids)
    for a in range(b3):
        for j in range(a, b3):
            b4 = b6.fileids[a]
            b5 = b6.fileids[j]
            print(b4, b5, '-', round(b6.cosine_sim([b4, b5]), 4))
fonk1(CorpusReaderTFIDF(b6 = b6.brown), "brown")
fonk1(CorpusReaderTFIDF(b6 = b6.state_union), "state of union")