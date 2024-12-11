import spacy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
b1 = spacy.load('en_core_web_md')
def fonk1(song):
    b2 = b1(song)
    b3 = ''
    for b4 in b2:
        if (not b4.is_stop) and (b4.pos_ != 'PUNCT') and (b4.pos_ != 'NUM'):
            b4 = b4.lemma_
            b3 += b4 + ' '
    return b3.strip()
def fonk2(b5):
    b5 = b5[b5['Main Language'] == 'en']
    b5.drop(['English Translation Lyrics'], b6 = 1, inplace=True)
    return b5
def fonk3(b5):
    b5['Text Lyrics'] = b5['Text Lyrics'].apply(clean_my_text)
    return b5
def fonk4(b10, b12, folder_save):
    b7 = os.path.join(folder_save, 'countvector.sav')
    pickle.dump(b10, open(b7, 'wb'))
    b8 = os.path.join(folder_save, 'b8.sav')
    pickle.dump(b12, open(b8, 'wb'))
def fonk5(df_read, folder_save):
    b9 = fonk2(df_read)
    b9 = fonk3(b9)
    b10 = CountVectorizer()
    b11 = b10.fit_transform(b9['Text Lyrics'])
    b12 = TfidfTransformer()
    b13 = b12.fit_transform(b11)
    fonk4(b10, b12, folder_save)
    b14 = pd.DataFrame(b13.toarray(), columns=b10.get_feature_names())
    b15 = b14
    b16 = b9['Name']
    return b15, b16
if b17 = = "__main__":
    pass
