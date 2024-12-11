import spacy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
b1 = spacy.load('en_core_web_md')
def fonk1(lyrics):
    b2 = b1(lyrics)
    b3 = ' '.join(token.lemma_ for token in b2 if not token.is_stop and token.pos_ not in ['PUNCT', 'NUM'])
    return b3.strip()
def fonk2(dataframe):
    b4 = dataframe[dataframe['Main Language'] == 'en'].drop(['English Translation Lyrics'], axis=1)
    return b4
def fonk3(dataframe):
    dataframe['Text Lyrics'] = dataframe['Text Lyrics'].apply(clean_lyrics)
    return dataframe
def fonk4(cv, tfidf, folder_path):
    b5 = os.path.join(folder_path, 'countvectorizer.sav')
    b6 = os.path.join(folder_path, 'tfidftransformer.sav')
    with open(b5, 'wb') as cv_file:
        pickle.dump(cv, cv_file)
    with open(b6, 'wb') as tfidf_file:
        pickle.dump(tfidf, tfidf_file)
def fonk5(input_data, save_folder):
    b7 = fonk3(fonk2(input_data))
    b8 = CountVectorizer()
    b9 = b8.fit_transform(b7['Text Lyrics'])
    b10 = TfidfTransformer()
    b11 = b10.fit_transform(b9)
    fonk4(b8, b10, save_folder)
    b12 = pd.DataFrame(b11.toarray(), columns=b8.get_feature_names())
    b13 = b12
    b14 = b7['Name']
    return b13, b14
if b15 = = "__main__":
    pass
