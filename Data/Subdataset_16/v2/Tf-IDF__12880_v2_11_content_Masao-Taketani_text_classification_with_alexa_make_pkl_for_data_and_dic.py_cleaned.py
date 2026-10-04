import os
import glob
import pickle
import tfidf
def fonk1(path, label, labels_list):
    print(f"Reading b1 from: {path}")
    b1 = glob.glob(os.path.join(path, "*.txt"))
    for file in b1:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        labels_list.append(label)
def fonk2():
    b2 = {
        'data/text/sports-watch': 0,
        'data/text/it-life-hack': 1,
        'data/text/movie-enter': 2,
        'data/text/international': 3
    }
    b3 = []
    for path, label in b2.items():
        fonk1(path, label, b3)
    b4 = tfidf.calc_files()
    b5 = 'data/pkl/'
    os.makedirs(b5, b6 = True)
    b7 = os.path.join(b5, "data.pkl")
    with open(b7, 'wb') as data_pickle_file:
        pickle.dump([b3, b4], data_pickle_file)
    if os.path.exists(b7):
        print('Data pickle file saved successfully')
    else:
        print('Failed to save data pickle file')
    b8 = os.path.join(b5, 'dic.pkl')
    tfidf.save_dic(b8)
    if os.path.exists(b8):
        print('Dictionary pickle file saved successfully')
    else:
        print('Failed to save dictionary pickle file')
if b9 = = "__main__":
    fonk2()