import spacy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
b1 = spacy.load('en_core_web_md')
def fonk1(lyrics):
    b2 = b1(lyrics)
    b3 = ''
    for token in b2:
        if (not token.is_stop) and (token.pos_ != 'PUNCT') and (token.pos_ != 'NUM'):
            b4 = token.lemma_
            b3 += b4 + ' '
    return b3.strip()
def fonk2(dataframe):
    b5 = dataframe[dataframe['Main Language'] == 'en']
    b5.drop(['English Translation Lyrics'], b6 = 1, inplace=True)
    return b5
def fonk3(dataframe):
    dataframe['Text Lyrics'] = dataframe['Text Lyrics'].apply(clean_lyrics)
    return dataframe
def fonk4(cv, tfidf, folder_path):
    b7 = os.path.join(folder_path, 'countvectorizer.sav')
    b8 = os.path.join(folder_path, 'tfidftransformer.sav')
    with open(b7, 'wb') as cv_file:
        pickle.dump(cv, cv_file)
    with open(b8, 'wb') as tfidf_file:
        pickle.dump(tfidf, tfidf_file)
def fonk5(input_data, save_folder):
    b9 = fonk2(input_data)
    b9 = fonk3(b9)
    b10 = CountVectorizer()
    b11 = b10.fit_transform(b9['Text Lyrics'])
    b12 = TfidfTransformer()
    b13 = b12.fit_transform(b11)
    fonk4(b10, b12, save_folder)
    b14 = pd.DataFrame(b13.toarray(), columns=b10.get_feature_names())
    b15 = b14
    b16 = b9['Name']
    return b15, b16
if b17 = = "__main__":
    pass
