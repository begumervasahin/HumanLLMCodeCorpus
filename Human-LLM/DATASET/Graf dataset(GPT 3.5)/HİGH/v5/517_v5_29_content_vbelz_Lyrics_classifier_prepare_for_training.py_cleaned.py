import spacy as spacy_en
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
b1 = spacy_en.load('en_core_web_md')
def fonk1(song):
    b2 = b1(song)
    b3 = ' '.join(word.lemma_ for word in b2 if not (word.is_stop or word.pos_ in ['PUNCT', 'NUM']))
    return b3
def fonk2(df):
    b4 = df[df['Main Language'] == 'en'].drop(columns=['English Translation Lyrics'])
    return b4
def fonk3(df):
    df['Text Lyrics'] = df['Text Lyrics'].apply(clean_my_text)
    return df
def fonk4(b8, b10, folder_save):
    b5 = os.path.join(folder_save, 'countvector.sav')
    pickle.dump(b8, open(b5, 'wb'))
    b6 = os.path.join(folder_save, 'b6.sav')
    pickle.dump(b10, open(b6, 'wb'))
def fonk5(df_read, folder_save):
    b7 = fonk2(df_read)
    b7 = fonk3(b7)
    b8 = CountVectorizer()
    b9 = b8.fit_transform(b7['Text Lyrics'])
    b10 = TfidfTransformer()
    b11 = b10.fit_transform(b9)
    fonk4(b8, b10, folder_save)
    b12 = pd.DataFrame(b11.todense(), columns=b8.get_feature_names())
    b13 = b7['Name']
    b14 = b12
    return b14, b13