import os
import glob
import pickle
import tfidf
labels = []
features = []
def read_files(directory, label):
    print("Reading files from:", directory)
    files = glob.glob(os.path.join(directory, "*.txt"))
    for file in files:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        labels.append(label)
categories = {
    'sports-watch': 0,
    'it-life-hack': 1,
    'movie-enter': 2,
    'international': 3
}
for category, label in categories.items():
    read_files(os.path.join('data/text', category), label)
features = tfidf.calc_files()
pkl_directory = 'data/pkl/'
os.makedirs(pkl_directory, exist_ok=True)
data_pickle_file = "data.pkl"
data_pickle_path = os.path.join(pkl_directory, data_pickle_file)
with open(data_pickle_path, 'wb') as file:
    pickle.dump([labels, features], file)
    if os.path.exists(data_pickle_path):
        print('Data pickle file saved successfully')
    else:
        print('Failed to save data pickle file')
dictionary_pickle_file = 'dic.pkl'
dictionary_pickle_path = os.path.join(pkl_directory, dictionary_pickle_file)
tfidf.save_dic(dictionary_pickle_path)
if os.path.exists(dictionary_pickle_path):
    print('Dictionary pickle file saved successfully')
else:
    print('Failed to save dictionary pickle file')