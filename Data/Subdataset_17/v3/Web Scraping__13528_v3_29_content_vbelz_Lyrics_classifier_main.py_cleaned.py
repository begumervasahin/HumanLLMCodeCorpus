import argparse
import os
import pandas as pd
from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
from training import train_bayes, train_logistic
from prediction import predict_from_text
def main(args):
    weights_folder = args.weights_folder
    num_artists = args.nb_artist
    artist_list = args.list_artist
    operation_mode = args.mode
    data_folder = args.data_folder
    save_filename = args.name_file_to_save
    read_filename = args.name_file_to_read
    is_scraping_mode = operation_mode == 'scraping'
    is_training_mode = operation_mode == 'training'
    is_prediction_mode = operation_mode == 'prediction'
    if is_scraping_mode:
        if artist_list != parser.get_default('list_artist'):
            artist_list = [artist.strip().lower() for artist in artist_list.split(',')]
        if num_artists == len(artist_list):
            print(f'You are going to scrape data for {num_artists} artists: {", ".join(artist_list)}')
            for artist_name in artist_list:
                print(f'Scraping data for {artist_name}...')
                create_database_save_to_disk(artist_name, data_folder)
            merge_databases_into_one(artist_list, data_folder, save_filename)
        else:
            print("The number of artists does not match the length of the artist list.")
            print("Please relaunch the command with the correct parameters.")
    elif is_training_mode:
        print(f'You are going to train the models on the database: {os.path.join(data_folder, read_filename)}')
        df = pd.read_csv(os.path.join(data_folder, read_filename))
        X, y = prepare_training(df, weights_folder)
        train_bayes(X, y, weights_folder)
        train_logistic(X, y, weights_folder)
    elif is_prediction_mode:
        if artist_list != parser.get_default('list_artist'):
            artist_list = [artist.strip().lower() for artist in artist_list.split(',')]
        prompt = f'Give me some text from lyrics between {", ".join(artist_list)}: '
        lyrics_text = input(prompt)
        predict_from_text(lyrics_text, weights_folder)
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