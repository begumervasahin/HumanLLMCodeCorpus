class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = 0
        self.common = 0
        self.word_count = 0
        self.contact_count = 0
def add_word(root, word, weight):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        if node.weight < weight:
            node.weight = weight
def find_max_weight(root, prefix):
    node = root
    for char in prefix:
        if char not in node.children:
            return -1
        node = node.children[char]
    return node.weight
def add_word_with_common(root, word):
    node = root
    max_result = 0
    for level, char in enumerate(word):
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.common += 1
        max_result = max(max_result, node.common * (level + 1))
    return max_result
def add_word_and_check_inconsistency(root, word):
    node = root
    is_prefix_of_another = True
    another_is_prefix_of_s = False
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
            is_prefix_of_another = False
        node = node.children[char]
        if node.word_count > 0:
            another_is_prefix_of_s = True
    node.word_count += 1
    return is_prefix_of_another or another_is_prefix_of_s
def add_contact(root, contact):
    node = root
    for char in contact:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.contact_count += 1
def find_contact(root, contact):
    node = root
    for char in contact:
        if char not in node.children:
            return 0
        node = node.children[char]
    return node.contact_count
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
    for case_number in range(t):
        root = TrieNode()
        result = 0
        n = int(input())
        for _ in range(n):
            word = input().strip()
            result = max(result, add_word_with_common(root, word))
        print(f'Case {case_number + 1}: {result}')
def problem_3():
    t = int(input())
    for case_number in range(t):
        n = int(input())
        root = TrieNode()
        is_inconsistent = False
        for _ in range(n):
            word = input().strip()
            if not is_inconsistent:
                is_inconsistent = add_word_and_check_inconsistency(root, word)
        print(f'Case {case_number + 1}: {"NO" if is_inconsistent else "YES"}')
def problem_4():
    n = int(input())
    root = TrieNode()
    is_vulnerable = False
    for _ in range(n):
        word = input().strip()
        if not is_vulnerable:
            is_vulnerable = add_word_and_check_inconsistency(root, word)
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