import os
import pickle
from sklearn.datasets import Bunch
def save_file(save_path, content):
    with open(save_path, "wb") as file:
        file.write(content)
def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()
def create_bunch_from_directory(segmented_path, wordbag_output_path):
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    categories = os.listdir(segmented_path)
    bunch.target_name.extend(categories)
    for category in categories:
        category_path = os.path.join(segmented_path, category)
        file_list = os.listdir(category_path)
        for file_name in file_list:
            full_path = os.path.join(category_path, file_name)
            bunch.label.append(category)
            bunch.filenames.append(full_path)
            bunch.contents.append(read_file(full_path).strip())
    with open(wordbag_output_path, "wb") as file:
        pickle.dump(bunch, file)
    print("Bunch object creation completed successfully!")
if __name__ == "__main__":
    segmented_texts_path = "train_corpus_seg/"
    wordbag_save_path = "train_word_bag/train_set.dat"
    create_bunch_from_directory(segmented_texts_path, wordbag_save_path)