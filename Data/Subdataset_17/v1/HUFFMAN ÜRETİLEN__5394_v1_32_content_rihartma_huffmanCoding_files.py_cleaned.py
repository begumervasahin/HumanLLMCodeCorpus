class Files:
    def loadFile(self, name):
        with open(name, 'r') as file:
            text = file.read()
        return text
    def saveTable(self, text, name):
        with open(name, 'w') as file:
            file.write(text)
    def saveFile(self, name, text, codes):
        b = ''.join(codes[char] for char in text)
        filetext = ""
        for i in range(0, len(b) - 8, 8):
            filetext += chr(int(b[i:i+8], 2))
        if len(b) % 8 != 0:
            filetext += "~~~" + b[-(len(b) % 8):]
        with open(name, 'w') as file:
            file.write(filetext)
    def loadTable(self, name):
        with open(name, "r") as file:
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
            char, code = pair.split("-")
            codes[code] = char
        return codes
if __name__ == "__main__":
    files = Files()
    original_text = files.loadFile("example.txt")
    huffman_codes = {
        'a': '101',
        'b': '111',
        'c': '000',
    }
    files.saveTable("a-101,b-111,c-000", "huffman_table.txt")
    files.saveFile("encoded_file.txt", original_text, huffman_codes)
    loaded_codes = files.loadTable("huffman_table.txt")
    print(loaded_codes)