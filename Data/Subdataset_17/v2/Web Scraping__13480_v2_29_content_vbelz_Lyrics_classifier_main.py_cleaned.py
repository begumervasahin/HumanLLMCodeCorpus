import argparse
import os
import pandas as pd
from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
from training import train_bayes, train_logistic
from prediction import predict_from_text
def main(args):
    folder_save = args.weights_folder
    nb_artist = args.nb_artist
    artist = args.list_artist
    mode = args.mode
    data_folder = args.data_folder
    file_name_to_save = args.name_file_to_save
    file_name_to_read = args.name_file_to_read
    scraping_mode = mode == 'scraping'
    training_mode = mode == 'training'
    prediction_mode = mode == 'prediction'
    if scraping_mode:
        if artist != parser.get_default('list_artist'):
            artist = [a.strip().lower() for a in artist.split(',')]
        if nb_artist == len(artist):
            print(f'You are going to scrape for {nb_artist} artists with names: {", ".join(artist)}')
            for artist_name in artist:
                print(artist_name)
                create_database_save_to_disk(artist_name, data_folder)
            merge_databases_into_one(artist, data_folder, file_name_to_save)
        else:
            print("Inconsistency between the number of artists and the list of artists.")
            print("Please relaunch the command line following the recommendations.")
    if training_mode:
        print(f'You are going to train the models on this database: {os.path.join(data_folder, file_name_to_read)}')
        df_read = pd.read_csv(os.path.join(data_folder, file_name_to_read))
        X, y = prepare_training(df_read, folder_save)
        train_bayes(X, y, folder_save)
        train_logistic(X, y, folder_save)
    if prediction_mode:
        if artist != parser.get_default('list_artist'):
            artist = [a.strip().lower() for a in artist.split(',')]
        sentence_to_ask = f'Give me some text from lyrics between {", ".join(artist)}: '
        text = input(sentence_to_ask)
        predict_from_text(text, folder_save)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Artist Lyrics Processing')
    parser.add_argument('--weights_folder', type=str, required=True, help='Folder to save model weights')
    parser.add_argument('--nb_artist', type=int, required=True, help='Number of artists')
    parser.add_argument('--list_artist', type=str, required=True, help='Comma-separated list of artist names')
    parser.add_argument('--mode', type=str, required=True, choices=['scraping', 'training', 'prediction'], help='Mode of operation')
    parser.add_argument('--data_folder', type=str, required=True, help='Folder to save data')
    parser.add_argument('--name_file_to_save', type=str, required=True, help='File name to save the merged database')
    parser.add_argument('--name_file_to_read', type=str, required=True, help='File name to read the database for training')
    args = parser.parse_args()
    main(args)