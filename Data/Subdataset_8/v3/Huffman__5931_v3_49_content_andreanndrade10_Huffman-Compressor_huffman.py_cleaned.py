import os
from buildTree import firstRound
def main():
    print_header()
    user_input = get_user_input()
    process_input(user_input)
def print_header():
    print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
    print("Teoria da Informacao - Huffman Compressor\n")
def get_user_input():
    return input("Please enter a string or file to compress >>> ")
def process_input(user_input):
    if "-c" in user_input:
        file_name = user_input.split()[1]
        print(f"You chose {file_name} as the file to be compressed...")
        read_file(file_name)
    else:
        print("\nThis function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
        process_input(get_user_input())
def read_file(file_name):
    try:
        with open(file_name, "rb") as file:
            content = file.read()
            analyze_content(content)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        process_input(get_user_input())
def analyze_content(content):
    frequency_dict = create_frequency_dict(content)
    symbol_list = list(frequency_dict.keys())
    proportions = calculate_proportions(frequency_dict, content)
    firstRound(proportions, symbol_list)
def create_frequency_dict(content):
    frequency_dict = {}
    for symbol in content:
        frequency_dict[symbol] = frequency_dict.get(symbol, 0) + 1
    return frequency_dict
def calculate_proportions(frequency_dict, content):
    total_symbols = len(content)
    proportions = [frequency_dict[symbol] / total_symbols for symbol in frequency_dict]
    proportions.sort(reverse=True)
    return proportions
if __name__ == "__main__":
    main()