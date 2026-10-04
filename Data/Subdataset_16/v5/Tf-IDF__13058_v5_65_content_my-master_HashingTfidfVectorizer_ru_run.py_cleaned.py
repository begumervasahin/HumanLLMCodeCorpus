import time
from nltk.corpus import stopwords
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from vectorizer import HashingTfIdfVectorizer
from logger import logger
def fonk1():
    b1 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
    b2 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
    b3 = stopwords.words('russian')
    b4 = SQLiteDataIterator(b1, batch_size=1000)
    b5 = RussianTokenizer(ngram_range=[1, 2], lemmas=True, stopwords=b3)
    b6 = HashingTfIdfVectorizer(b4, tokenizer=b5)
    b7 = time.time()
    try:
        b6.fit()
        b6.save(b2)
    except Exception as e:
        logger.exception(e)
        raise
    b8 = time.time()
    logger.info(f"Process completed in {b8 - b7:.2f} seconds")
if b9 = = "__main__":
    fonk1()