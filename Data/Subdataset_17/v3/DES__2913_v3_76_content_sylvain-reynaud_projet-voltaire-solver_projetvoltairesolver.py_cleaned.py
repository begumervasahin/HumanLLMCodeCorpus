import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
DATA_FILENAME = "data.txt"
DIRECTORY = "."
def load_data_from_files(directory, filename):
    collected_responses = []
    for file in os.listdir(directory):
        if file.endswith(filename):
            with open(os.path.join(directory, file), 'r', encoding="utf-8") as f:
                data = f.read()
                try:
                    start_index = data.index("[\"java.util.ArrayList")
                    end_index = data.index("]") + 1
                    json_data = data[start_index:end_index].replace("\\", "\\\\")
                    collected_responses.extend(json.loads(json_data))
                except (ValueError, json.JSONDecodeError):
                    pass
    return collected_responses
def filter_responses(responses):
    return [response for response in responses if "\\x3C" in response]
def highlight_matches(possibility):
    decoded_string = unquote(possibility.replace("\\x", "%"))
    return re.sub(r"<B>(.*?)<\/B>", lambda match: colored(match.group(1), "green"), decoded_string)
def main():
    responses = load_data_from_files(DIRECTORY, DATA_FILENAME)
    filtered_responses = filter_responses(responses)
    while True:
        phrase = input("Entrer la phrase donnee : ")
        possibilities = difflib.get_close_matches(phrase, filtered_responses)
        if possibilities:
            highlighted_text = highlight_matches(possibilities[0])
            print(highlighted_text, '\n')
        else:
            print(colored("Il n'y a pas de faute", "green"), '\n')
if __name__ == '__main__':
    main()