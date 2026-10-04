import time
import logging
from nltk.corpus import stopwords
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from vectorizer import HashingTfIdfVectorizer
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
DATA_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
SAVE_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
BATCH_SIZE = 1000
russian_stopwords = stopwords.words('russian')
data_iterator = SQLiteDataIterator(DATA_PATH, batch_size=BATCH_SIZE)
tokenizer = RussianTokenizer(ngram_range=[1, 2], lemmas=True, stopwords=russian_stopwords)
vectorizer = HashingTfIdfVectorizer(data_iterator, tokenizer=tokenizer)
start_time = time.time()
try:
    vectorizer.fit()
    vectorizer.save(SAVE_PATH)
    elapsed_time = time.time() - start_time
    logger.info(f"Vectorizer fitted and saved successfully. Time taken: {elapsed_time:.2f} seconds")
except Exception as e:
    logger.exception("An error occurred during vectorization")
    raise