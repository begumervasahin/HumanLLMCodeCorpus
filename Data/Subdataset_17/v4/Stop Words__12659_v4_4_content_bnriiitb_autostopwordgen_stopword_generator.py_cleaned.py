
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class AutoStopWordsGen:
    def __init__(self, corpus):
        logging.info('Initializing the AutoStopwordsGen started')
        self.cv = CountVectorizer()
        self.cvft = self.cv.fit_transform(corpus)
        self.tfidfcv = TfidfVectorizer()
        self.tfidfcvft = self.tfidfcv.fit_transform(corpus)
        logging.info('Initializing the AutoStopwordsGen completed')
    def get_stopwords(self, top_n=0.95, last_n=0.1):
        logging.info('Generating stopwords started')
        word_freq_df = pd.DataFrame({
            'word': self.tfidfcv.get_feature_names_out(),
            'frequency': np.asarray(self.cvft.sum(axis=0)).ravel(),
            'idf': self.tfidfcv.idf_
        })
        word_freq_df.sort_values(by=['frequency'], ascending=False, inplace=True)
        word_freq_df['prob'] = word_freq_df['frequency'] / word_freq_df['frequency'].sum()
        word_freq_df['entropy'] = word_freq_df['prob'].apply(lambda x: x * np.log(1 / x) if x > 0 else 0)
        word_freq_df['vp'] = np.power(word_freq_df['prob'] - word_freq_df['prob'].mean(), 2)
        stopwords = {'frequency': [], 'idf': [], 'entropy': [], 'vp': []}
        cols = ['frequency', 'entropy', 'vp']
        for col in cols:
            if col == 'frequency':
                threshold = word_freq_df[col].quantile(top_n)
                stopwords[col] = word_freq_df[word_freq_df[col] >= threshold]['word'].tolist()
            else:
                threshold = word_freq_df[col].quantile(last_n)
                stopwords[col] = word_freq_df[word_freq_df[col] <= threshold]['word'].tolist()
        for key in stopwords:
            stopwords[key] = set(stopwords[key])
        very_high_aggregation = set(word_freq_df[word_freq_df['frequency'] < 2]['word'].tolist())
        very_high_aggregation.update(stopwords['frequency'].intersection(stopwords['entropy']).intersection(stopwords['vp']))
        logging.info('Generating stopwords completed')
        return list(very_high_aggregation)