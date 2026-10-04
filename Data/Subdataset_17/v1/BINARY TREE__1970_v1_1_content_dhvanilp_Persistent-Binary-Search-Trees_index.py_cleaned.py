class FileNode:
    def __init__(self, name, data=''):
        self.name = name
        self.data = data
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
class PBSTNode:
    def __init__(self, key, data=''):
        self.key = key
        self.data = FileNode(key, data)
        self.left = None
        self.right = None
class PBST:
    def __init__(self):
        self.branches = {'master': None}
    def search(self, key, branch='master'):
        node = self.branches[branch]
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.data
        return None
    def insert(self, key, branch='master'):
        if branch not in self.branches:
            print("Branch doesn't exist")
            return
        node = self.branches[branch]
        parent = None
        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                print("File already exists!")
                return
        new_node = PBSTNode(key)
        if parent is None:
            self.branches[branch] = new_node
        else:
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
    def delete(self, key, branch='master'):
        if branch not in self.branches:
            print("Branch doesn't exist")
            return
        self.branches[branch], deleted = self._delete_rec(self.branches[branch], key)
        if deleted:
            print("File deleted")
        else:
            print("File not found")
    def _delete_rec(self, node, key):
        if node is None:
            return node, False
        if key < node.key:
            node.left, deleted = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right, deleted = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            min_larger_node = self._min_value_node(node.right)
            node.key, node.data = min_larger_node.key, min_larger_node.data
            node.right, _ = self._delete_rec(node.right, min_larger_node.key)
            return node, True
        return node, deleted
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def edit(self, key, branch='master'):
        file = self.search(key, branch)
        if file is None:
            print("File does not exist!")
        else:
            new_data = input("Enter new data for the file: ")
            file.setData(new_data)
    def inFix(self, branch='master'):
        if branch not in self.branches:
            print("Branch doesn't exist")
            return
        self._inFix_rec(self.branches[branch])
        print()
    def _inFix_rec(self, node):
        if node is not None:
            self._inFix_rec(node.left)
            print(node.key, end=" ")
            self._inFix_rec(node.right)
    def newBranch(self, new_branch, base_branch):
        if base_branch not in self.branches:
            print("Base branch doesn't exist")
            return
        self.branches[new_branch] = self.branches[base_branch]
from PersistentBST import PBST
print("\n\tARCHEIO")
Tree = PBST()
currentBranch = "master"
prevBranch = None
branches = ["master"]
while True:
    print("\nCurrent Branch:", currentBranch)
    print("\n1. List Files\n2. View File\n3. New File\n4. Delete File\n5. Edit File\n6. List Branches\n7. New Branch\n8. Switch Branch\n9. Exit\n")
    choice = input("$ ")
    print()
    if choice == "1":
        print("Files: ")
        Tree.inFix(currentBranch)
    elif choice == "2":
        name = input("Enter name of file to be opened: ")
        file = Tree.search(name, currentBranch)
        if file is None:
            print("File does not exist!")
        else:
            print(file.getData())
    elif choice == "3":
        name = input("Enter name of new file: ")
        Tree.insert(name, currentBranch)
    elif choice == "4":
        name = input("Enter name of file to be deleted: ")
        Tree.delete(name, currentBranch)
    elif choice == "5":
        name = input("Enter name of file to be edited: ")
        Tree.edit(name, currentBranch)
    elif choice == "6":
        print("Branches:")
        for branch in branches:
            print(branch)
    elif choice == "7":
        branchName = input("Enter name of new branch: ")
        if branchName in branches:
            print("Branch already exists")
            continue
        branches.append(branchName)
        prevBranch, currentBranch = currentBranch, branchName
        Tree.newBranch(currentBranch, prevBranch)
    elif choice == "8":
        branchName = input("Enter name of branch to switch to: ")
        if branchName not in branches:
            print("Branch doesn't exist")
            continue
        prevBranch, currentBranch = currentBranch, branchName
    elif choice == "exit" or choice == "9":
        file = None
        Tree = None
        print("Exiting...")
        break
    elif choice == "debug":
        print()
    else:
        print("Invalid Input")