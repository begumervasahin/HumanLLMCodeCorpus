import nltk.corpus as corpus
from sys import stdout
from CorpusReader_TFIDF import CorpusReaderTFIDF
def test_corpus(corpus_reader, corpus_name):
    print(f"Corpus: {corpus_name}")
    top_terms = corpus_reader.tf_idf_dim()[:15]
    print("Top 15 TF-IDF terms:")
    print(", ".join(f"'{term}'" for term in top_terms))
    print('\n')
    for i, file_id in enumerate(corpus_reader.fileids):
        vec = corpus_reader.tf_idf()[i][:15]
        vec_str = " ".join(str(round(v, 4)) for v in vec)
        print(f"{file_id}: {vec_str}")
    doc_count = len(corpus_reader.fileids)
    for i in range(doc_count):
        for j in range(i, doc_count):
            file_id1 = corpus_reader.fileids[i]
            file_id2 = corpus_reader.fileids[j]
            similarity = round(corpus_reader.cosine_sim([file_id1, file_id2]), 4)
            print(f"{file_id1} - {file_id2}: {similarity}")
test_corpus(CorpusReaderTFIDF(corpus=corpus.brown), "Brown Corpus")
test_corpus(CorpusReaderTFIDF(corpus=corpus.state_union), "State of the Union Corpus")