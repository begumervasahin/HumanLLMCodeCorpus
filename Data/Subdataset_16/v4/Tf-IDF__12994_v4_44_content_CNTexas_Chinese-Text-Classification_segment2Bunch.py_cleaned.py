import os
import jieba
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
b1 = Bunch(target_name=[], label=[], filenames=[], contents=[])
b2 = "train_word_bag/train_set.dat"
b3 = "train_corpus_seg/"
b4 = os.listdir(b3)
b1.target_name.extend(b4)
for category in b4:
    b5 = os.path.join(b3, category)
    b6 = os.listdir(b5)
    for file_name in b6:
        b7 = os.path.join(b5, file_name)
        b1.label.append(category)
        b1.filenames.append(b7)
        b1.contents.append(fonk2(b7).strip())
with open(b2, "wb") as file_obj:
    pickle.dump(b1, file_obj)
print("Text object construction completed!!!")