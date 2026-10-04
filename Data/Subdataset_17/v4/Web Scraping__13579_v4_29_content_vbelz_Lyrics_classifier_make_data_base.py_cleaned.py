import os
import pandas as pd
from langdetect import detect
from googletrans import Translator
from Scraping_tools import create_table_artist_link_lyrics, add_text_Lyrics_column
def detect_language(text):
    return detect(text)
def text_length(text):
    return len(text)
def clean_and_add_language_column(df):
    df.dropna(inplace=True)
    df['Length'] = df['Text Lyrics'].apply(text_length)
    df = df[df['Length'] >= 50]
    df['Main Language'] = df['Text Lyrics'].apply(detect_language)
    return df
def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text)
    return translation.text
def add_english_translation(df):
    df['English Translation Lyrics'] = ''
    non_english_mask = df['Main Language'] != 'en'
    df.loc[non_english_mask, 'English Translation Lyrics'] = df.loc[non_english_mask, 'Text Lyrics'].apply(translate_to_english)
    return df
def create_and_save_artist_database(artist, data_folder):
    df_artist = create_table_artist_link_lyrics(artist)
    df_artist = add_text_Lyrics_column(df_artist)
    print(f'Completed converting to text for {artist}')
    df_artist = clean_and_add_language_column(df_artist)
    print(f'Completed cleaning table for {artist}')
    df_artist = add_english_translation(df_artist)
    print(f'Completed translating lyrics for {artist}')
    file_path = os.path.join(data_folder, f'{artist}_songs.csv')
    df_artist.to_csv(file_path, index=False)
    print(f'Saved to disk for {artist}')
def merge_databases(list_of_artists, data_folder, output_file_name):
    merged_df = pd.DataFrame()
    for artist in list_of_artists:
        artist_file_path = os.path.join(data_folder, f'{artist}_songs.csv')
        artist_df = pd.read_csv(artist_file_path)
        merged_df = pd.concat([merged_df, artist_df])
    merged_df.to_csv(os.path.join(data_folder, output_file_name), index=False)
    print(f'Merged databases and saved to disk for {", ".join(list_of_artists)}')