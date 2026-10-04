import pandas as pd
from langdetect import detect
from googletrans import Translator
from Scraping_tools import create_table_artist_link_lyrics, add_text_Lyrics_column
import os
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
    b2['English Translation Lyrics'] = b2.apply(
        lambda row: fonk4(row['Text Lyrics']) if row['Main Language'] != 'en' else row['Text Lyrics'],
        a1 = 1
    )
    return b2
def fonk6(artist, data_folder):
    b5 = create_table_artist_link_lyrics(artist)
    b5 = add_text_Lyrics_column(b5)
    print(f'Finished converting to text for {artist}')
    b5 = fonk3(b5)
    print(f'Finished cleaning table for {artist}')
    b5 = fonk5(b5)
    print(f'Finished translating for {artist}')
    b6 = os.path.join(data_folder, f'{artist}_songs.csv')
    b5.to_csv(b6, b7 = False)
    print(f'Saved to disk for {artist}')
def fonk7(artist_list, data_folder, output_filename):
    b8 = pd.DataFrame()
    for artist in artist_list:
        b9 = os.path.join(data_folder, f'{artist}_songs.csv')
        b10 = pd.read_csv(b9)
        b8 = pd.concat([b8, b10], ignore_index=True)
    b11 = os.path.join(data_folder, output_filename)
    b8.to_csv(b11, b7 = False)
    print(f'Saved merged database for {", ".join(artist_list)}')
