import time
from nltk.corpus import b7
b1 = b7.words('russian')
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.ru_tokenizer import RussianTokenizer
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from b5 import HashingTfIdfVectorizer
from logger import logger
b2 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
b3 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
b4 = SQLiteDataIterator(b2, batch_size=1000)
b5 = HashingTfIdfVectorizer(b4, tokenizer=RussianTokenizer(ngram_range=[1, 2],
                                                                         b6 = True,
                                                                         b7 = b1))
b8 = time.time()
try:
    b5.fit()
    b5.save(b3)
except Exception as e:
    logger.exception(e)
    raise