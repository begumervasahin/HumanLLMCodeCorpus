import os
import morph
import utils
from constants import ARTICLES_DIR_NAME, COLLECTIONS_FILE_NAME, TF_FILE_NAME, SPLIT_SENTENCES, TXT_EXTENSION, FILE_MODE_READ
def create_collection(articles_path=ARTICLES_DIR_NAME):
    if not os.path.exists(articles_path):
        print('ERROR: Unable to find articles')
        return -1
    text = extract_text(articles_path)
    if not text:
        print('ERROR: No text extracted from articles')
        return -1
    normalized_array_of_doc_res, tf_counter = morph.normalize_array_of_doc(text.split(SPLIT_SENTENCES))
    utils.write_to_file(COLLECTIONS_FILE_NAME, normalized_array_of_doc_res)
    utils.write_to_file(TF_FILE_NAME, tf_counter)
    return 0
def extract_text(dir_name):
    result_text = ''
    for dir_item in os.listdir(dir_name):
        path_to_item = os.path.join(dir_name, dir_item)
        if os.path.isdir(path_to_item):
            result_text += extract_text(path_to_item)
        else:
            _, file_extension = os.path.splitext(path_to_item)
            if file_extension == TXT_EXTENSION:
                with open(path_to_item, FILE_MODE_READ) as file:
                    result_text += file.read()
    return result_text
if __name__ == "__main__":
    create_collection()