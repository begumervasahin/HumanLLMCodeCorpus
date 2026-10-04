class Files:
    def load_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    def save_table(self, content, filename):
        with open(filename, 'w') as file:
            file.write(content)
    def save_file(self, filename, text, codes):
        binary_string = ''.join(codes[char] for char in text)
        encoded_text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string) - 8, 8))
        if len(binary_string) % 8 != 0:
            remainder = binary_string[-(len(binary_string) % 8):]
            encoded_text += "~~~" + remainder
        with open(filename, 'w') as file:
            file.write(encoded_text)
    def load_table(self, filename):
        with open(filename, 'r') as file:
            text = file.read()
        codes = {}
        pairs = text.split(",")
        index = 0
        while index < len(pairs):
            if pairs[index] == "":
                pairs[index + 1] = "," + pairs[index + 1]
                del pairs[index]
            else:
                index += 1
        for pair in pairs:
            symbol, code = pair.split("-")
            codes[code] = symbol
        return codes