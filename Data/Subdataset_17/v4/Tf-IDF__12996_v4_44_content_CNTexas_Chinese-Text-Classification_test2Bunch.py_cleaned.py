import os
import pickle
from sklearn.datasets import Bunch
import jieba
def save_file(save_path, content):
    with open(save_path, "wb") as fp:
        fp.write(content)
def read_file(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content
bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
wordbag_path = "test_word_bag/test_set.dat"
seg_path = "test_corpus_seg/"
catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)
for mydir in catelist:
    class_path = os.path.join(seg_path, mydir)
    file_list = os.listdir(class_path)
    for file_name in file_list:
        full_name = os.path.join(class_path, file_name)
        bunch.label.append(mydir)
        bunch.filenames.append(full_name)
        bunch.contents.append(read_file(full_name).strip())
with open(wordbag_path, "wb") as file_obj:
    pickle.dump(bunch, file_obj)
print("Text object construction completed!")