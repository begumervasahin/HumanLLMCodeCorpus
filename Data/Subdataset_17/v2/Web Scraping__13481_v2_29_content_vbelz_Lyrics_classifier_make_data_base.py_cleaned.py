import pandas as pd
from langdetect import detect
from googletrans import Translator
from Scraping_tools import create_table_artist_link_lyrics, add_text_Lyrics_column
import os
def detect_language(text):
    return detect(text)
def text_length(text):
    return len(text)
def clean_and_add_language(df):
    df.dropna(inplace=True)
    df['Length'] = df['Text Lyrics'].apply(text_length)
    df = df[df['Length'] >= 50]
    df['Main Language'] = df['Text Lyrics'].apply(detect_language)
    return df
def translate_text_to_english(text):
    translator = Translator()
    translation = translator.translate(text)
    return translation.text
def add_english_translation(df):
    df['English Translation Lyrics'] = df.apply(
        lambda row: translate_text_to_english(row['Text Lyrics']) if row['Main Language'] != 'en' else row['Text Lyrics'],
        axis=1
    )
    return df
def create_artist_database(artist, data_folder):
    df_artist = create_table_artist_link_lyrics(artist)
    df_artist = add_text_Lyrics_column(df_artist)
    print(f'Finished converting to text for {artist}')
    df_artist = clean_and_add_language(df_artist)
    print(f'Finished cleaning table for {artist}')
    df_artist = add_english_translation(df_artist)
    print(f'Finished translating for {artist}')
    save_path = os.path.join(data_folder, f'{artist}_songs.csv')
    df_artist.to_csv(save_path, index=False)
    print(f'Saved to disk for {artist}')
def merge_artist_databases(artist_list, data_folder, output_filename):
    merged_df = pd.DataFrame()
    for artist in artist_list:
        file_path = os.path.join(data_folder, f'{artist}_songs.csv')
        artist_df = pd.read_csv(file_path)
        merged_df = pd.concat([merged_df, artist_df], ignore_index=True)
    output_path = os.path.join(data_folder, output_filename)
    merged_df.to_csv(output_path, index=False)
    print(f'Saved merged database for {", ".join(artist_list)}')
