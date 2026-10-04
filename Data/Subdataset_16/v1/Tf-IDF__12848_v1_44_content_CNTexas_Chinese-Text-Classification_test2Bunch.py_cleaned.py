import os
import pickle
from sklearn.utils import Bunch
import jieba
def fonk1(savepath, b1):
    with open(savepath, "wb") as fp:
        fp.write(b1)
def fonk2(path):
    with open(path, "rb") as fp:
        b1 = fp.read()
    return b1
b2 = Bunch(target_name=[], label=[], filenames=[], contents=[])
b3 = "test_word_bag/test_set.dat"
b4 = "test_corpus_seg/"
b5 = os.listdir(b4)
b2.target_name.extend(b5)
for mydir in b5:
    b6 = os.path.join(b4, mydir)
    b7 = os.listdir(b6)
    for file_path in b7:
        b8 = os.path.join(b6, file_path)
        b2.label.append(mydir)
        b2.filenames.append(b8)
        b2.contents.append(fonk2(b8).strip())
with open(b3, "wb") as file_obj:
    pickle.dump(b2, file_obj)
print("æå»ºææ¬å¯¹è±¡ç»æï¼ï¼ï¼")