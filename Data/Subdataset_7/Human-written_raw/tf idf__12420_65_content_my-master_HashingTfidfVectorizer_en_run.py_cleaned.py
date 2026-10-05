import time
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from b5 import HashingTfIdfVectorizer
from logger import logger
b1 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
b2 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
b3 = ['Hello world', 'Shiny day']
b4 = SQLiteDataIterator(b1, batch_size=1000)
b5 = HashingTfIdfVectorizer(b4, tokenizer=StreamSpacyTokenizer(ngram_range=[1, 2],
                                                                             b6 = True,
                                                                             b7 = 'sklearn',
                                                                             b8 = 4))
b9 = time.time()
try:
    b5.fit()
    b5.save(b2)
except Exception as e:
    logger.exception(e)
    raise