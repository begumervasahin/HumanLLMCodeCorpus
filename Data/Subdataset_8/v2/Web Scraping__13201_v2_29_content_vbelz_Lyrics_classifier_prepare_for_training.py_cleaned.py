import spacy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import os
nlp = spacy.load('en_core_web_md')
def clean_lyrics(lyrics):
    doc = nlp(lyrics)
    clean_text = ''
    for token in doc:
        if (not token.is_stop) and (token.pos_ != 'PUNCT') and (token.pos_ != 'NUM'):
            word = token.lemma_
            clean_text += word + ' '
    return clean_text.strip()
def filter_english_songs(dataframe):
    english_songs = dataframe[dataframe['Main Language'] == 'en']
    english_songs.drop(['English Translation Lyrics'], axis=1, inplace=True)
    return english_songs
def apply_text_processing(dataframe):
    dataframe['Text Lyrics'] = dataframe['Text Lyrics'].apply(clean_lyrics)
    return dataframe
def save_transformations(cv, tfidf, folder_path):
    cv_path = os.path.join(folder_path, 'countvectorizer.sav')
    tfidf_path = os.path.join(folder_path, 'tfidftransformer.sav')
    with open(cv_path, 'wb') as cv_file:
        pickle.dump(cv, cv_file)
    with open(tfidf_path, 'wb') as tfidf_file:
        pickle.dump(tfidf, tfidf_file)
def prepare_training_data(input_data, save_folder):
    processed_data = filter_english_songs(input_data)
    processed_data = apply_text_processing(processed_data)
    count_vectorizer = CountVectorizer()
    lyrics_matrix = count_vectorizer.fit_transform(processed_data['Text Lyrics'])
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(lyrics_matrix)
    save_transformations(count_vectorizer, tfidf_transformer, save_folder)
    features_df = pd.DataFrame(tfidf_matrix.toarray(), columns=count_vectorizer.get_feature_names())
    X = features_df
    y = processed_data['Name']
    return X, y
if __name__ == "__main__":
    pass
