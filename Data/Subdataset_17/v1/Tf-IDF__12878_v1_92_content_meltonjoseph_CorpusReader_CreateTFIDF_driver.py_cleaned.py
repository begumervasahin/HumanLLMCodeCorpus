import nltk
from nltk.corpus import brown, state_union
from sys import stdout
from CorpusReader_TFIDF import CorpusReaderTFIDF
def test_corpus(corpus_reader, corpus_name):
    print(corpus_name)
    for term in corpus_reader.tf_idf_dim()[:15]:
        print(f"'{term}' ", end='')
    print('\n')
    for idx, vec in enumerate(corpus_reader.tf_idf()):
        file_id = corpus_reader.fileids[idx]
        print(f"{file_id}, ", end='')
        vec = vec[:15]
        for value in vec:
            print(f"{round(value, 4)} ", end='')
        print('\n')
    doc_count = len(corpus_reader.fileids)
    for i in range(doc_count):
        for j in range(i, doc_count):
            file_id1 = corpus_reader.fileids[i]
            file_id2 = corpus_reader.fileids[j]
            cosine_similarity = corpus_reader.cosine_sim([file_id1, file_id2])
            print(f"{file_id1} {file_id2} - {round(cosine_similarity, 4)}")
test_corpus(CorpusReaderTFIDF(corpus=brown), "brown")
test_corpus(CorpusReaderTFIDF(corpus=state_union), "state of union")