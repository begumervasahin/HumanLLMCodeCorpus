import sys
import string
from collections import Counter
languages = ['EN', 'DE']
default_language_index = 0
default_file_path = 'files/sample.txt'
default_stop_words_path = 'stopwords/stop_words_%s.txt' % languages[default_language_index]
default_output_file = 'out.txt'
def main():
    language_prompt = "Select Language from the following:%s - default is EN: " % ' '.join(languages)
    selected_language = raw_input(language_prompt).upper()
    if selected_language in languages:
        stop_words_path = 'stopwords/stop_words_%s.txt' % selected_language
        print "Parsing your text with the %s stopwords" % selected_language
    else:
        stop_words_path = default_stop_words_path
        print "Not a valid language. Assuming English..."
    output_file_prompt = "Select name of output text file (default is %s ): " % default_output_file
    output_file_name = raw_input(output_file_prompt)
    output_file_name = output_file_name if output_file_name.endswith('.txt') else output_file_name + '.txt'
    output_file_path = default_output_file if output_file_name == "" else output_file_name
    print "Printing your results to %s." % output_file_path
    your_file = sys.argv[1] if len(sys.argv) > 1 else default_file_path
    print 'Using %s as file and %s as stop word reference, printing to %s.' % (your_file, stop_words_path, output_file_path)
    print
    index_them(your_file, stop_words_path, output_file_path)
def index_them(your_file, stop_words_path, output_file_path):
    punctuation = set(string.punctuation)
    book_words = open(your_file).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    book_words = [word.rstrip(string.punctuation).lstrip(string.punctuation) for word in book_words]
    stop_words = open(stop_words_path).read().decode("utf-8-sig").encode("utf-8").splitlines()
    final_words = [word for word in book_words if word not in stop_words]
    top_words = Counter(final_words)
    frequency = []
    for word in top_words:
        frequency.append(top_words[word])
    total_words_count = sum(top_words.values())
    frequent_occurrence_threshold = total_words_count / (len(top_words))
    frequent_words = {key: value for (key, value) in top_words.iteritems() if value >= frequent_occurrence_threshold}
    sorted_frequent_words = sorted(frequent_words.items(), key=lambda x: x[0])
    output_file = open(output_file_path, 'w+')
    for word_index in range(len(sorted_frequent_words)):
        print >> output_file, '%s: %s' % (sorted_frequent_words[word_index][0], sorted_frequent_words[word_index][1])
    output_file.close()
if __name__ == '__main__':
    main()