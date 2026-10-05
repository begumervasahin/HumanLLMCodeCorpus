import os
from buildTree import firstRound
print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
print("Teoria da Informacao - Huffman Compressor\n")
symbol = []
def main():
    init()
def init():
    my_stringorfile = input("Please enter a string or file to compress >>> ")
    if my_stringorfile.find("-c") != -1:
        file = my_stringorfile.split()[1]
        print("You chose", file, "as the file to be compressed...")
        readFile(file)
        return file
    else:
        string = my_stringorfile
        readString(string)
        return string
def readString(string):
    print("\nThis function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
    init()
def readFile(file):
    try:
        with open(file, "rb") as f:
            content = f.read()
            dictionary(content)
            return content
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        init()
def contentSize(contentFile):
    contentSize = len(contentFile)
    return contentSize
def dictionary(contentFile):
    dict = {}
    for i in contentFile:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    proportions(dict, contentFile)
    global symbol
    symbol = dict.keys()
    return dict
def proportions(dictionary, contentFile):
    for key in dictionary:
        dictionary[key] /= len(contentFile)
    proportions = sorted(dictionary.values(), reverse=True)
    firstRound(proportions, symbol)
    return proportions
if __name__ == "__main__":
    main()