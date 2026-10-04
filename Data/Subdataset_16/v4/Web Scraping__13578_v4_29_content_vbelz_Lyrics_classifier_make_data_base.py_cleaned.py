import os
import pandas as pd
from langdetect import detect
from googletrans import Translator
from Scraping_tools import create_table_artist_link_lyrics, add_text_Lyrics_column
def fonk1(text):
    return detect(text)
def fonk2(text):
    return len(text)
def fonk3(b2):
    b2.dropna(b1 = True)
    b2['Length'] = b2['Text Lyrics'].apply(text_length)
    b2 = b2[b2['Length'] >= 50]
    b2['Main Language'] = b2['Text Lyrics'].apply(detect_language)
    return b2
def fonk4(text):
    b3 = Translator()
    b4 = b3.translate(text)
    return b4.text
def fonk5(b2):
    b2['English Translation Lyrics'] = ''
    b5 = b2['Main Language'] != 'en'
    b2.loc[b5, 'English Translation Lyrics'] = b2.loc[b5, 'Text Lyrics'].apply(translate_to_english)
    return b2
def fonk6(artist, data_folder):
    b6 = create_table_artist_link_lyrics(artist)
    b6 = add_text_Lyrics_column(b6)
    print(f'Completed converting to text for {artist}')
    b6 = fonk3(b6)
    print(f'Completed cleaning table for {artist}')
    b6 = fonk5(b6)
    print(f'Completed translating lyrics for {artist}')
    b7 = os.path.join(data_folder, f'{artist}_songs.csv')
    b6.to_csv(b7, b8 = False)
    print(f'Saved to disk for {artist}')
def fonk7(list_of_artists, data_folder, output_file_name):
    b9 = pd.DataFrame()
    for artist in list_of_artists:
        b10 = os.path.join(data_folder, f'{artist}_songs.csv')
        b11 = pd.read_csv(b10)
        b9 = pd.concat([b9, b11])
    b9.to_csv(os.path.join(data_folder, output_file_name), b8 = False)
    print(f'Merged databases and saved to disk for {", ".join(list_of_artists)}')