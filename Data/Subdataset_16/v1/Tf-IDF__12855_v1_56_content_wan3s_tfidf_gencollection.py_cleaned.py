import os
import morph
import utils
from constants import ARTICLES_DIR_NAME, COLLECTIONS_FILE_NAME, TF_FILE_NAME, SPLIT_SENTENCES, TXT_EXTENSION, FILE_MODE_READ
def fonk1(b1 = ARTICLES_DIR_NAME):
    if not os.path.exists(b1):
        print('ERROR: Unable to find articles')
        return -1
    b2 = fonk2(b1)
    if not b2:
        print('ERROR: No b2 extracted from articles')
        return -1
    normalized_array_of_doc_res, b3 = morph.normalize_array_of_doc(b2.split(SPLIT_SENTENCES))
    utils.write_to_file(COLLECTIONS_FILE_NAME, normalized_array_of_doc_res)
    utils.write_to_file(TF_FILE_NAME, b3)
    return 0
def fonk2(dir_name):
    b4 = ''
    for dir_item in os.listdir(dir_name):
        b5 = os.path.join(dir_name, dir_item)
        if os.path.isdir(b5):
            b4 += fonk2(b5)
        else:
            _, b6 = os.path.splitext(b5)
            if b6 = = TXT_EXTENSION:
                with open(b5, FILE_MODE_READ) as file:
                    b4 += file.read()
    return b4
if b7 = = "__main__":
    fonk1()