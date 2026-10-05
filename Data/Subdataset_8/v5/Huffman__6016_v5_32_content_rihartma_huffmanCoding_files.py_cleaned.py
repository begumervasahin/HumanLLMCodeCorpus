class Files:
    def load_file(self, name):
        with open(name, 'r') as file:
            return file.read()
    def save_table(self, text, name):
        with open(name, 'w') as file:
            file.write(text)
    def save_file(self, name, text, codes):
        binary_text = ''.join(codes[char] for char in text)
        file_text = ""
        for i in range(0, len(binary_text) - 8, 8):
            file_text += chr(int(binary_text[i:i + 8], 2))
        if len(binary_text) % 8 != 0:
            file_text += "~~~" + binary_text[len(binary_text) - 1 - len(binary_text) % 8: len(binary_text)]
        with open(name, 'w') as file:
            file.write(file_text)
    def load_table(self, name):
        with open(name, "r") as file:
            text = file.read()
        codes = {}
        pairs = text.split(",")
        pairs = [pair.strip() for pair in pairs if pair.strip()]
        for pair in pairs:
            char, code = pair.split("-")
            codes[code] = char
        return codes