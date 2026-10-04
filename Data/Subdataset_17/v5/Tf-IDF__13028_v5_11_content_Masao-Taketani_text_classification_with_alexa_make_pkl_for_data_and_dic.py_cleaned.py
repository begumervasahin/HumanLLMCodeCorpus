import os
import glob
import pickle
import tfidf
def read_files(path, label, labels):
    print(f"Reading files from: {path}")
    files = glob.glob(os.path.join(path, "*.txt"))
    for file_path in files:
        if os.path.basename(file_path) == 'LICENSE.txt':
            continue
        tfidf.add_file(file_path)
        labels.append(label)
def save_pickle(data, filepath):
    with open(filepath, 'wb') as pkl_file:
        pickle.dump(data, pkl_file)
    if os.path.exists(filepath):
        print(f'{filepath} has been saved successfully.')
    else:
        print(f'Failed to save {filepath}.')
def process_files_and_save_pickles():
    labels = []
    directories = [
        ('data/text/sports-watch', 0),
        ('data/text/it-life-hack', 1),
        ('data/text/movie-enter', 2),
        ('data/text/international', 3)
    ]
    for directory, label in directories:
        read_files(directory, label, labels)
    tfidf_data = tfidf.calc_files()
    pickle_dir = 'data/pkl/'
    os.makedirs(pickle_dir, exist_ok=True)
    data_pickle_path = os.path.join(pickle_dir, "data.pkl")
    save_pickle([labels, tfidf_data], data_pickle_path)
    dictionary_pickle_path = os.path.join(pickle_dir, 'dic.pkl')
    tfidf.save_dic(dictionary_pickle_path)
    if os.path.exists(dictionary_pickle_path):
        print('Dictionary pickle file has been saved successfully.')
    else:
        print('Failed to save the dictionary pickle file.')
if __name__ == "__main__":
    process_files_and_save_pickles()