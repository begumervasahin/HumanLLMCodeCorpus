import os
import jieba
import pickle
from sklearn.datasets import Bunch
def fonk1(save_path, b1):
    with open(save_path, "wb") as fp:
        fp.write(b1)
def fonk2(path):
    with open(path, "rb") as fp:
        b1 = fp.read()
    return b1
b2 = Bunch(target_name=[], label=[], filenames=[], contents=[])
b3 = "train_word_bag/train_set.dat"
b4 = "train_corpus_seg/"
b5 = os.listdir(b4)
b2.target_name.extend(b5)
for mydir in b5:
    b6 = os.path.join(b4, mydir)
    b7 = os.listdir(b6)
    for file_name in b7:
        b8 = os.path.join(b6, file_name)
        b2.label.append(mydir)
        b2.filenames.append(b8)
        b2.contents.append(fonk2(b8).strip())
with open(b3, "wb") as file_obj:
    pickle.dump(b2, file_obj)
print("æå»ºææ¬å¯¹è±¡ç»æï¼ï¼ï¼")