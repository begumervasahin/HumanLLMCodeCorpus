import time
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from b6 import HashingTfIdfVectorizer
from logger import logger
b1 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
b2 = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
b3 = ['Hello world', 'Shiny day']
class class1(SQLiteDataIterator):
    def fonk1(self, b3):
        self.b3 = b3
        self.a1 = 1000
        self.a2 = 0
    def fonk2(self):
        return self
    def fonk3(self):
        if self.a2 >= len(self.b3):
            raise StopIteration
        b4 = self.b3[self.a2:min(self.a2 + self.a1, len(self.b3))]
        self.a2 += self.a1
        return b4
b5 = class1(b3)
b6 = HashingTfIdfVectorizer(b5,
                                     b7 = StreamSpacyTokenizer(ngram_range=[1, 2],
                                                                    b8 = True,
                                                                    b9 = 'sklearn',
                                                                    b10 = 4))
b11 = time.time()
try:
    b6.fit()
    b6.save(b2)
except Exception as e:
    logger.exception(e)
    raise
b12 = time.time() - b11
print("Execution time:", b12)