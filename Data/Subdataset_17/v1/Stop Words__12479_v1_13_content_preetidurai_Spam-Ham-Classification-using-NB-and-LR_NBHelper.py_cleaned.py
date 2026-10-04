import os
import re
word_regex = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def getWords(text):
    return list(word_regex.findall(text.lower()))
def getWordsSansStopWords(text, stopWords):
    words = list(word_regex.findall(text.lower()))
    newWordList = [word for word in words if word not in stopWords]
    return newWordList
def getMailDictionary(path):
    messages = {}
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in files:
        filePath = os.path.join(path, file)
        with open(filePath, encoding='utf-8', errors='ignore') as mailFile:
            messages[file] = getWords(mailFile.read())
    return messages
def getMailDictionaryWOStopWords(path, stopWords):
    messages = {}
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in files:
        filePath = os.path.join(path, file)
        with open(filePath, encoding='utf-8', errors='ignore') as mailFile:
            messages[file] = getWordsSansStopWords(mailFile.read(), stopWords)
    return messages
def readStopWords(path):
    with open(path, encoding='utf-8', errors='ignore') as stopFile:
        stopWords = getWords(stopFile.read())
    return stopWords
def getVocabulary(mailDict):
    vocab = []
    for value in mailDict.values():
        vocab.extend(value)
    return vocab
if __name__ == "__main__":
    mail_dir = "path_to_mails"
    stop_words_file = "path_to_stopwords.txt"
    stopWords = readStopWords(stop_words_file)
    mailDict = getMailDictionary(mail_dir)
    mailDictWOStopWords = getMailDictionaryWOStopWords(mail_dir, stopWords)
    vocab = getVocabulary(mailDict)
    vocabWOStopWords = getVocabulary(mailDictWOStopWords)
    print("Mail Dictionary:", mailDict)
    print("Mail Dictionary Without Stop Words:", mailDictWOStopWords)
    print("Vocabulary:", vocab)
    print("Vocabulary Without Stop Words:", vocabWOStopWords)