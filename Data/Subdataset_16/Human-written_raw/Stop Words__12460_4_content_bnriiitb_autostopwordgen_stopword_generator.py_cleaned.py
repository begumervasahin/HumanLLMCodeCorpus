
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import logging
logging.basicConfig(b1 = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class class1:
    def fonk1(self, corpus):
        logging.info('initializing the AutoStopwordsGen started')
        b2 = CountVectorizer()
        b3 = b2.fit_transform(corpus)
        b4 = TfidfVectorizer()
        b5 = b4.fit_transform(corpus)
        self.b4 = b4
        self.b3 = b3
        logging.info('initializing the AutoStopwordsGen completed')
    def fonk2(self, b6 = .95, last_n=.1):
        logging.info('generating b10 started')
        b7 = pd.DataFrame({'word': self.b4.get_feature_names(),
                                     'frequency':np.asarray(self.b3.sum(b8 = 0)).ravel().tolist(),
                                     'idf':self.b4.idf_})
        b7.sort_values(b9 = ['frequency'],ascending = False,inplace=True)
        b7['prob']=b7.frequency/b7.shape[0]
        b7['entropy']=b7.prob.apply(lambda x: x*np.log(1/x))
        b7['vp']=np.power(b7.prob-b7.prob.mean(),2)/b7.shape[0]
        b10 = dict({'frequency':[],'idf':[],'entropy':[],'vp':[]})
        b11 = ['frequency','entropy','vp']
        for b12 in b11:
            if(b12 = ='frequency'):
                b13 = b7[b12].quantile([last_n,b6]).tolist()[1]
                b10[b12]=b7[b7[b12]>=b13].word.tolist()
            else:
                b14 = b7[b12].quantile([last_n,b6]).tolist()[0]
                b10[b12]=b7[b7[b12]<=b14].word.tolist()
        for key in b10.keys():
            b10[key]=set(b10[key])
        b15 = b7[b7.frequency<2].word.tolist()
        b15.extend(list(b10['frequency'].intersection(b10['entropy']).intersection(b10['vp'])))
        b15 = list(set(b15))
        logging.info('
        logging.info('generating b10 completed')
        return b15