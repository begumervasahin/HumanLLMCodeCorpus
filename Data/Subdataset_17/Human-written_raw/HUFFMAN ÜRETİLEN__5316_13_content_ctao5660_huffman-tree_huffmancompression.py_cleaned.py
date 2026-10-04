class Node:
    def __init__(self,frequency,char):
        self.left= None
        self.right=None
        self.frequency=frequency
        self.char=char
    def printTree(node):
        if(node.char!=None):
            print( self.char, end=" ")
        else:
             printTree(self.left)
             printTree(self.right)
class BinaryTree:
    def __init__(self,freqlist):
        self.sortedList=sorted(freqlist, key=freqlist.get)
        self.sortedList.reverse()
        self.listlength=len(self.sortedList)
        self.freqList=freqlist
        self.codeDict={}
        self.reverseDict={}
        self.nodeList=[]
    def createTree(self):
        for char in self.sortedList:
            self.nodeList.append(Node(self.freqList[char],char))
        while(True):
            self.nodeList.sort(key=lambda node:node.frequency)
            node1=self.nodeList.pop(0)
            node2=self.nodeList.pop(0)
            newNode=Node(node1.frequency+node2.frequency,None)
            if(node1.frequency>=node2.frequency):
                newNode.left=node1
                newNode.right=node2
            else:
                newNode.left=node2
                newNode.right=node1
            self.nodeList.append(newNode)
            self.nodeList.sort(key=lambda node:node.frequency)
            if(len(self.nodeList)==1):
                break
        return self.nodeList.pop(0)
    def SearchAndCode2(self, rNode, encoded):
        if (rNode is None):
            return
        if (rNode.char is not None):
            self.codeDict[rNode.char]=encoded
            self.reverseDict[encoded]=rNode.char
            print('Character is {} and Code is {}'.format(rNode.char,encoded))
            return
        lencoded = encoded + "1"
        rencoded = encoded + "0"
        self.SearchAndCode2(rNode.left, lencoded)
        self.SearchAndCode2(rNode.right, rencoded)
    def isNode(self,stringlist, node):
        s=stringlist
        if (node.char is not  None):
            return True
        if not s:
            return False
        if(s[0]== '1'):
            s.pop(0)
            return self.isNode(s,node.left)
        elif(s[0]== '0'):
            s.pop(0)
            return self.isNode(s,node.right)
        return False
    def decodeMessage(self,filelocation,node):
        file_test=open(filelocation,'r+')
        encoded=list(file_test.read())
        index=0
        string=''
        while index<len(encoded):
            indexrange=0
            while(self.isNode(encoded[index:index+indexrange],node) is False):
                indexrange+=1
                try:
                    file_test.write(self.reverseDict[''.join(encoded[index:index+indexrange])])
                    string+=(self.reverseDict[''.join(encoded[index:index+indexrange])])
                    print(self.reverseDict[''.join(encoded[index:index+indexrange])])
                except KeyError:
                    continue
            index+=indexrange
        print(string)
def countChars(filelocation):
    file_test=open(filelocation,'r')
    listofchar={}
    charCount=0
    while True:
        print('Hello')
        char=file_test.read(1)
        if not char:
            break
        if char not in listofchar:
            listofchar[char]=1
        else:
            listofchar[char]+=1
        charCount+=1
    return listofchar
def encodeMessage(filelocation,newfilelocation, tree):
    file_test=open(filelocation,'r+')
    file_output=open(newfilelocation,'w+')
    numCount=0
    for k,v in tree.reverseDict.items():
        if(v=='\n'):
            file_output.write('{}.-.{}\n'.format(k,'\\n'))
        else:
            file_output.write('{}.-.{}\n'.format(k,v))
    file_output.write('```\n')
    while True:
        char=file_test.read(1)
        if not char:
            break
        numCount+=1
        file_output.write(tree.codeDict[char])
    print('Number of bits is {}'.format(numCount/8))
aList=countChars('/Users/christao/downloads/freshprince.txt')
tree=BinaryTree(aList)
aNode=tree.createTree()
tree.SearchAndCode2(aNode,'')
encodeMessage('/Users/christao/downloads/freshprince.txt','/Users/christao/downloads/testparagraph.txt',tree)
print(tree.reverseDict)