import os
import morph
import utils
from constants import (
    ARTICLES_DIR_NAME,
    COLLECTIONS_FILE_NAME,
    TF_FILE_NAME,
    SPLIT_SENTENCES,
    TXT_EXTENSION,
    FILE_MODE_READ
)
def create_collection(articles_path=ARTICLES_DIR_NAME):
    if not os.path.exists(articles_path):
        print('ERROR: Unable to find articles')
        return -1
    text = extract_text(articles_path)
    if not text:
        print('ERROR: No text extracted from articles')
        return -1
    normalized_docs, tf_counter = morph.normalize_array_of_doc(text.split(SPLIT_SENTENCES))
    utils.write_to_file(COLLECTIONS_FILE_NAME, normalized_docs)
    utils.write_to_file(TF_FILE_NAME, tf_counter)
    return 0
def extract_text(dir_name):
    result_text = []
    for item in os.listdir(dir_name):
        item_path = os.path.join(dir_name, item)
        if os.path.isdir(item_path):
            result_text.append(extract_text(item_path))
        else:
            _, ext = os.path.splitext(item_path)
            if ext == TXT_EXTENSION:
                with open(item_path, FILE_MODE_READ) as file:
                    result_text.append(file.read())
    return ''.join(result_text)
if __name__ == "__main__":
    create_collection()