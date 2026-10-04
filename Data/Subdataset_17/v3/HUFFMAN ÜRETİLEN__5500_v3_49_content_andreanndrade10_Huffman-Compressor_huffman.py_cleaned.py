import os
from buildTree import firstRound
def main():
    display_header()
    input_data = prompt_user_input()
    if is_compression_requested(input_data):
        file_path = extract_file_path(input_data)
        content = read_file_content(file_path)
    else:
        content = notify_unavailable_feature()
    if content:
        frequency_dict = calculate_byte_frequencies(content)
        compute_and_print_proportions(frequency_dict, len(content))
def display_header():
    print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
    print("Teoria da Informação - Huffman Compressor\n")
def prompt_user_input():
    return input("Please enter a string or the file path to compress (e.g., '-c <file_path>') >>> ")
def is_compression_requested(input_data):
    return input_data.startswith("-c")
def extract_file_path(input_data):
    parts = input_data.split(maxsplit=1)
    return parts[1] if len(parts) > 1 else ""
def read_file_content(file_path):
    if not file_path:
        print("Error: No file path provided.")
        return None
    try:
        with open(file_path, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
def notify_unavailable_feature():
    print(f"\nThis feature is not yet implemented. Please select a .txt file from your directory: {os.getcwd()}")
    return None
def calculate_byte_frequencies(content):
    frequency_dict = {}
    for byte in content:
        frequency_dict[byte] = frequency_dict.get(byte, 0) + 1
    return frequency_dict
def compute_and_print_proportions(frequency_dict, total_size):
    proportions = {byte: count / total_size for byte, count in frequency_dict.items()}
    sorted_proportions = sorted(proportions.values(), reverse=True)
    symbols = list(proportions.keys())
    firstRound(sorted_proportions, symbols)
if __name__ == "__main__":
    main()