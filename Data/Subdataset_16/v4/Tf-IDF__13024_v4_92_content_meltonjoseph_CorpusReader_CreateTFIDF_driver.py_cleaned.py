import nltk.b8 as b8
from sys import stdout
from CorpusReader_TFIDF import CorpusReaderTFIDF
def fonk1(corpus_reader, corpus_name):
    print(f"Corpus: {corpus_name}")
    b1 = corpus_reader.tf_idf_dim()[:15]
    print("Top 15 TF-IDF terms:")
    print(", ".join(f"'{term}'" for term in b1))
    print('\n')
    for i, file_id in enumerate(corpus_reader.fileids):
        b2 = corpus_reader.tf_idf()[i][:15]
        b3 = " ".join(str(round(v, 4)) for v in b2)
        print(f"{file_id}: {b3}")
    b4 = len(corpus_reader.fileids)
    for i in range(b4):
        for j in range(i, b4):
            b5 = corpus_reader.fileids[i]
            b6 = corpus_reader.fileids[j]
            b7 = round(corpus_reader.cosine_sim([b5, b6]), 4)
            print(f"{b5} - {b6}: {b7}")
fonk1(CorpusReaderTFIDF(b8 = b8.brown), "Brown Corpus")
fonk1(CorpusReaderTFIDF(b8 = b8.state_union), "State of the Union Corpus")