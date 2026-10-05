class Node:
    def __init__(self):
        self.child = {}
        self.weight = 0
def addWord(root, word, weight):
    temp = root
    for ch in word:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.weight < weight:
            temp.weight = weight
def findMaxWeight(root, word):
    temp = root
    for ch in word:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.weight
def processWordQueries():
    root = Node()
    n, q = map(int, input().split())
    for _ in range(n):
        word, weight = input().split()
        addWord(root, word, int(weight))
    for _ in range(q):
        query = input()
        print(findMaxWeight(root, query))
def addWordWithCommonPrefix(root, word):
    temp = root
    max_prefix_length = 0
    for level, ch in enumerate(word):
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.common += 1
        max_prefix_length = max(max_prefix_length, temp.common * (level + 1))
    return max_prefix_length
def processCommonPrefixQueries():
    t = int(input())
    for case in range(t):
        root = Node()
        result = 0
        n = int(input())
        for _ in range(n):
            result = max(result, addWordWithCommonPrefix(root, input()))
        print('Case {}: {}'.format(case + 1, result))
def addWordWithInconsistency(root, word):
    temp = root
    is_prefix_another = True
    another_prefix = False
    for ch in word:
        if ch not in temp.child:
            temp.child[ch] = Node()
            is_prefix_another = False
        temp = temp.child[ch]
        if temp.countWord != 0:
            another_prefix = True
    temp.countWord += 1
    return is_prefix_another or another_prefix
def isConsistentWords():
    t = int(input())
    for case in range(t):
        n = int(input())
        is_inconsistent = False
        root = Node()
        for _ in range(n):
            if not is_inconsistent:
                is_inconsistent = addWordWithInconsistency(root, input())
            else:
                input()
        print('Case {}: {}'.format(case + 1, 'NO' if is_inconsistent else 'YES'))
def addPassword(root, password):
    temp = root
    is_prefix_another = True
    another_prefix = False
    for ch in password:
        if ch not in temp.child:
            temp.child[ch] = Node()
            is_prefix_another = False
        temp = temp.child[ch]
        if temp.countPassword != 0:
            another_prefix = True
    temp.countPassword += 1
    return is_prefix_another or another_prefix
def isVulnerable():
    n = int(input())
    root = Node()
    is_vulnerable = False
    for _ in range(n):
        if not is_vulnerable:
            is_vulnerable = addPassword(root, input())
        else:
            input()
    print('vulnerable' if is_vulnerable else 'non vulnerable')
def addContact(root, contact):
    temp = root
    for ch in contact:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.contactCount += 1
def findContact(root, contact):
    temp = root
    for ch in contact:
        if ch not in temp.child:
            return 0
        temp = temp.child[ch]
    return temp.contactCount
def processContacts():
    n = int(input())
    root = Node()
    for _ in range(n):
        line = input().split()
        if line[0] == 'add':
            addContact(root, line[1])
        else:
            print(findContact(root, line[1]))
def main():
    processWordQueries()
    processCommonPrefixQueries()
    isConsistentWords()
    isVulnerable()
    processContacts()
if __name__ == "__main__":
    main()