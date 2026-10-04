import os
import pickle
from sklearn.utils import Bunch
import jieba
def savefile(savepath, content):
    with open(savepath, "wb") as fp:
        fp.write(content)
def readfile(path):
    with open(path, "rb") as fp:
        return fp.read()
def create_bunch(seg_path, wordbag_path):
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    catelist = os.listdir(seg_path)
    bunch.target_name.extend(catelist)
    for category in catelist:
        class_path = os.path.join(seg_path, category)
        file_list = os.listdir(class_path)
        for file_name in file_list:
            full_path = os.path.join(class_path, file_name)
            content = readfile(full_path).strip()
            bunch.label.append(category)
            bunch.filenames.append(full_path)
            bunch.contents.append(content)
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("Text object construction completed!")
if __name__ == "__main__":
    SEG_PATH = "test_corpus_seg/"
    WORDBAG_PATH = "test_word_bag/test_set.dat"
    create_bunch(SEG_PATH, WORDBAG_PATH)