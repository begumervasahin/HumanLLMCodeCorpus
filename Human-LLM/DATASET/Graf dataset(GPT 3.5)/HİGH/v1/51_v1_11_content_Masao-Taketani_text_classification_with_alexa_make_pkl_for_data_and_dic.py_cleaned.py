import os
import glob
import pickle
import tfidf
b1 = []
b2 = []
def fonk1(path, label):
    print("Reading b3 from:", path)
    b3 = glob.glob(path + "/*.txt")
    for f in b3:
        if os.path.basename(f) == 'LICENSE.txt':
            continue
        tfidf.add_file(f)
        b1.append(label)
fonk1('data/text/sports-watch', 0)
fonk1('data/text/it-life-hack', 1)
fonk1('data/text/movie-enter', 2)
fonk1('data/text/international', 3)
b2 = tfidf.calc_files()
b4 = 'data/pkl/'
os.makedirs(b4, b5 = True)
b6 = "data.pkl"
with open(b4 + b6, 'wb') as f:
    pickle.dump([b1, b2], f)
    print('Data pickle file saved successfully')
b7 = 'dic.pkl'
tfidf.save_dic(b4 + b7)
print('Dictionary pickle file saved successfully')