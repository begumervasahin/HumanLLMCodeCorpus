import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
data_filename = "data.txt"
directory = "."
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
    return [response for response in responses if "\\x3C" in response]
def main():
    responses = read_responses_from_files(directory, data_filename)
    responses = filter_responses(responses)
    while True:
        phrase = input("Enter the given phrase: ")
        possibilities = difflib.get_close_matches(phrase, responses)
        if possibilities:
            formatted_match = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(possibilities[0].replace("\\x", "%")))
            print('', formatted_match, '\n')
        else:
            print('', colored("No mistakes found", "green"), '\n')
if __name__ == "__main__":
    main()