import os
import glob
import pickle
import tfidf
labels = []
features = []
def read_files(directory, label):
    print("Reading files from:", directory)
    files = glob.glob(directory + "/*.txt")
    for file in files:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        labels.append(label)
read_files('data/text/sports-watch', 0)
read_files('data/text/it-life-hack', 1)
read_files('data/text/movie-enter', 2)
read_files('data/text/international', 3)
features = tfidf.calc_files()
pkl_directory = 'data/pkl/'
os.makedirs(pkl_directory, exist_ok=True)
data_pickle_file = "data.pkl"
with open(pkl_directory + data_pickle_file, 'wb') as file:
    pickle.dump([labels, features], file)
    if os.path.exists(pkl_directory + data_pickle_file):
        print('Data pickle file saved successfully')
    else:
        print('Failed to save data pickle file')
dictionary_pickle_file = 'dic.pkl'
tfidf.save_dic(pkl_directory + dictionary_pickle_file)
if os.path.exists(pkl_directory + dictionary_pickle_file):
    print('Dictionary pickle file saved successfully')
else:
    print('Failed to save dictionary pickle file')