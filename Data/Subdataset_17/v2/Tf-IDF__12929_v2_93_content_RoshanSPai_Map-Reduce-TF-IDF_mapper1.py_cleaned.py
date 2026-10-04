import sys
import os
stop_words = set([
    "a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at",
    "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever",
    "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i",
    "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must",
    "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said",
    "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these",
    "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while",
    "who", "whom", "why", "will", "with", "would", "yet", "you", "your"
])
file_path = os.getenv('map_input_file', 'default.txt')
file_name = os.path.basename(file_path)
for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        if word.lower() not in stop_words:
            print(f'{word}&{file_name}\t1')