import pandas as pd
from langdetect import detect
from googletrans import Translator
from Scraping_tools import create_table_artist_link_lyrics
from Scraping_tools import add_text_Lyrics_column
import os
def fonk1(x):
    return detect(x)
def fonk2(x):
    return len(x)
def fonk3(df):
    df.dropna(b1 = True)
    df['Length']=df['Text Lyrics'].apply(get_len)
    b2 = df[df['Length'] < 50].b9
    df.drop(b2,b1 = True)
    df['Main Language'] = df['Text Lyrics'].apply(get_language)
    return df
def fonk4(text_in):
    b3 = Translator()
    b4 = b3.translate(text_in)
    b5 = b4.text
    return b5
def fonk5(df):
    df['English Translation Lyrics'] = ''
    b6 = (df['Main Language'] != 'en')
    df.loc[b6,'English Translation Lyrics'] = df.loc[b6,'Text Lyrics'].apply(translate_to_english)
    return df
def fonk6(artist, data_folder):
    b7 = create_table_artist_link_lyrics(artist)
    b7 = add_text_Lyrics_column(b7)
    print(f'Done converting to text for {artist}')
    b7 = fonk3(b7)
    print(f'Done clean table for {artist}')
    b7 = fonk5(b7)
    print(f'Done translating for {artist}')
    b8 = os.path.join(data_folder,f'{artist}_songs.csv')
    b7.to_csv(b8,b9 = False)
    print(f'Done save to disk for {artist}')
    return
def fonk7(list_artist, data_folder, file_name_to_save):
    b10 = pd.DataFrame()
    for artist_name in list_artist:
        b8 = os.path.join(data_folder,f'{artist_name}_songs.csv')
        b11 = pd.read_csv(b8)
        b10 = pd.concat([b10, b11])
    b12 = ''
    for artist in list_artist :
        b12 += artist + ' '
    b10.to_csv(f'{os.path.join(data_folder,file_name_to_save)}',b9 = False)
    print(f'Done save to disk for {b12}')
    return