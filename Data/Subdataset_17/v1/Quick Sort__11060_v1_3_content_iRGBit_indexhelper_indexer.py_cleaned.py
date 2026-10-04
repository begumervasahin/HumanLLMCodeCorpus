import sys
import string
from collections import Counter
languages = ['EN', 'DE']
mylang = 0
defaultFile = 'files/sample.txt'
defaultStopWords = f'stopwords/stop_words_{languages[mylang]}.txt'
defaultOut = 'out.txt'
def main():
    mystring = f"Select Language from the following: {', '.join(languages)} - default is EN: "
    slang = input(mystring).upper()
    if slang in languages:
        yourStopWords = f'stopwords/stop_words_{slang}.txt'
        print(f"Parsing your text with the {slang} stopwords")
    else:
        yourStopWords = defaultStopWords
        print("Not a valid language. Assuming English...")
    mystring = f"Select name of output text file (default is {defaultOut}): "
    sout = input(mystring)
    if sout == "":
        yourOut = defaultOut
    elif sout.endswith('.txt'):
        yourOut = sout
    else:
        yourOut = sout + '.txt'
    print(f"Printing your results to {yourOut}.")
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given {defaultFile} and {defaultStopWords} will be used as default files\n")
        sys.exit()
    elif len(sys.argv) == 2:
        yourFile = sys.argv[1]
    else:
        yourFile = defaultFile
    print(f'Using {yourFile} as file and {yourStopWords} as stop word reference, printing to {yourOut}.\n')
    indexThem(yourFile, yourStopWords, yourOut)
def indexThem(yourFile, yourStopWords, yourOut):
    punct = set(string.punctuation)
    with open(yourFile, 'r', encoding='utf-8') as f:
        bookWords = f.read().lower().split()
        bookWords = [word.strip(string.punctuation) for word in bookWords]
    with open(yourStopWords, 'r', encoding='utf-8') as f:
        stopWords = f.read().splitlines()
    finalWords = [word for word in bookWords if word not in stopWords]
    topWords = Counter(finalWords)
    total = sum(topWords.values())
    frequent = total / len(topWords)
    tops = {word: count for word, count in topWords.items() if count >= frequent}
    final = sorted(tops.items())
    with open(yourOut, 'w') as outFile:
        for word, count in final:
            outFile.write(f'{word}: {count}\n')
if __name__ == '__main__':
    main()