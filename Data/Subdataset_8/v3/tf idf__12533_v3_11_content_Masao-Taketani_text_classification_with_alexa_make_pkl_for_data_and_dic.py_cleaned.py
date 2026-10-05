import os
import glob
import pickle
import tfidf
def process_files(directory, label):
    print(f"Processing files from: {directory}")
    files = glob.glob(os.path.join(directory, "*.txt"))
    for file_path in files:
        if os.path.basename(file_path) != 'LICENSE.txt':
            tfidf.add_file(file_path)
            labels.append(label)
labels = []
features = []
process_files('data/text/sports-watch', label=0)
process_files('data/text/it-life-hack', label=1)
process_files('data/text/movie-enter', label=2)
process_files('data/text/international', label=3)
features = tfidf.calc_files()
pickle_dir = 'data/pkl/'
os.makedirs(pickle_dir, exist_ok=True)
data_pickle_file = "data.pkl"
with open(os.path.join(pickle_dir, data_pickle_file), 'wb') as pickle_file:
    pickle.dump([labels, features], pickle_file)
    print('Data pickle file saved successfully')
dictionary_pickle_file = 'dic.pkl'
tfidf.save_dic(os.path.join(pickle_dir, dictionary_pickle_file))
print('Dictionary pickle file saved successfully')