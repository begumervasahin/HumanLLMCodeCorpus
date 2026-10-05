import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
f = open("tech_text_final.txt", "r", encoding="utf-8")
dataFile = open("output.txt", "w", encoding="utf-8")
lemmaFile = open("lemma.txt", "w+", encoding="utf-8")
tagFile = open("tags.txt", "w", encoding="utf-8")
wordDict = {}
def processModel():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    text = f.read()
    test = text.split("à¥¤")
    for line in test:
        line = re.sub(r'(\d+)', r' ', line)
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.split()
        for word in line:
            if word:
                tagged_word = tnt_pos_tagger.tag(nltk.word_tokenize(word))
                dataFile.write(word.rstrip() + "\n")
                tagFile.write(word.rstrip() + " : " + tagged_word[0][1] + "\n")
    tagFile.close()
    dataFile.close()
def lemmatize():
    with open("tags.txt", "r", encoding="utf-8") as d:
        data1 = d.read().split("\n")
    for token in data1:
        if not token:
            continue
        line = token.split(":")
        if line[1].strip().startswith("NN") or line[1].strip().startswith("PR") or line[1].strip().startswith("VAUX"):
            wordDict[line[0].strip()] = [line[0].strip()]
        else:
            generate_stem_words(line[0].strip())
def generate_stem_words(word):
    suffixes = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    rule1 = suffixes[4][17]
    rule2 = suffixes[4][16]
    rule3 = suffixes[1][1]
    rule4 = suffixes[1][6]
    rule5 = suffixes[1][4]
    rule6 = suffixes[5][4]
    rule7 = suffixes[5][5]
    rule8 = suffixes[5][6]
    if word.endswith(rule1):
        wordDict[word] = [word[:word.rindex(rule1)] + suffixes[1][4]]
    elif word.endswith(rule2):
        wordDict[word] = [word[:word.rindex(rule2)] + suffixes[1][4]]
    elif word.endswith(rule3):
        wordDict[word] = [word[:word.rindex(rule3)] + suffixes[1][6]]
    elif word.endswith(rule4):
        wordDict[word] = [word[:word.rindex(rule4)] + suffixes[1][6]]
    elif word.endswith(rule5):
        wordDict[word] = [word[:word.rindex(rule5)] + suffixes[1][4]]
    elif word.endswith(rule6):
        wordDict[word] = [word[:word.rindex(rule6)] + suffixes[3][2]]
    elif word.endswith(rule7):
        wordDict[word] = [word[:word.rindex(rule7)] + suffixes[3][2]]
    elif word.endswith(rule8):
        wordDict[word] = [word[:word.rindex(rule8)] + suffixes[3][2]]
    else:
        if wordDict.get(word, None) is None:
            wordDict[word] = []
        for key in suffixes.keys():
            for value in suffixes[key]:
                if word.endswith(value):
                    suff = word.rindex(value)
                    wordDict[word].append(word[:suff])
def printdict():
    for k, v in wordDict.items():
        if not v:
            lemmaFile.write(k + ": " + k)
        else:
            lemmaFile.write(k + ": ")
            for element in set(v):
                lemmaFile.write(element + " ")
        lemmaFile.write("\n")
def main():
    processModel()
    lemmatize()
    printdict()
if __name__ == "__main__":
    main()