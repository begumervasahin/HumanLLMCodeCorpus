import os
import glob
import pickle
import tfidf
def fonk1(directory, b4):
    print(f"Processing b1 from: {directory}")
    b1 = glob.glob(os.path.join(directory, "*.txt"))
    for file_path in b1:
        if os.path.basename(file_path) != 'LICENSE.txt':
            tfidf.add_file(file_path)
            b2.append(b4)
b2 = []
b3 = []
fonk1('data/text/sports-watch', b4 = 0)
fonk1('data/text/it-life-hack', b4 = 1)
fonk1('data/text/movie-enter', b4 = 2)
fonk1('data/text/international', b4 = 3)
b3 = tfidf.calc_files()
b5 = 'data/pkl/'
os.makedirs(b5, b6 = True)
b7 = "data.pkl"
with open(os.path.join(b5, b7), 'wb') as pickle_file:
    pickle.dump([b2, b3], pickle_file)
    print('Data pickle file saved successfully')
b8 = 'dic.pkl'
tfidf.save_dic(os.path.join(b5, b8))
print('Dictionary pickle file saved successfully')