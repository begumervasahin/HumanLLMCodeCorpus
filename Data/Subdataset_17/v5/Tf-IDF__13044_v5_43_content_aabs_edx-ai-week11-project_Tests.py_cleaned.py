import unittest
from SentimentPredictor import SentimentPredictor
from driver_3 import imdb_data_preprocess
class Reporter:
    def write(self, msg):
        pass
class NullReporter(Reporter):
    def write(self, msg):
        print()
def generate_corpus():
    return []
class TestSentimentPredictor(unittest.TestCase):
    def test_can_create_from_default(self):
        predictor = SentimentPredictor().build()
        self.assertIsNotNone(predictor)
    def test_can_inject_console_reporter(self):
        predictor = SentimentPredictor().with_reporter(NullReporter()).build()
        self.assertIsNotNone(predictor)
    def test_can_run_on_default_test_data(self):
        predictor = SentimentPredictor().with_reporter(NullReporter()).build()
        corpus = generate_corpus()
        predictor.fit()
        results = [predictor.predict(text) for text in corpus]
        self.assertIsNotNone(results)
class TestImdbDataPreprocess(unittest.TestCase):
    def test_run(self):
        imdb_data_preprocess('./')
    def test_run_mixed(self):
        imdb_data_preprocess('./', mix=True)
if __name__ == '__main__':
    unittest.main()