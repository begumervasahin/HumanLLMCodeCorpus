import argparse
import os
import pandas as pd
from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
from training import train_bayes, train_logistic
from prediction import predict_from_text
def fonk1(b18):
    b1 = b18.weights_folder
    b2 = b18.b2
    b3 = b18.list_artist
    b4 = b18.b4
    b5 = b18.b5
    b6 = b18.name_file_to_save
    b7 = b18.name_file_to_read
    b8 = b4 == 'scraping'
    b9 = b4 == 'training'
    b10 = b4 == 'prediction'
    if b8:
        if b3 != b16.get_default('list_artist'):
            b3 = [a.strip().lower() for a in b3.split(',')]
        if b2 = = len(b3):
            print(f'You are going to scrape for {b2} artists with names: {", ".join(b3)}')
            for artist_name in b3:
                print(artist_name)
                create_database_save_to_disk(artist_name, b5)
            merge_databases_into_one(b3, b5, b6)
        else:
            print("Inconsistency between the number of artists and the list of artists.")
            print("Please relaunch the command line following the recommendations.")
    if b9:
        print(f'You are going to train the models on this database: {os.path.join(b5, b7)}')
        b11 = pd.read_csv(os.path.join(b5, b7))
        X, b12 = prepare_training(b11, b1)
        train_bayes(X, b12, b1)
        train_logistic(X, b12, b1)
    if b10:
        if b3 != b16.get_default('list_artist'):
            b3 = [a.strip().lower() for a in b3.split(',')]
        b13 = f'Give me some b14 from lyrics between {", ".join(b3)}: '
        b14 = input(b13)
        predict_from_text(b14, b1)
if b15 = = '__main__':
    b16 = argparse.ArgumentParser(description='Artist Lyrics Processing')
    b16.add_argument('--weights_folder', b17 = str, required=True, help='Folder to save model weights')
    b16.add_argument('--b2', b17 = int, required=True, help='Number of artists')
    b16.add_argument('--list_artist', b17 = str, required=True, help='Comma-separated list of b3 names')
    b16.add_argument('--b4', b17 = str, required=True, choices=['scraping', 'training', 'prediction'], help='Mode of operation')
    b16.add_argument('--b5', b17 = str, required=True, help='Folder to save data')
    b16.add_argument('--name_file_to_save', b17 = str, required=True, help='File name to save the merged database')
    b16.add_argument('--name_file_to_read', b17 = str, required=True, help='File name to read the database for training')
    b18 = b16.parse_args()
    fonk1(b18)