import os
import glob
import pickle
import tfidf
def read_files(path, label, y):
    print("Reading files from:", path)
    files = glob.glob(os.path.join(path, "*.txt"))
    for file in files:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        y.append(label)
data_paths = {
    'data/text/sports-watch': 0,
    'data/text/it-life-hack': 1,
    'data/text/movie-enter': 2,
    'data/text/international': 3
}
y = []
for path, label in data_paths.items():
    read_files(path, label, y)
x = tfidf.calc_files()
dir_for_pkls = 'data/pkl/'
os.makedirs(dir_for_pkls, exist_ok=True)
pkl_for_data = os.path.join(dir_for_pkls, "data.pkl")
with open(pkl_for_data, 'wb') as f:
    pickle.dump([y, x], f)
if os.path.exists(pkl_for_data):
    print('Data pickle file saved successfully')
else:
    print('Failed to save data pickle file')
pkl_for_dic = os.path.join(dir_for_pkls, 'dic.pkl')
tfidf.save_dic(pkl_for_dic)
if os.path.exists(pkl_for_dic):
    print('Dictionary pickle file saved successfully')
else:
    print('Failed to save dictionary pickle file')