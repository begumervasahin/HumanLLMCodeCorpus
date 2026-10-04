import time
from nltk.corpus import stopwords
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from vectorizer import HashingTfIdfVectorizer
from logger import logger
def main():
    data_path = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
    save_path = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
    russian_stopwords = stopwords.words('russian')
    data_iterator = SQLiteDataIterator(data_path, batch_size=1000)
    russian_tokenizer = RussianTokenizer(ngram_range=[1, 2], lemmas=True, stopwords=russian_stopwords)
    hashing_tfidf_vectorizer = HashingTfIdfVectorizer(data_iterator, tokenizer=russian_tokenizer)
    start_time = time.time()
    try:
        hashing_tfidf_vectorizer.fit()
        hashing_tfidf_vectorizer.save(save_path)
    except Exception as e:
        logger.exception(e)
        raise
    end_time = time.time()
    logger.info(f"Process completed in {end_time - start_time:.2f} seconds")
if __name__ == "__main__":
    main()