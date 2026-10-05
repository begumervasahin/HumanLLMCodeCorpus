class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key, data=None):
        self.root = self._insert(self.root, key, data)
    def _insert(self, node, key, data):
        if node is None:
            return Node(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        return node
    def remove(self, key):
        self.root = self._remove(self.root, key)
    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key, node.data = temp.key, temp.data
            node.right = self._remove(node.right, temp.key)
        return node
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    def inorder(self):
        self._inorder(self.root)
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(f"Key: {node.key}, Data: {node.data}")
            self._inorder(node.right)
def main():
    n = int(input("ENTER THE NUMBER OF STUDENTS: \n"))
    bst = BST()
    for i in range(n):
        print(f"\nENTER THE DETAILS OF STUDENT {i + 1}:")
        key = int(input("Enter the roll num: "))
        name = input("Enter name: ")
        add = input("Enter the address: ")
        mob = int(input("Enter the mobile number: "))
        course = input("Enter the course: ")
        print('Enter the marks in three subjects:')
        m1 = int(input("First subject: "))
        m2 = int(input("Second subject: "))
        m3 = int(input("Third subject: "))
        total = m1 + m2 + m3
        percent = total / 3
        print("Total Marks:", total)
        print("Average marks:", percent)
        bst.insert(key, {
            'name': name,
            'address': add,
            'mobile': mob,
            'course': course,
            'marks': [m1, m2, m3],
            'total': total,
            'percent': percent
        })
    print("\nBST TRAVERSAL\n")
    bst.inorder()
    print("DO YOU WANT TO DELETE ANY KEYS IN THE TREE?")
    print("IF YES ENTER y OR Y\n")
    ch = input()
    if ch.lower() == 'y':
        while ch.lower() == 'y':
            print("\nEnter the number to be deleted:")
            num = int(input())
            bst.remove(num)
            print("Enter y or Y to continue:")
            ch = input()
        print("AFTER THE DELETION :\n")
        bst.inorder()
    print("\nDO YOU WANT TO SEARCH ANY KEYS IN THE TREE?")
    print("IF YES ENTER y OR Y\n")
    ch = input()
    while ch.lower() == 'y':
        print("\nEnter the key to be searched:")
        num = int(input())
        result = bst.search(num)
        if result:
            print("Student Found:")
            print(f"Key: {result.key}, Data: {result.data}")
        else:
            print("Student not found.")
        print("Enter y or Y to continue:")
        ch = input()
    print("\n*************************END OF BST OPERATIONS*******************************\n")
if __name__ == '__main__':
    main()