class Node:
    def __init__(self):
        self.child = dict()
        self.weight = 0
def addWord(root, s, w):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.weight < w:
            temp.weight = w
def findMaxWeight(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.weight
root = Node()
n, q = map(int, input().split())
for i in range(n):
    line = list(input().split())
    addWord(root, line[0], int(line[1]))
for i in range(q):
    query = input()
    print(findMaxWeight(root, query))
class Node:
    def __init__(self):
        self.child = dict()
        self.common = 0
def addWord(root, s):
    temp = root
    res = 0
    for level in range(len(s)):
        char = s[level]
        if char not in temp.child:
            temp.child[char] = Node()
        temp = temp.child[char]
        temp.common += 1
        res = max(res, temp.common * (level + 1))
    return res
t = int(input())
for k in range(t):
    root = Node()
    result = 0
    n = int(input())
    for i in range(n):
        result = max(result, addWord(root, input()))
    print('Case {}: {}'.format(k + 1, result))
class Node:
    def __init__(self):
        self.child = dict()
        self.countWord = 0
def addWord(root, s):
    temp = root
    s_prefix_another = True
    another_prefix_s = False
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
            s_prefix_another = False
        temp = temp.child[ch]
        if temp.countWord != 0:
            another_prefix_s = True
    temp.countWord += 1
    return s_prefix_another or another_prefix_s
t = int(input())
for i in range(t):
    n = int(input())
    is_inconsistent = False
    root = Node()
    for _ in range(n):
        if not is_inconsistent:
            is_inconsistent = addWord(root, input())
        else:
            input()
    print('Case {}: {}'.format(i + 1, 'NO' if is_inconsistent else 'YES'))
class Node:
    def __init__(self):
        self.child = dict()
        self.countPassword = 0
def addPassword(root, s):
    temp = root
    s_prefix_another = True
    another_prefix_s = False
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
            s_prefix_another = False
        temp = temp.child[ch]
        if temp.countPassword != 0:
            another_prefix_s = True
    temp.countPassword += 1
    return s_prefix_another or another_prefix_s
n = int(input())
root = Node()
is_vulnerable = False
for i in range(n):
    if not is_vulnerable:
        is_vulnerable = addPassword(root, input())
    else:
        input()
print('vulnerable' if is_vulnerable else 'non vulnerable')
class Node:
    def __init__(self):
        self.child = dict()
        self.contactCount = 0
def addContact(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.contactCount += 1
def findContact(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return 0
        temp = temp.child[ch]
    return temp.contactCount
n = int(input())
root = Node()
for i in range(n):
    line = list(input().split())
    if line[0] == 'add':
        addContact(root, line[1])
    else:
        print(findContact(root, line[1]))