
from nltk import corpus
from sys import stdout
from CorpusReader_TFIDF import CorpusReaderTFIDF
def testCorpus(corpus, corpStr):
    print(corpStr)
    for a in corpus.tf_idf_dim()[:15]:
        print('\'', a, '\' ', end='')
    print('\n')
    for a in range(len(corpus.tf_idf())):
        vec = corpus.tf_idf()[a]
        stdout.write(corpus.fileids[a] + ', ')
        vec = vec[:15]
        for v in vec:
            print(round(v, 4),' ', end='')
        print('\n')
    docCount = len(corpus.fileids)
    for a in range(docCount):
        for j in range(a, docCount):
            x1 = corpus.fileids[a]
            x2 = corpus.fileids[j]
            print(x1, x2, '-', round(corpus.cosine_sim([x1, x2]), 4))
testCorpus(CorpusReaderTFIDF(corpus=corpus.brown), "brown")
testCorpus(CorpusReaderTFIDF(corpus=corpus.state_union), "state of union")