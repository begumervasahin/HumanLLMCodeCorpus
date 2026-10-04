import os
import pickle
from sklearn.datasets import Bunch
def fonk1(save_path, content):
    with open(save_path, "wb") as file:
        file.write(content)
def fonk2(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def fonk3(b7, wordbag_file_path):
    b1 = Bunch(target_name=[], label=[], filenames=[], contents=[])
    b2 = os.listdir(b7)
    b1.target_name.extend(b2)
    for category in b2:
        b3 = os.path.join(b7, category)
        b4 = os.listdir(b3)
        for file_name in b4:
            b5 = os.path.join(b3, file_name)
            b1.label.append(category)
            b1.filenames.append(b5)
            b1.contents.append(fonk2(b5).strip())
    with open(wordbag_file_path, "wb") as file:
        pickle.dump(b1, file)
    print("Text object construction completed!")
b6 = "test_word_bag/test_set.dat"
b7 = "test_corpus_seg/"
fonk3(b7, b6)