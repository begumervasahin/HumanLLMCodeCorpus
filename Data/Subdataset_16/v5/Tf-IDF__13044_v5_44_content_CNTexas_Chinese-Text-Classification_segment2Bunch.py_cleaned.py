import os
import pickle
from sklearn.datasets import Bunch
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def fonk1(save_path, content):
    with open(save_path, "wb") as fp:
        fp.write(content)
def fonk2(path):
    with open(path, "rb") as fp:
        return fp.read()
def fonk3(b8, b7):
    b1 = Bunch(target_name=[], label=[], filenames=[], contents=[])
    b2 = os.listdir(b8)
    b1.target_name.extend(b2)
    for category in b2:
        b3 = os.path.join(b8, category)
        b4 = os.listdir(b3)
        for file_name in b4:
            b5 = os.path.join(b3, file_name)
            b1.label.append(category)
            b1.filenames.append(b5)
            b1.contents.append(fonk2(b5).strip())
    with open(b7, "wb") as file_obj:
        pickle.dump(b1, file_obj)
    print("Text object construction completed!!!")
if b6 = = "__main__":
    b7 = "train_word_bag/train_set.dat"
    b8 = "train_corpus_seg/"
    fonk3(b8, b7)