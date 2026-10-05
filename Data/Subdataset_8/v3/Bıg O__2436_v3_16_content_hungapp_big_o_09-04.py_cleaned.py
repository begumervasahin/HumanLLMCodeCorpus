class Node:
    def __init__(self):
        self.child = {}
        self.weight = 0
        self.common = 0
        self.countWord = 0
        self.countPassword = 0
        self.contactCount = 0
def addWord(root, word, weight):
    current = root
    for char in word:
        if char not in current.child:
            current.child[char] = Node()
        current = current.child[char]
        if current.weight < weight:
            current.weight = weight
def findMaxWeight(root, word):
    current = root
    for char in word:
        if char not in current.child:
            return -1
        current = current.child[char]
    return current.weight
def addWordWithCommonPrefix(root, word):
    current = root
    max_prefix_length = 0
    for level, char in enumerate(word):
        if char not in current.child:
            current.child[char] = Node()
        current = current.child[char]
        current.common += 1
        max_prefix_length = max(max_prefix_length, current.common * (level + 1))
    return max_prefix_length
def isConsistentWords(t):
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
def addWordWithInconsistency(root, word):
    current = root
    is_prefix_another = True
    another_prefix = False
    for char in word:
        if char not in current.child:
            current.child[char] = Node()
            is_prefix_another = False
        current = current.child[char]
        if current.countWord != 0:
            another_prefix = True
    current.countWord += 1
    return is_prefix_another or another_prefix
def addPassword(root, password):
    current = root
    is_prefix_another = True
    another_prefix = False
    for char in password:
        if char not in current.child:
            current.child[char] = Node()
            is_prefix_another = False
        current = current.child[char]
        if current.countPassword != 0:
            another_prefix = True
    current.countPassword += 1
    return is_prefix_another or another_prefix
def isVulnerable(n):
    root = Node()
    is_vulnerable = False
    for _ in range(n):
        if not is_vulnerable:
            is_vulnerable = addPassword(root, input())
        else:
            input()
    print('vulnerable' if is_vulnerable else 'non vulnerable')
def addContact(root, contact):
    current = root
    for char in contact:
        if char not in current.child:
            current.child[char] = Node()
        current = current.child[char]
        current.contactCount += 1
def findContact(root, contact):
    current = root
    for char in contact:
        if char not in current.child:
            return 0
        current = current.child[char]
    return current.contactCount
def processContacts(n):
    root = Node()
    for _ in range(n):
        line = input().split()
        if line[0] == 'add':
            addContact(root, line[1])
        else:
            print(findContact(root, line[1]))
def main():
    root = Node()
    n, q = map(int, input().split())
    for _ in range(n):
        word, weight = input().split()
        addWord(root, word, int(weight))
    for _ in range(q):
        query = input()
        print(findMaxWeight(root, query))
    t = int(input())
    for case in range(t):
        root = Node()
        result = 0
        n = int(input())
        for _ in range(n):
            result = max(result, addWordWithCommonPrefix(root, input()))
        print('Case {}: {}'.format(case + 1, result))
    t = int(input())
    isConsistentWords(t)
    n = int(input())
    isVulnerable(n)
    n = int(input())
    processContacts(n)
if __name__ == "__main__":
    main()