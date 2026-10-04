import nltk.b9 as b9
from CorpusReader_TFIDF import CorpusReaderTFIDF
def fonk1(corpus_reader, b1 = 15):
    b2 = corpus_reader.tf_idf_dim()[:b1]
    print("Top TF-IDF terms:")
    print(", ".join(f"'{term}'" for term in b2))
    print('\n')
def fonk2(corpus_reader, b1 = 15):
    for i, file_id in enumerate(corpus_reader.fileids):
        b3 = corpus_reader.tf_idf()[i][:b1]
        b4 = " ".join(str(round(v, 4)) for v in b3)
        print(f"{file_id}: {b4}")
def fonk3(corpus_reader):
    b5 = len(corpus_reader.fileids)
    for i in range(b5):
        for j in range(i, b5):
            b6 = corpus_reader.fileids[i]
            b7 = corpus_reader.fileids[j]
            b8 = round(corpus_reader.cosine_sim([b6, b7]), 4)
            print(f"{b6} - {b7}: {b8}")
def fonk4(corpus_reader, corpus_name):
    print(f"Corpus: {corpus_name}\n")
    fonk1(corpus_reader)
    fonk2(corpus_reader)
    fonk3(corpus_reader)
fonk4(CorpusReaderTFIDF(b9 = b9.brown), "Brown Corpus")
fonk4(CorpusReaderTFIDF(b9 = b9.state_union), "State of the Union Corpus")