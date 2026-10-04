
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import logging
logging.basicConfig(b1 = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class class1:
    def fonk1(self, corpus):
        logging.info('Initializing the AutoStopwordsGen started')
        self.b2 = CountVectorizer()
        self.b3 = self.b2.fit_transform(corpus)
        self.b4 = TfidfVectorizer()
        self.b5 = self.b4.fit_transform(corpus)
        logging.info('Initializing the AutoStopwordsGen completed')
    def fonk2(self, b6 = 0.95, last_n=0.1):
        logging.info('Generating b10 started')
        b7 = pd.DataFrame({
            'word': self.b4.get_feature_names_out(),
            'frequency': np.asarray(self.b3.sum(b8 = 0)).ravel(),
            'idf': self.b4.idf_
        })
        b7.sort_values(b9 = ['frequency'], ascending=False, inplace=True)
        b7['prob'] = b7['frequency'] / b7['frequency'].sum()
        b7['entropy'] = b7['prob'].apply(lambda x: x * np.log(1 / x) if x > 0 else 0)
        b7['vp'] = np.power(b7['prob'] - b7['prob'].mean(), 2)
        b10 = {'frequency': [], 'idf': [], 'entropy': [], 'vp': []}
        b11 = ['frequency', 'entropy', 'vp']
        for b12 in b11:
            if b12 = = 'frequency':
                b13 = b7[b12].quantile(b6)
                b10[b12] = b7[b7[b12] >= b13]['word'].tolist()
            else:
                b13 = b7[b12].quantile(last_n)
                b10[b12] = b7[b7[b12] <= b13]['word'].tolist()
        for key in b10:
            b10[key] = set(b10[key])
        b14 = set(b7[b7['frequency'] < 2]['word'].tolist())
        b14.update(b10['frequency'].intersection(b10['entropy']).intersection(b10['vp']))
        logging.info('Generating b10 completed')
        return list(b14)