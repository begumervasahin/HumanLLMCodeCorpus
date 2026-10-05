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
class TestPredictorBuilderTests(unittest.TestCase):
    def test_create_with_default_settings(self):
        sut = SentimentPredictor().build()
        self.assertIsNotNone(sut)
    def test_create_with_console_reporter(self):
        sut = SentimentPredictor().with_reporter(NullReporter()).build()
        self.assertIsNotNone(sut)
    def test_run_on_default_test_data(self):
        sut = SentimentPredictor().with_reporter(NullReporter()).build()
        corpus = generate_corpus()
        sut.fit()
        results = [sut.predict(x) for x in corpus]
        self.assertIsNotNone(results)
class XformerTests(unittest.TestCase):
    def test_run_data_preprocessing(self):
        imdb_data_preprocess('./')
    def test_run_mixed_data_preprocessing(self):
        imdb_data_preprocess('./', mix=True)
if __name__ == "__main__":
    unittest.main()