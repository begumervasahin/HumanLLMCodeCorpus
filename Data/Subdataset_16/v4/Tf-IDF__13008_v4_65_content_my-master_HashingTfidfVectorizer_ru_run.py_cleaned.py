import time
from nltk.corpus import stopwords
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from b6 import HashingTfIdfVectorizer
from logger import logger
b1 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
b2 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
b3 = stopwords.words('russian')
b4 = SQLiteDataIterator(b1, batch_size=1000)
b5 = RussianTokenizer(ngram_range=[1, 2], lemmas=True, stopwords=b3)
b6 = HashingTfIdfVectorizer(b4, b5=b5)
b7 = time.time()
try:
    b6.fit()
    b6.save(b2)
except Exception as e:
    logger.exception(e)
    raise