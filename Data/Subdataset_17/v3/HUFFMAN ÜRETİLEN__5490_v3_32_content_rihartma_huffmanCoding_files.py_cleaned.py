class Files:
    def load_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    def save_table(self, table_text, filename):
        with open(filename, 'w') as file:
            file.write(table_text)
    def save_encoded_file(self, filename, text, codes):
        binary_string = ''.join(codes[char] for char in text)
        encoded_text = ''.join(
            chr(int(binary_string[i:i + 8], 2))
            for i in range(0, len(binary_string) - len(binary_string) % 8, 8)
        )
        remaining_bits = len(binary_string) % 8
        if remaining_bits != 0:
            encoded_text += f"~~~{binary_string[-remaining_bits:]}"
        with open(filename, 'w') as file:
            file.write(encoded_text)
    def load_table(self, filename):
        with open(filename, "r") as file:
            content = file.read()
        codes = {}
        pairs = content.split(",")
        for pair in pairs:
            if pair:
                char, code = pair.split("-")
                codes[code] = char
        return codes
if __name__ == "__main__":
    files = Files()
    original_text = files.load_file("example.txt")
    huffman_codes = {
        'a': '101',
        'b': '111',
        'c': '000',
    }
    files.save_table("a-101,b-111,c-000", "huffman_table.txt")
    files.save_encoded_file("encoded_file.txt", original_text, huffman_codes)
    loaded_codes = files.load_table("huffman_table.txt")
    print(loaded_codes)