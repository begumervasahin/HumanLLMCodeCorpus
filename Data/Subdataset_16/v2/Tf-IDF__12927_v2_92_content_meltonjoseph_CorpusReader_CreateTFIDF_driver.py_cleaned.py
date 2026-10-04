import nltk
from nltk.b8 import brown, state_union
from CorpusReader_TFIDF import CorpusReaderTFIDF
def fonk1(corpus_reader, b1 = 15):
    for term in corpus_reader.tf_idf_dim()[:b1]:
        print(f"'{term}' ", b2 = '')
    print('\n')
def fonk2(corpus_reader, b1 = 15):
    for idx, vec in enumerate(corpus_reader.tf_idf()):
        b3 = corpus_reader.fileids[idx]
        print(f"{b3}, ", b2 = '')
        for value in vec[:b1]:
            print(f"{round(value, 4)} ", b2 = '')
        print('\n')
def fonk3(corpus_reader):
    b4 = len(corpus_reader.fileids)
    for i in range(b4):
        for j in range(i, b4):
            b5 = corpus_reader.fileids[i]
            b6 = corpus_reader.fileids[j]
            b7 = corpus_reader.cosine_sim([b5, b6])
            print(f"{b5} {b6} - {round(b7, 4)}")
def fonk4(corpus_reader, corpus_name):
    print(corpus_name)
    fonk1(corpus_reader)
    fonk2(corpus_reader)
    fonk3(corpus_reader)
fonk4(CorpusReaderTFIDF(b8 = brown), "Brown Corpus")
fonk4(CorpusReaderTFIDF(b8 = state_union), "State of the Union Corpus")