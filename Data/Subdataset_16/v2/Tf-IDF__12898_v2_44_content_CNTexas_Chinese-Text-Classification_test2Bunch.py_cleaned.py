import os
import pickle
from sklearn.utils import Bunch
import jieba
def fonk1(savepath, b6):
    with open(savepath, "wb") as fp:
        fp.write(b6)
def fonk2(path):
    with open(path, "rb") as fp:
        return fp.read()
def fonk3(seg_path, wordbag_path):
    b1 = Bunch(target_name=[], label=[], filenames=[], contents=[])
    b2 = os.listdir(seg_path)
    b1.target_name.extend(b2)
    for category in b2:
        b3 = os.path.join(seg_path, category)
        b4 = os.listdir(b3)
        for file_name in b4:
            b5 = os.path.join(b3, file_name)
            b6 = fonk2(b5).strip()
            b1.label.append(category)
            b1.filenames.append(b5)
            b1.contents.append(b6)
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(b1, file_obj)
    print("Text object construction completed!")
if b7 = = "__main__":
    b8 = "test_corpus_seg/"
    b9 = "test_word_bag/test_set.dat"
    fonk3(b8, b9)