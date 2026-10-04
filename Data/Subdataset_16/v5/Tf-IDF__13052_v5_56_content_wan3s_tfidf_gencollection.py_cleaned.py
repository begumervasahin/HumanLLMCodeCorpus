import os
import morph
import utils
from constants import *
def fonk1(b1 = ARTICLES_DIR_NAME):
    if not os.path.exists(b1):
        print('ÐÐ¨ÐÐÐÐ: Ð½Ðµ Ð¿Ð¾Ð»ÑÑÐ°ÐµÑÑÑ Ð½Ð°Ð¹ÑÐ¸ ÑÑÐ°ÑÑÐ¸')
        return -1
    b2 = fonk2(b1)
    b3 = b2.split(SPLIT_SENTENCES)
    normalized_docs, b4 = morph.normalizeArrayOfDoc(b3)
    utils.writeToFile(COLLECTIONS_FILE_NAME, normalized_docs)
    utils.writeToFile(TF_FILE_NAME, b4)
    return 0
def fonk2(dir_name):
    b5 = ''
    for dir_item in os.listdir(dir_name):
        b6 = os.path.join(dir_name, dir_item)
        if os.path.isdir(b6):
            b5 += fonk2(b6)
        else:
            _, b7 = os.path.splitext(b6)
            if b7 = = TXT_EXTENSION:
                with open(b6, FILE_MODE_READ) as file:
                    b5 += file.read()
    return b5