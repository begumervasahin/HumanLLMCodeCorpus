
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class AutoStopWordsGen:
    def __init__(self, corpus):
        logging.info('Initializing AutoStopWordsGen started')
        self.cv = CountVectorizer()
        self.cvft = self.cv.fit_transform(corpus)
        self.tfidfcv = TfidfVectorizer()
        self.tfidfcvft = self.tfidfcv.fit_transform(corpus)
        logging.info('Initializing AutoStopWordsGen completed')
    def get_stopwords(self, top_n=0.95, last_n=0.1):
        logging.info('Generating stopwords started')
        word_freq_df = pd.DataFrame({
            'word': self.tfidfcv.get_feature_names_out(),
            'frequency': np.asarray(self.cvft.sum(axis=0)).ravel(),
            'idf': self.tfidfcv.idf_
        })
        word_freq_df.sort_values(by='frequency', ascending=False, inplace=True)
        word_freq_df['prob'] = word_freq_df['frequency'] / word_freq_df['frequency'].sum()
        word_freq_df['entropy'] = word_freq_df['prob'].apply(lambda x: x * np.log(1 / x))
        word_freq_df['vp'] = np.power(word_freq_df['prob'] - word_freq_df['prob'].mean(), 2) / word_freq_df.shape[0]
        stopwords = {'frequency': [], 'idf': [], 'entropy': [], 'vp': []}
        criteria = ['frequency', 'entropy', 'vp']
        for criterion in criteria:
            if criterion == 'frequency':
                top_threshold = word_freq_df[criterion].quantile(top_n)
                stopwords[criterion] = word_freq_df[word_freq_df[criterion] >= top_threshold].word.tolist()
            else:
                last_threshold = word_freq_df[criterion].quantile(last_n)
                stopwords[criterion] = word_freq_df[word_freq_df[criterion] <= last_threshold].word.tolist()
        for key in stopwords.keys():
            stopwords[key] = set(stopwords[key])
        very_high_aggregation = word_freq_df[word_freq_df['frequency'] < 2].word.tolist()
        very_high_aggregation.extend(
            list(stopwords['frequency'].intersection(stopwords['entropy']).intersection(stopwords['vp']))
        )
        very_high_aggregation = list(set(very_high_aggregation))
        logging.info('Generating stopwords completed')
        return very_high_aggregation
if __name__ == "__main__":
    corpus = [
        "This is a sample document.",
        "This document is another example.",
        "And this is yet another sample document."
    ]
    aswg = AutoStopWordsGen(corpus)
    stopwords = aswg.get_stopwords()
    print("Generated stopwords:", stopwords)