from make_data_base import create_database_save_to_disk, merge_databases_into_one
from prepare_for_training import prepare_training
import pandas as pd
from training import train_bayes, train_logistic
from prediction import predict_from_text
from b2 import parser
import os
if b1 = = '__main__':
    b2 = parser.parse_args()
    b3 = b2.weights_folder
    b4 = b2.b4
    b5 = b2.list_artist
    b6 = b2.b6
    b7 = b2.b7
    b8 = b2.name_file_to_save
    b9 = b2.name_file_to_read
    b10 = False
    b11 = False
    b12 = False
    if b6 = = 'prediction':
        b12 = True
    elif b6 = = 'training':
        b11 = True
    elif b6 = = 'scraping':
        b10 = True
    if b10:
        if b5 != parser.get_default('list_artist'):
            b13 = ''
            for item in b5:
                b13 += item
            b14 = b13.split(',')
            b5 = b14
        if (b4 = = len(b5)):
            b5 = [x.lower() for x in b5]
            b15 = f'You are going to scrape for {b4} artists with b16: '
            b16 = ''
            b16 = ', '.join(b5)
            b15 += b16 + '  '
            print(b15)
            for artist_name in b5:
                print(artist_name)
                create_database_save_to_disk(artist_name, b7)
            merge_databases_into_one(b5, b7, b8)
        else:
            print("There is inconsistency between number of b5 and list of b5\n")
            print("relaunch the command line following recommendations")
    if b11:
        print("You are going to train the models on this database : \n")
        print(f'{os.path.join(b7,b9)}')
        b17 = pd.read_csv(os.path.join(
            b7, b9))
        X, b18 = prepare_training(b17, b3)
        train_bayes(X, b18, b3)
        train_logistic(X, b18, b3)
    if b12:
        if b5 != parser.get_default('list_artist'):
            b13 = ''
            for item in b5:
                b13 += item
            b14 = b13.split(',')
            b5 = b14
        b15 = 'Give me some b19 from Lyrics between '
        b16 = ''
        b16 = ', '.join(b5)
        b15 += b16 + '  '
        b19 = input(b15)
        predict_from_text(b19, b3)