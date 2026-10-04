class TrieNode:
    def __init__(self):
        self.children = dict()
        self.weight = 0
        self.common = 0
        self.countWord = 0
        self.contactCount = 0
def add_word(root, word, weight):
    temp = root
    for ch in word:
        if ch not in temp.children:
            temp.children[ch] = TrieNode()
        temp = temp.children[ch]
        if temp.weight < weight:
            temp.weight = weight
def find_max_weight(root, prefix):
    temp = root
    for ch in prefix:
        if ch not in temp.children:
            return -1
        temp = temp.children[ch]
    return temp.weight
def add_word_with_common(root, word):
    temp = root
    res = 0
    for level in range(len(word)):
        char = word[level]
        if char not in temp.children:
            temp.children[char] = TrieNode()
        temp = temp.children[char]
        temp.common += 1
        res = max(res, temp.common * (level + 1))
    return res
def add_word_and_check_inconsistency(root, word):
    temp = root
    s_prefix_another = True
    another_prefix_s = False
    for ch in word:
        if ch not in temp.children:
            temp.children[ch] = TrieNode()
            s_prefix_another = False
        temp = temp.children[ch]
        if temp.countWord != 0:
            another_prefix_s = True
    temp.countWord += 1
    return s_prefix_another or another_prefix_s
def add_contact(root, contact):
    temp = root
    for ch in contact:
        if ch not in temp.children:
            temp.children[ch] = TrieNode()
        temp = temp.children[ch]
        temp.contactCount += 1
def find_contact(root, contact):
    temp = root
    for ch in contact:
        if ch not in temp.children:
            return 0
        temp = temp.children[ch]
    return temp.contactCount
def problem_1():
    root = TrieNode()
    n, q = map(int, input().split())
    for _ in range(n):
        word, weight = input().split()
        add_word(root, word, int(weight))
    for _ in range(q):
        prefix = input().strip()
        print(find_max_weight(root, prefix))
def problem_2():
    t = int(input())
    for k in range(t):
        root = TrieNode()
        result = 0
        n = int(input())
        for _ in range(n):
            word = input().strip()
            result = max(result, add_word_with_common(root, word))
        print(f'Case {k + 1}: {result}')
def problem_3():
    t = int(input())
    for i in range(t):
        n = int(input())
        is_inconsistent = False
        root = TrieNode()
        for _ in range(n):
            if not is_inconsistent:
                is_inconsistent = add_word_and_check_inconsistency(root, input().strip())
            else:
                input().strip()
        print(f'Case {i + 1}: {"NO" if is_inconsistent else "YES"}')
def problem_4():
    n = int(input())
    root = TrieNode()
    is_vulnerable = False
    for _ in range(n):
        if not is_vulnerable:
            is_vulnerable = add_word_and_check_inconsistency(root, input().strip())
        else:
            input().strip()
    print('vulnerable' if is_vulnerable else 'non vulnerable')
def problem_5():
    n = int(input())
    root = TrieNode()
    for _ in range(n):
        command, value = input().split()
        if command == 'add':
            add_contact(root, value)
        else:
            print(find_contact(root, value))
def main():
    problem_selection = int(input("Select problem to solve (1-5): "))
    if problem_selection == 1:
        problem_1()
    elif problem_selection == 2:
        problem_2()
    elif problem_selection == 3:
        problem_3()
    elif problem_selection == 4:
        problem_4()
    elif problem_selection == 5:
        problem_5()
    else:
        print("Invalid selection.")
if __name__ == "__main__":
    main()