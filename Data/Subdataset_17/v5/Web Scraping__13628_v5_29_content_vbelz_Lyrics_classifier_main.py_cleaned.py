import os
import pandas as pd
from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
from training import train_bayes, train_logistic
from prediction import predict_from_text
from args import parser
def main():
    args = parser.parse_args()
    folder_save = args.weights_folder
    nb_artist = args.nb_artist
    artist = args.list_artist
    mode = args.mode
    data_folder = args.data_folder
    file_name_to_save = args.name_file_to_save
    file_name_to_read = args.name_file_to_read
    if mode == 'scraping':
        handle_scraping(artist, nb_artist, data_folder, file_name_to_save)
    elif mode == 'training':
        handle_training(data_folder, file_name_to_read, folder_save)
    elif mode == 'prediction':
        handle_prediction(artist, folder_save)
    else:
        print("Invalid mode selected. Choose from 'scraping', 'training', or 'prediction'.")
def handle_scraping(artist, nb_artist, data_folder, file_name_to_save):
    artist = parse_artist_list(artist)
    if nb_artist == len(artist):
        print(f'Scraping data for {nb_artist} artists: {", ".join(artist)}')
        for artist_name in artist:
            create_database_save_to_disk(artist_name, data_folder)
        merge_databases_into_one(artist, data_folder, file_name_to_save)
    else:
        print("Inconsistency between the number of artists and the list of artists. Please relaunch the command with correct parameters.")
def handle_training(data_folder, file_name_to_read, folder_save):
    print(f'Training models on database: {os.path.join(data_folder, file_name_to_read)}')
    df = pd.read_csv(os.path.join(data_folder, file_name_to_read))
    X, y = prepare_training(df, folder_save)
    train_bayes(X, y, folder_save)
    train_logistic(X, y, folder_save)
def handle_prediction(artist, folder_save):
    artist = parse_artist_list(artist)
    text = input(f'Provide some text from lyrics between {", ".join(artist)}: ')
    predict_from_text(text, folder_save)
def parse_artist_list(artist_list):
    if artist_list != parser.get_default('list_artist'):
        return [name.strip().lower() for name in ','.join(artist_list).split(',')]
    return artist_list
if __name__ == '__main__':
    main()