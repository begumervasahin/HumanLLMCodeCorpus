import os
import morph
import utils
from constants import *
def createCollection (b1 = ARTICLES_DIR_NAME):
    if not os.path.exists(b1):
        print('ÐÐ¨ÐÐÐÐ: Ð½Ðµ Ð¿Ð¾Ð»ÑÑÐ°ÐµÑÑÑ Ð½Ð°Ð¹ÑÐ¸ ÑÑÐ°ÑÑÐ¸')
        return -1
    normalizedArrayOfDocRes, b2 = morph.normalizeArrayOfDoc(extractText(b1).split(SPLIT_SENTENCES))
    utils.writeToFile(COLLECTIONS_FILE_NAME, normalizedArrayOfDocRes)
    utils.writeToFile(TF_FILE_NAME, b2)
    return 0
def extractText (dirName):
    b3 = ''
    for dirItem in os.listdir(dirName):
        b4 = os.path.join(dirName, dirItem)
        if os.path.isdir(b4):
            b3 += extractText(b4)
        _, b5 = os.path.splitext(b4)
        if b5 = = TXT_ETENSION:
            b6 = open(b4, FILE_MODE_READ)
            b3 += b6.read()
            b6.close()
    return b3