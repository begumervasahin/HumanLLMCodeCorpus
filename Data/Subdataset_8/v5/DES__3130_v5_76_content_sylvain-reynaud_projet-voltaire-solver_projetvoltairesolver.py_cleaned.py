import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
DATA_FILENAME = "data.txt"
DIRECTORY = "."
def read_responses_from_files(directory, data_filename):
    responses = []
    for filename in os.listdir(directory):
        if filename.endswith(data_filename):
            with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
                try:
                    data = f.read()
                    start_index = data.index("[\"java.util.ArrayList")
                    end_index = data.index("]")
                    data = data[start_index:end_index + 1] + "]"
                    data = data.replace("\\", "\\\\")
                    responses += json.loads(data)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    return responses
def filter_responses(responses):
    return [response for response in responses if "\\x3C" in response]
def get_closest_match(phrase, responses):
    return difflib.get_close_matches(phrase, responses)
def format_and_print_match(match):
    formatted_match = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(match.replace("\\x", "%")))
    print('', formatted_match, '\n')
def main():
    responses = read_responses_from_files(DIRECTORY, DATA_FILENAME)
    responses = filter_responses(responses)
    while True:
        phrase = input("Enter the given phrase: ")
        possibilities = get_closest_match(phrase, responses)
        if possibilities:
            format_and_print_match(possibilities[0])
        else:
            print('', colored("No mistakes found", "green"), '\n')
if __name__ == "__main__":
    main()