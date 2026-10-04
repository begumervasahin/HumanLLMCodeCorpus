import pandas as pd
from langdetect import detect
from googletrans import Translator
from Scraping_tools import create_table_artist_link_lyrics
from Scraping_tools import add_text_Lyrics_column
import os
def fonk1(text):
    return detect(text)
def fonk2(text):
    return len(text)
def fonk3(b2):
    b2.dropna(b1 = True)
    b2['Length'] = b2['Text Lyrics'].apply(get_len)
    b2 = b2[b2['Length'] >= 50]
    b2['Main Language'] = b2['Text Lyrics'].apply(get_language)
    return b2
def fonk4(text_in):
    b3 = Translator()
    b4 = b3.translate(text_in)
    return b4.text
def fonk5(b2):
    b2['English Translation Lyrics'] = b2.apply(
        lambda row: fonk4(row['Text Lyrics']) if row['Main Language'] != 'en' else row['Text Lyrics'], a1 = 1
    )
    return b2
def fonk6(artist, data_folder):
    b5 = create_table_artist_link_lyrics(artist)
    b5 = add_text_Lyrics_column(b5)
    print(f'Done converting to text for {artist}')
    b5 = fonk3(b5)
    print(f'Done cleaning table for {artist}')
    b5 = fonk5(b5)
    print(f'Done translating for {artist}')
    b6 = os.path.join(data_folder, f'{artist}_songs.csv')
    b5.to_csv(b6, b7 = False)
    print(f'Done saving to disk for {artist}')
def fonk7(list_artist, data_folder, file_name_to_save):
    b8 = pd.DataFrame()
    for artist_name in list_artist:
        b6 = os.path.join(data_folder, f'{artist_name}_songs.csv')
        b9 = pd.read_csv(b6)
        b8 = pd.concat([b8, b9], ignore_index=True)
    b8.to_csv(os.path.join(data_folder, file_name_to_save), b7 = False)
    print(f'Done saving to disk for {", ".join(list_artist)}')
