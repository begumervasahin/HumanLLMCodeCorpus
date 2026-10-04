from PersistentBST import PBST
def display_menu(current_branch):
    print(f"\nCurrent Branch: {current_branch}\n")
    print("1. List Files")
    print("2. View File")
    print("3. New File")
    print("4. Delete File")
    print("5. Edit File")
    print("6. List Branches")
    print("7. New Branch")
    print("8. Switch Branch")
    print("9. Exit\n")
    return input("$ ").strip()
def list_files(tree, current_branch):
    print("Files:")
    tree.inFix(current_branch)
def view_file(tree, current_branch):
    name = input("Enter name of file to be opened: ").strip()
    file = tree.search(name, current_branch)
    if file is None:
        print("File does not exist!")
    else:
        print(file.getData())
def new_file(tree, current_branch):
    name = input("Enter name of new file: ").strip()
    tree.insert(name, current_branch)
def delete_file(tree, current_branch):
    name = input("Enter name of file to be deleted: ").strip()
    tree.delete(name, current_branch)
def edit_file(tree, current_branch):
    name = input("Enter name of file to be edited: ").strip()
    tree.edit(name, current_branch)
def list_branches(branches):
    print("Branches:")
    for branch in branches:
        print(branch)
def new_branch(tree, branches, current_branch):
    branch_name = input("Enter name of new branch: ").strip()
    if branch_name in branches:
        print("Branch already exists")
    else:
        branches.append(branch_name)
        tree.newBranch(branch_name, current_branch)
        return branch_name
    return current_branch
def switch_branch(branches):
    branch_name = input("Enter name of branch to switch to: ").strip()
    if branch_name not in branches:
        print("Branch doesn't exist")
        return None
    return branch_name
def main():
    print("\n\tARCHEIO")
    tree = PBST()
    current_branch = "master"
    branches = ["master"]
    while True:
        choice = display_menu(current_branch)
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
            current_branch = new_branch(tree, branches, current_branch)
        elif choice == "8":
            new_branch_name = switch_branch(branches)
            if new_branch_name:
                current_branch = new_branch_name
        elif choice in ["9", "exit"]:
            print("Exiting...")
            break
        else:
            print("Invalid Input")
if __name__ == "__main__":
    main()