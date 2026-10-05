import os
from buildTree import firstRound
def main():
    print_header()
    init()
def print_header():
    print("\n\nAndre Luiz LourenÃ§o de Andrade - 14/0016295")
    print("Teoria da Informacao - Huffman Compressor\n")
def init():
    user_input = input("Please enter a string or file to compress >>> ")
    if "-c" in user_input:
        file_name = user_input.split()[1]
        print(f"You chose {file_name} as the file to be compressed...")
        read_file(file_name)
    else:
        print("\nThis function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
        init()
def read_file(file_name):
    with open(file_name, "rb") as file:
        content = file.read()
        create_dictionary(content)
def create_dictionary(content):
    frequency_dict = {}
    for char in content:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    calculate_proportions(frequency_dict, content)
def calculate_proportions(frequency_dict, content):
    symbol_set = frequency_dict.keys()
    total_content_length = len(content)
    for key in frequency_dict:
        frequency_dict[key] /= total_content_length
    sorted_frequencies = sorted(frequency_dict.values(), reverse=True)
    firstRound(sorted_frequencies, symbol_set)
if __name__ == "__main__":
    main()