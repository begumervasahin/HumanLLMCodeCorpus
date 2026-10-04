import nltk
from nltk.b11 import brown, state_union
from CorpusReader_TFIDF import CorpusReaderTFIDF
def fonk1(corpus_reader, b1 = 15):
    b2 = corpus_reader.tf_idf_dim()[:b1]
    b3 = ' '.join([f"'{term}'" for term in b2])
    print(b3)
    print()
def fonk2(corpus_reader, b1 = 15):
    for idx, vec in enumerate(corpus_reader.tf_idf()):
        b4 = corpus_reader.fileids[idx]
        b5 = ' '.join([f"{round(value, 4)}" for value in vec[:b1]])
        print(f"{b4}, {b5}")
    print()
def fonk3(corpus_reader):
    b6 = len(corpus_reader.fileids)
    for i in range(b6):
        for j in range(i, b6):
            b7 = corpus_reader.fileids[i]
            b8 = corpus_reader.fileids[j]
            b9 = corpus_reader.cosine_sim([b7, b8])
            print(f"{b7} {b8} - {round(b9, 4)}")
def fonk4(corpus_reader, corpus_name):
    print(f"Testing {corpus_name}\n")
    fonk1(corpus_reader)
    fonk2(corpus_reader)
    fonk3(corpus_reader)
if b10 = = "__main__":
    fonk4(CorpusReaderTFIDF(b11 = brown), "Brown Corpus")
    fonk4(CorpusReaderTFIDF(b11 = state_union), "State of the Union Corpus")