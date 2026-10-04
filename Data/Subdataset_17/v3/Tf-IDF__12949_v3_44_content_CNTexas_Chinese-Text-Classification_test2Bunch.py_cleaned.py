import os
import pickle
from sklearn.utils import Bunch
import jieba
def save_file(file_path, content):
    with open(file_path, "wb") as file:
        file.write(content)
def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def create_bunch_from_files(segmented_path, output_path):
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    categories = os.listdir(segmented_path)
    bunch.target_name.extend(categories)
    for category in categories:
        category_path = os.path.join(segmented_path, category)
        files = os.listdir(category_path)
        for file_name in files:
            file_path = os.path.join(category_path, file_name)
            content = read_file(file_path).strip()
            bunch.label.append(category)
            bunch.filenames.append(file_path)
            bunch.contents.append(content)
    with open(output_path, "wb") as output_file:
        pickle.dump(bunch, output_file)
    print("Text object construction completed!")
if __name__ == "__main__":
    SEGMENTED_PATH = "test_corpus_seg/"
    OUTPUT_PATH = "test_word_bag/test_set.dat"
    create_bunch_from_files(SEGMENTED_PATH, OUTPUT_PATH)