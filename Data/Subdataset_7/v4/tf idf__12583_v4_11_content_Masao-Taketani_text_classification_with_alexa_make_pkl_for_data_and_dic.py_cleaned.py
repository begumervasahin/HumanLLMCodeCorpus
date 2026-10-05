import os
import glob
import pickle
import tfidf
b1 = []
b2 = []
def fonk1(directory, label):
    print("Reading b3 from:", directory)
    b3 = glob.glob(directory + "/*.txt")
    for file in b3:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        b1.append(label)
fonk1('data/text/sports-watch', 0)
fonk1('data/text/it-life-hack', 1)
fonk1('data/text/movie-enter', 2)
fonk1('data/text/international', 3)
b2 = tfidf.calc_files()
b4 = 'data/pkl/'
os.makedirs(b4, b5 = True)
b6 = "data.pkl"
with open(b4 + b6, 'wb') as file:
    pickle.dump([b1, b2], file)
    if os.path.exists(b4 + b6):
        print('Data pickle file saved successfully')
    else:
        print('Failed to save data pickle file')
b7 = 'dic.pkl'
tfidf.save_dic(b4 + b7)
if os.path.exists(b4 + b7):
    print('Dictionary pickle file saved successfully')
else:
    print('Failed to save dictionary pickle file')