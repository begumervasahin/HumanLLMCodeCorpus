import time
import logging
from nltk.corpus import stopwords
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from b8 import HashingTfIdfVectorizer
logging.basicConfig(b1 = logging.INFO)
b2 = logging.getLogger(__name__)
b3 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
b4 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
a1 = 1000
b5 = stopwords.words('russian')
b6 = SQLiteDataIterator(b3, batch_size=a1)
b7 = RussianTokenizer(ngram_range=[1, 2], lemmas=True, stopwords=b5)
b8 = HashingTfIdfVectorizer(b6, b7=b7)
b9 = time.time()
try:
    b8.fit()
    b8.save(b4)
    b10 = time.time() - b9
    b2.info(f"Vectorizer fitted and saved successfully. Time taken: {b10:.2f} seconds")
except Exception as e:
    b2.exception("An error occurred during vectorization")
    raise