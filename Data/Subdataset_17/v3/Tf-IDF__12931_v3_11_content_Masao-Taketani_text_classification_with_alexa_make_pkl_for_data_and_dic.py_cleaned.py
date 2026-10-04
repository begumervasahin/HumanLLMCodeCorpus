import os
import glob
import pickle
import tfidf
def read_files(path, label, labels_list):
    print(f"Reading files from: {path}")
    files = glob.glob(os.path.join(path, "*.txt"))
    for file in files:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        labels_list.append(label)
def save_pickle_file(data, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(data, file)
    if os.path.exists(filepath):
        print(f'Pickle file saved successfully at {filepath}')
    else:
        print(f'Failed to save pickle file at {filepath}')
def main():
    data_paths = {
        'data/text/sports-watch': 0,
        'data/text/it-life-hack': 1,
        'data/text/movie-enter': 2,
        'data/text/international': 3
    }
    labels = []
    for path, label in data_paths.items():
        read_files(path, label, labels)
    tfidf_values = tfidf.calc_files()
    pickle_dir = 'data/pkl/'
    os.makedirs(pickle_dir, exist_ok=True)
    data_pickle_path = os.path.join(pickle_dir, "data.pkl")
    save_pickle_file([labels, tfidf_values], data_pickle_path)
    dic_pickle_path = os.path.join(pickle_dir, 'dic.pkl')
    tfidf.save_dic(dic_pickle_path)
    if os.path.exists(dic_pickle_path):
        print('Dictionary pickle file saved successfully')
    else:
        print('Failed to save dictionary pickle file')
if __name__ == "__main__":
    main()