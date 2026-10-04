import sys
import os
def fonk1():
    return set([
        "a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at",
        "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever",
        "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i",
        "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must",
        "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said",
        "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these",
        "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while",
        "who", "whom", "why", "will", "with", "would", "yet", "you", "your"
    ])
def fonk2():
    b1 = os.getenv('map_input_file', 'default.txt')
    return os.path.basename(b1)
def fonk3(b3, b4):
    for line in sys.stdin:
        b2 = line.strip().split()
        for word in b2:
            if word.lower() not in b3:
                print(f'{word}&{b4}\t1')
def fonk4():
    b3 = fonk1()
    b4 = fonk2()
    fonk3(b3, b4)
if b5 = = '__main__':
    fonk4()