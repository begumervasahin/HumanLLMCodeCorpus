import spacy as spacy_en
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
model = spacy_en.load('en_core_web_md')
def clean_my_text(song):
    doc = model(song)
    clean_text = ''
    for word in doc:
        if (word.is_stop == False)  and (word.pos_ != 'PUNCT') and  (word.pos_ != 'NUM'):
            word = word.lemma_
            clean_text += word + ' '
    return clean_text
def keep_english_for_spacy_nn(df):
    df = df.loc[df['Main Language'] == 'en', :]
    df.drop(['English Translation Lyrics'], axis=1, inplace=True)
    return df
def apply_spacy_nn_to_DataFrame(df):
    df['Text Lyrics'] = df['Text Lyrics'].apply(clean_my_text)
    return df
def save_transform_to_disk(cv, tf, folder_save):
    countvectorfile = os.path.join(folder_save, 'countvector.sav')
    pickle.dump(cv, open(countvectorfile, 'wb'))
    Tfidfile = os.path.join(folder_save, 'Tfidfile.sav')
    pickle.dump(tf, open(Tfidfile, 'wb'))
    return
def prepare_training(df_read, folder_save):
    df_prep = keep_english_for_spacy_nn(df_read)
    df_prep = apply_spacy_nn_to_DataFrame(df_prep)
    cv = CountVectorizer()
    corpus_vec = cv.fit_transform(df_prep['Text Lyrics'])
    tf = TfidfTransformer()
    transform_vec = tf.fit_transform(corpus_vec)
    save_transform_to_disk(cv, tf, folder_save)
    df_word_vec = pd.DataFrame(transform_vec.todense(), columns=cv.get_feature_names())
    y = df_prep['Name']
    X = df_word_vec
    return X, y