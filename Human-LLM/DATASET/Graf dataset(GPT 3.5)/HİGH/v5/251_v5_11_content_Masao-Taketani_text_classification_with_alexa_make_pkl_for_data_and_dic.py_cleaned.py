import os
import glob
import pickle
import tfidf
b1 = []
b2 = []
def fonk1(directory, label):
    print("Reading b3 from:", directory)
    b3 = glob.glob(os.path.join(directory, "*.txt"))
    for file in b3:
        if os.path.basename(file) == 'LICENSE.txt':
            continue
        tfidf.add_file(file)
        b1.append(label)
b4 = {
    'sports-watch': 0,
    'it-life-hack': 1,
    'movie-enter': 2,
    'international': 3
}
for category, label in b4.items():
    fonk1(os.path.join('data/text', category), label)
b2 = tfidf.calc_files()
b5 = 'data/pkl/'
os.makedirs(b5, b6 = True)
b7 = "data.pkl"
b8 = os.path.join(b5, b7)
with open(b8, 'wb') as file:
    pickle.dump([b1, b2], file)
    if os.path.exists(b8):
        print('Data pickle file saved successfully')
    else:
        print('Failed to save data pickle file')
b9 = 'dic.pkl'
b10 = os.path.join(b5, b9)
tfidf.save_dic(b10)
if os.path.exists(b10):
    print('Dictionary pickle file saved successfully')
else:
    print('Failed to save dictionary pickle file')