import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
def read_responses_from_files(directory, data_filename):
    responses = []
    for filename in os.listdir(directory):
        if filename.endswith(data_filename):
            with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
                try:
                    data = f.read()
                    data = data[data.index("[\"java.util.ArrayList"):data.index("]")] + "]"
                    data = data.replace("\\", "\\\\")
                    responses += json.loads(data)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    return responses
def filter_responses(responses):
    return [x for x in responses if "\\x3C" in x]
def find_similar_phrases(phrase, responses):
    return difflib.get_close_matches(phrase, responses)
def format_and_print_match(match):
    formatted_match = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(match.replace("\\x", "%")))
    print('', formatted_match, '\n')
def main():
    data_filename = "data.txt"
    directory = "."
    responses = read_responses_from_files(directory, data_filename)
    responses = filter_responses(responses)
    while True:
        phrase = input("Enter the given phrase: ")
        possibilities = find_similar_phrases(phrase, responses)
        if possibilities:
            format_and_print_match(possibilities[0])
        else:
            print('', colored("There is no mistake", "green"), '\n')
if __name__ == "__main__":
    main()