class Node:
    def __init__(self, frequency, char):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.char = char
    def printTree(self):
        if self.char is not None:
            print(self.char, end=" ")
        else:
            if self.left:
                self.left.printTree()
            if self.right:
                self.right.printTree()
class BinaryTree:
    def __init__(self, freqlist):
        self.sortedList = sorted(freqlist, key=freqlist.get)
        self.sortedList.reverse()
        self.listlength = len(self.sortedList)
        self.freqList = freqlist
        self.codeDict = {}
        self.reverseDict = {}
        self.nodeList = []
    def createTree(self):
        for char in self.sortedList:
            self.nodeList.append(Node(self.freqList[char], char))
        while len(self.nodeList) > 1:
            self.nodeList.sort(key=lambda node: node.frequency)
            node1 = self.nodeList.pop(0)
            node2 = self.nodeList.pop(0)
            newNode = Node(node1.frequency + node2.frequency, None)
            if node1.frequency >= node2.frequency:
                newNode.left = node1
                newNode.right = node2
            else:
                newNode.left = node2
                newNode.right = node1
            self.nodeList.append(newNode)
        return self.nodeList.pop(0)
    def SearchAndCode2(self, rNode, encoded):
        if rNode is None:
            return
        if rNode.char is not None:
            self.codeDict[rNode.char] = encoded
            self.reverseDict[encoded] = rNode.char
            print(f'Character is {rNode.char} and Code is {encoded}')
            return
        self.SearchAndCode2(rNode.left, encoded + "1")
        self.SearchAndCode2(rNode.right, encoded + "0")
    def isNode(self, stringlist, node):
        if node.char is not None:
            return True
        if not stringlist:
            return False
        if stringlist[0] == '1':
            return self.isNode(stringlist[1:], node.left)
        elif stringlist[0] == '0':
            return self.isNode(stringlist[1:], node.right)
        return False
    def decodeMessage(self, filelocation, node):
        with open(filelocation, 'r') as file_test:
            encoded = list(file_test.read())
        index = 0
        decoded_string = ''
        while index < len(encoded):
            index_range = 1
            while not self.isNode(encoded[index:index + index_range], node):
                index_range += 1
            decoded_char = self.reverseDict[''.join(encoded[index:index + index_range])]
            decoded_string += decoded_char
            index += index_range
        print("Decoded Message:", decoded_string)
        return decoded_string
def countChars(filelocation):
    with open(filelocation, 'r') as file_test:
        listofchar = {}
        while True:
            char = file_test.read(1)
            if not char:
                break
            listofchar[char] = listofchar.get(char, 0) + 1
    return listofchar
def encodeMessage(filelocation, newfilelocation, tree):
    with open(filelocation, 'r') as file_test, open(newfilelocation, 'w') as file_output:
        for k, v in tree.reverseDict.items():
            file_output.write(f'{k}.-.{v if v != "\\n" else "\\n"}\n')
        file_output.write('```\n')
        while True:
            char = file_test.read(1)
            if not char:
                break
            file_output.write(tree.codeDict[char])
def main():
    aList = countChars('path/to/your/input.txt')
    tree = BinaryTree(aList)
    aNode = tree.createTree()
    tree.SearchAndCode2(aNode, '')
    encodeMessage('path/to/your/input.txt', 'path/to/your/output.txt', tree)
    print("Reverse Dictionary:", tree.reverseDict)
    tree.decodeMessage('path/to/your/output.txt', aNode)
if __name__ == "__main__":
    main()