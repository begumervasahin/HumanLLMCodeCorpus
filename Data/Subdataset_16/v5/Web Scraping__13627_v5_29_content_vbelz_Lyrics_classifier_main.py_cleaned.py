import os
import pandas as pd
from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
from training import train_bayes, train_logistic
from prediction import predict_from_text
from b1 import parser
def fonk1():
    b1 = parser.parse_args()
    b2 = b1.weights_folder
    b3 = b1.b3
    b4 = b1.list_artist
    b5 = b1.b5
    b6 = b1.b6
    b7 = b1.name_file_to_save
    b8 = b1.name_file_to_read
    if b5 = = 'scraping':
        fonk2(b4, b3, b6, b7)
    elif b5 = = 'training':
        fonk3(b6, b8, b2)
    elif b5 = = 'prediction':
        fonk4(b4, b2)
    else:
        print("Invalid b5 selected. Choose from 'scraping', 'training', or 'prediction'.")
def fonk2(b4, b3, b6, b7):
    b4 = fonk5(b4)
    if b3 = = len(b4):
        print(f'Scraping data for {b3} artists: {", ".join(b4)}')
        for artist_name in b4:
            create_database_save_to_disk(artist_name, b6)
        merge_databases_into_one(b4, b6, b7)
    else:
        print("Inconsistency between the number of artists and the list of artists. Please relaunch the command with correct parameters.")
def fonk3(b6, b8, b2):
    print(f'Training models on database: {os.path.join(b6, b8)}')
    b9 = pd.read_csv(os.path.join(b6, b8))
    X, b10 = prepare_training(b9, b2)
    train_bayes(X, b10, b2)
    train_logistic(X, b10, b2)
def fonk4(b4, b2):
    b4 = fonk5(b4)
    b11 = input(f'Provide some b11 from lyrics between {", ".join(b4)}: ')
    predict_from_text(b11, b2)
def fonk5(artist_list):
    if artist_list != parser.get_default('list_artist'):
        return [name.strip().lower() for name in ','.join(artist_list).split(',')]
    return artist_list
if b12 = = '__main__':
    fonk1()