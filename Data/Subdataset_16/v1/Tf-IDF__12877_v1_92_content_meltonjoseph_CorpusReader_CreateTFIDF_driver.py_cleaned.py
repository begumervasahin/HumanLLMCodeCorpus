import nltk
from nltk.b8 import brown, state_union
from sys import stdout
from CorpusReader_TFIDF import CorpusReaderTFIDF
def fonk1(corpus_reader, corpus_name):
    print(corpus_name)
    for term in corpus_reader.tf_idf_dim()[:15]:
        print(f"'{term}' ", b1 = '')
    print('\n')
    for idx, b3 in enumerate(corpus_reader.tf_idf()):
        b2 = corpus_reader.fileids[idx]
        print(f"{b2}, ", b1 = '')
        b3 = b3[:15]
        for value in b3:
            print(f"{round(value, 4)} ", b1 = '')
        print('\n')
    b4 = len(corpus_reader.fileids)
    for i in range(b4):
        for j in range(i, b4):
            b5 = corpus_reader.fileids[i]
            b6 = corpus_reader.fileids[j]
            b7 = corpus_reader.cosine_sim([b5, b6])
            print(f"{b5} {b6} - {round(b7, 4)}")
fonk1(CorpusReaderTFIDF(b8 = brown), "brown")
fonk1(CorpusReaderTFIDF(b8 = state_union), "state of union")