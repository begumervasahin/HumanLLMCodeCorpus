import os
import pickle
from sklearn.datasets import Bunch
def save_file(save_path, content):
    with open(save_path, "wb") as file:
        file.write(content)
def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def create_bunch(segmentation_path, wordbag_file_path):
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    category_list = os.listdir(segmentation_path)
    bunch.target_name.extend(category_list)
    for category in category_list:
        category_path = os.path.join(segmentation_path, category)
        file_list = os.listdir(category_path)
        for file_name in file_list:
            full_file_path = os.path.join(category_path, file_name)
            bunch.label.append(category)
            bunch.filenames.append(full_file_path)
            bunch.contents.append(read_file(full_file_path).strip())
    with open(wordbag_file_path, "wb") as file:
        pickle.dump(bunch, file)
    print("Text object construction completed!")
wordbag_path = "test_word_bag/test_set.dat"
segmentation_path = "test_corpus_seg/"
create_bunch(segmentation_path, wordbag_path)