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
    with open(data_pickle_path, 'wb') as data_pickle_file:
        pickle.dump([labels, tfidf_values], data_pickle_file)
    if os.path.exists(data_pickle_path):
        print('Data pickle file saved successfully')
    else:
        print('Failed to save data pickle file')
    dic_pickle_path = os.path.join(pickle_dir, 'dic.pkl')
    tfidf.save_dic(dic_pickle_path)
    if os.path.exists(dic_pickle_path):
        print('Dictionary pickle file saved successfully')
    else:
        print('Failed to save dictionary pickle file')
if __name__ == "__main__":
    main()