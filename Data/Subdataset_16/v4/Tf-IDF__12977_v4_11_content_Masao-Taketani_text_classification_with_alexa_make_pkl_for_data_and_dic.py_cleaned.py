import os
import glob
import pickle
import tfidf
def fonk1(path, label, b2):
    print("Reading b1 from:", path)
    b1 = glob.glob(os.path.join(path, "*.txt"))
    for file_path in b1:
        if os.path.basename(file_path) == 'LICENSE.txt':
            continue
        tfidf.add_file(file_path)
        b2.append(label)
def fonk2(data, filepath):
    with open(filepath, 'wb') as pkl_file:
        pickle.dump(data, pkl_file)
    if os.path.exists(filepath):
        print(f'{filepath} has been saved successfully.')
    else:
        print(f'Failed to save {filepath}.')
def fonk3():
    b2 = []
    b3 = [
        ('data/text/sports-watch', 0),
        ('data/text/it-life-hack', 1),
        ('data/text/movie-enter', 2),
        ('data/text/international', 3)
    ]
    for directory, label in b3:
        fonk1(directory, label, b2)
    b4 = tfidf.calc_files()
    b5 = 'data/pkl/'
    os.makedirs(b5, b6 = True)
    b7 = os.path.join(b5, "data.pkl")
    fonk2([b2, b4], b7)
    b8 = os.path.join(b5, 'dic.pkl')
    tfidf.save_dic(b8)
    if os.path.exists(b8):
        print('Dictionary pickle file has been saved successfully.')
    else:
        print('Failed to save the dictionary pickle file.')
if b9 = = "__main__":
    fonk3()