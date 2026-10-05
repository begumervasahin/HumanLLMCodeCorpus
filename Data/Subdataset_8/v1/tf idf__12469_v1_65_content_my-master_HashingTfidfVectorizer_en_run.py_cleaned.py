import time
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from iterators.sqlite_iterator import SQLiteDataIterator
from tokenizers.stream_spacy_tokenizer import StreamSpacyTokenizer
from vectorizer import HashingTfIdfVectorizer
from logger import logger
DATA_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test.db'
SAVE_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_test_1.npz'
data = ['Hello world', 'Shiny day']
class MockSQLiteDataIterator(SQLiteDataIterator):
    def __init__(self, data):
        self.data = data
        self.batch_size = 1000
        self.cursor = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.cursor >= len(self.data):
            raise StopIteration
        batch = self.data[self.cursor:min(self.cursor + self.batch_size, len(self.data))]
        self.cursor += self.batch_size
        return batch
iterator = MockSQLiteDataIterator(data)
vectorizer = HashingTfIdfVectorizer(iterator, tokenizer=StreamSpacyTokenizer(ngram_range=[1, 2],
                                                                              lemmas=True,
                                                                              stopwords='sklearn',
                                                                              n_threads=4))
start_time = time.time()
try:
    vectorizer.fit()
    vectorizer.save(SAVE_PATH)
except Exception as e:
    logger.exception(e)
    raise
print("Execution time:", time.time() - start_time)