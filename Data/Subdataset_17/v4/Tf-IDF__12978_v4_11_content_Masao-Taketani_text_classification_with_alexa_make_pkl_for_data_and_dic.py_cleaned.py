import os
import glob
import pickle
import tfidf
def read_files(path, label, y):
    print("Reading files from:", path)
    files = glob.glob(os.path.join(path, "*.txt"))
    for file_path in files:
        if os.path.basename(file_path) == 'LICENSE.txt':
            continue
        tfidf.add_file(file_path)
        y.append(label)
def save_pickle(data, filepath):
    with open(filepath, 'wb') as pkl_file:
        pickle.dump(data, pkl_file)
    if os.path.exists(filepath):
        print(f'{filepath} has been saved successfully.')
    else:
        print(f'Failed to save {filepath}.')
def main():
    y = []
    directories = [
        ('data/text/sports-watch', 0),
        ('data/text/it-life-hack', 1),
        ('data/text/movie-enter', 2),
        ('data/text/international', 3)
    ]
    for directory, label in directories:
        read_files(directory, label, y)
    x = tfidf.calc_files()
    dir_for_pkls = 'data/pkl/'
    os.makedirs(dir_for_pkls, exist_ok=True)
    pkl_for_data = os.path.join(dir_for_pkls, "data.pkl")
    save_pickle([y, x], pkl_for_data)
    pkl_for_dic = os.path.join(dir_for_pkls, 'dic.pkl')
    tfidf.save_dic(pkl_for_dic)
    if os.path.exists(pkl_for_dic):
        print('Dictionary pickle file has been saved successfully.')
    else:
        print('Failed to save the dictionary pickle file.')
if __name__ == "__main__":
    main()