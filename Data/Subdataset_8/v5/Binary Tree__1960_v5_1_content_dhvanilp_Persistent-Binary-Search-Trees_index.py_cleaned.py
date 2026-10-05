from PersistentBST import PersistentBinarySearchTree
def print_menu(current_branch, branches):
    print("\nCurrent Branch:", current_branch)
    print("\n1. List Files\n2. View File\n3. New File\n4. Delete File\n5. Edit File\n6. List Branches\n7. New Branch\n8. Switch Branch\n9. Exit\n")
def list_files(tree, current_branch):
    print("Files: ")
    tree.inFix(current_branch)
def view_file(tree, current_branch):
    name = input("Enter name of file to be opened: ")
    file = tree.search(name, current_branch)
    if file is None:
        print("File does not exist!")
    else:
        print(file.getData())
def new_file(tree, current_branch):
    name = input("Enter name of new file: ")
    tree.insert(name, current_branch)
def delete_file(tree, current_branch):
    name = input("Enter name of file to be deleted: ")
    tree.delete(name, current_branch)
def edit_file(tree, current_branch):
    name = input("Enter name of file to be edited: ")
    tree.edit(name, current_branch)
def list_branches(branches):
    print("Branches:")
    for branch in branches:
        print(branch)
def new_branch(tree, current_branch, branches):
    branch_name = input("Enter name of new branch: ")
    if branch_name in branches:
        print("Branch already exists")
        return
    branches.append(branch_name)
    tree.newBranch(branch_name, current_branch)
    return branch_name
def switch_branch(current_branch, branches):
    branch_name = input("Enter name of branch to switch to: ")
    if branch_name not in branches:
        print("Branch doesn't exist")
        return current_branch
    return branch_name
def main():
    print("\n\tARCHEIO")
    tree = PersistentBinarySearchTree()
    current_branch = "master"
    branches = ["master"]
    while True:
        print_menu(current_branch, branches)
        choice = input("$ ").lower()
        print()
        if choice == "1":
            list_files(tree, current_branch)
        elif choice == "2":
            view_file(tree, current_branch)
        elif choice == "3":
            new_file(tree, current_branch)
        elif choice == "4":
            delete_file(tree, current_branch)
        elif choice == "5":
            edit_file(tree, current_branch)
        elif choice == "6":
            list_branches(branches)
        elif choice == "7":
            current_branch = new_branch(tree, current_branch, branches)
        elif choice == "8":
            current_branch = switch_branch(current_branch, branches)
        elif choice == "exit" or choice == "9":
            print("Exiting...")
            break
        elif choice == "debug":
            print()
        else:
            print("Invalid Input")
if __name__ == "__main__":
    main()