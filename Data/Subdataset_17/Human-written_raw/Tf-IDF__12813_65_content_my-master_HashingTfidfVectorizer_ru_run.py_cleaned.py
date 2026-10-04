import time
from nltk.corpus import stopwords
STOPWORDS = stopwords.words('russian')
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from vectorizer import HashingTfIdfVectorizer
from logger import logger
DATA_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
SAVE_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
iterator = SQLiteDataIterator(DATA_PATH, batch_size=1000)
vectorizer = HashingTfIdfVectorizer(iterator, tokenizer=RussianTokenizer(ngram_range=[1, 2],
                                                                         lemmas=True,
                                                                         stopwords=STOPWORDS))
start_time = time.time()
try:
    vectorizer.fit()
    vectorizer.save(SAVE_PATH)
except Exception as e:
    logger.exception(e)
    raise