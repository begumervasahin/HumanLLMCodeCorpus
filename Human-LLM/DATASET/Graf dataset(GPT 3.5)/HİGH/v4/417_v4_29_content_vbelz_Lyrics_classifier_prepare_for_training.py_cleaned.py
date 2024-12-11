import spacy as spacy_en
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
b1 = spacy_en.load('en_core_web_md')
def fonk1(song):
    b2 = b1(song)
    b3 = ''
    for b5 in b2:
        if (b5.b4 = = False)  and (b5.pos_ != 'PUNCT') and  (b5.pos_ != 'NUM'):
            b5 = b5.lemma_
            b3 += b5 + ' '
    return b3
def fonk2(b6):
    b6 = b6.loc[b6['Main Language'] == 'en', :]
    b6.drop(['English Translation Lyrics'], b7 = 1, inplace=True)
    return b6
def fonk3(b6):
    b6['Text Lyrics'] = b6['Text Lyrics'].apply(clean_my_text)
    return b6
def fonk4(b11, b13, folder_save):
    b8 = os.path.join(folder_save, 'countvector.sav')
    pickle.dump(b11, open(b8, 'wb'))
    b9 = os.path.join(folder_save, 'b9.sav')
    pickle.dump(b13, open(b9, 'wb'))
    return
def fonk5(df_read, folder_save):
    b10 = fonk2(df_read)
    b10 = fonk3(b10)
    b11 = CountVectorizer()
    b12 = b11.fit_transform(b10['Text Lyrics'])
    b13 = TfidfTransformer()
    b14 = b13.fit_transform(b12)
    fonk4(b11, b13, folder_save)
    b15 = pd.DataFrame(b14.todense(), columns=b11.get_feature_names())
    b16 = b10['Name']
    b17 = b15
    return b17, b16