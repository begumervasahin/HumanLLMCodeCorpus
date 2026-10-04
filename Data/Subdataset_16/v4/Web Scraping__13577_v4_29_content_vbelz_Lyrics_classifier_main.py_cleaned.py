from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
import pandas as pd
from training import train_bayes, train_logistic
from prediction import predict_from_text
from b1 import parser
import os
def fonk1():
    b1 = parser.parse_args()
    b2 = b1.weights_folder
    b3 = b1.b3
    b4 = b1.list_artist
    b5 = b1.b5
    b6 = b1.b6
    b7 = b1.name_file_to_save
    b8 = b1.name_file_to_read
    b9 = b5 == 'scraping'
    b10 = b5 == 'training'
    b11 = b5 == 'prediction'
    if b9:
        fonk2(b4, b3, b6, b7)
    elif b10:
        fonk3(b6, b8, b2)
    elif b11:
        fonk4(b4, b2)
    else:
        print("Invalid b5 selected. Choose from 'scraping', 'training', or 'prediction'.")
def fonk2(b4, b3, b6, b7):
    if b4 != parser.get_default('list_artist'):
        b4 = [name.strip().lower() for name in ','.join(b4).split(',')]
    if b3 = = len(b4):
        print(f'You are going to scrape for {b3} artists with names: {", ".join(b4)}')
        for artist_name in b4:
            create_database_save_to_disk(artist_name, b6)
        merge_databases_into_one(b4, b6, b7)
    else:
        print("There is inconsistency between the number of artists and the list of artists. Relaunch the command line following recommendations.")
def fonk3(b6, b8, b2):
    print(f'You are going to train the models on this database: {os.path.join(b6, b8)}')
    b12 = pd.read_csv(os.path.join(b6, b8))
    X, b13 = prepare_training(b12, b2)
    train_bayes(X, b13, b2)
    train_logistic(X, b13, b2)
def fonk4(b4, b2):
    if b4 != parser.get_default('list_artist'):
        b4 = [name.strip() for name in ','.join(b4).split(',')]
    b14 = input(f'Give me some b14 from Lyrics between {", ".join(b4)}: ')
    predict_from_text(b14, b2)
if b15 = = '__main__':
    fonk1()