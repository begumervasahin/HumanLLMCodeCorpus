import nltk
from nltk.corpus import brown, state_union
from CorpusReader_TFIDF import CorpusReaderTFIDF
def display_tf_idf_dimensions(corpus_reader, top_n=15):
    top_terms = corpus_reader.tf_idf_dim()[:top_n]
    formatted_terms = ' '.join([f"'{term}'" for term in top_terms])
    print(formatted_terms)
    print()
def display_tf_idf_vectors(corpus_reader, top_n=15):
    for idx, vec in enumerate(corpus_reader.tf_idf()):
        file_id = corpus_reader.fileids[idx]
        formatted_vec = ' '.join([f"{round(value, 4)}" for value in vec[:top_n]])
        print(f"{file_id}, {formatted_vec}")
    print()
def display_cosine_similarities(corpus_reader):
    doc_count = len(corpus_reader.fileids)
    for i in range(doc_count):
        for j in range(i, doc_count):
            file_id1 = corpus_reader.fileids[i]
            file_id2 = corpus_reader.fileids[j]
            cosine_similarity = corpus_reader.cosine_sim([file_id1, file_id2])
            print(f"{file_id1} {file_id2} - {round(cosine_similarity, 4)}")
def test_corpus(corpus_reader, corpus_name):
    print(f"Testing {corpus_name}\n")
    display_tf_idf_dimensions(corpus_reader)
    display_tf_idf_vectors(corpus_reader)
    display_cosine_similarities(corpus_reader)
if __name__ == "__main__":
    test_corpus(CorpusReaderTFIDF(corpus=brown), "Brown Corpus")
    test_corpus(CorpusReaderTFIDF(corpus=state_union), "State of the Union Corpus")