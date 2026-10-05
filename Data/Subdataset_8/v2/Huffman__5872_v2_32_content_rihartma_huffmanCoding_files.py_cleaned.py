class Files:
    def load_file(self, name):
        text = ""
        with open(name, 'r') as file:
            text = file.read()
        return text
    def save_table(self, text, name):
        with open(name, 'w') as file:
            file.write(text)
    def save_file(self, name, text, codes):
        binary_string = ''
        for char in text:
            binary_string += codes[char]
        file_text = ""
        for i in range(0, len(binary_string) - 8, 8):
            file_text += chr(int(binary_string[i:i + 8], 2))
        if len(binary_string) % 8 != 0:
            file_text += "~~~" + binary_string[len(binary_string) - 1 - len(binary_string) % 8:len(binary_string)]
        with open(name, 'w') as file:
            file.write(file_text)
    def load_table(self, name):
        with open(name, "r") as file:
            text = file.read()
        codes = {}
        pairs = text.split(",")
        pairs = [pair.strip() for pair in pairs]
        for pair in pairs:
            if pair:
                t = pair.split("-")
                codes[t[1]] = t[0]
        return codes
files = Files()
codes = files.load_table("codes.txt")
print(codes)
text = files.load_file("input.txt")
print(text)
files.save_file("output.txt", text, codes)